import logging
from queue import Empty, Queue

import aivm_grpc.share_service_pb2 as sspb2
import aivm_grpc.share_service_pb2_grpc as ssgrpc
import curl
import grpc
import torch
from curl.mpc.ptype import ptype
from google.protobuf.empty_pb2 import Empty as grpcEmpty

from aivm.server.preprocessing import PreprocessingManager
from aivm_config import cfg


class ClientServicer(ssgrpc.ShareServicer):

    def __init__(
        self,
        world_size,
        rank,
        precision,
        proxy,
    ):
        super().__init__()

        self.proxy = proxy

        self.preprocessing_manager = PreprocessingManager()
        self.world_size = world_size
        self.precision = precision
        self.rank = rank

        self.requests = Queue()
        self.responses = Queue()

    def GetServerConfiguration(self, request, context):
        return sspb2.ServerConfiguration(
            world_size=self.world_size,
            precision=self.precision,
            models=list(cfg.models.keys()),
            model_types=cfg.to_grpc(list(cfg.model_to_type.values())),
        )

    def GetPrediction(self, request, context):
        share_type = (
            ptype.arithmetic
            if request.type == sspb2.ShareType.ARITHMETIC
            else ptype.binary
        )
        logging.debug(
            f"Received shares: type={share_type}, shape={request.shape}, precision={request.precision}, model={request.model}"
        )
        model_type = cfg.from_grpc(request.model_type)
        if request.model not in cfg.models:
            context.set_details(f"Model {request.model} not found")
            context.set_code(grpc.StatusCode.NOT_FOUND)
            return sspb2.Shares()

        if model_type != cfg.model_to_type[request.model]:
            context.set_details(
                f"Model {request.model} has type {request.model_type}, but expected {cfg.model_to_type[request.model]}"
            )
            context.set_code(grpc.StatusCode.NOT_FOUND)
            return sspb2.Shares()

        if (
            request.shape
            != cfg.config["model_types"][cfg.models[request.model]]["input_shape"]
        ):
            context.set_details(
                f"Model {request.model} has shape {cfg.models[request.model]}, got {request.shape}"
            )
            context.set_code(grpc.StatusCode.NOT_FOUND)
            return sspb2.Shares()

        if len(request.shares) != torch.prod(torch.tensor(request.shape)):
            context.set_details(
                f"Expected {torch.prod(torch.tensor(request.shape))} shares, got {len(request.shares)}"
            )
            context.set_code(grpc.StatusCode.INVALID_ARGUMENT)
            return sspb2.Shares()

        tensor = torch.tensor(request.shares, dtype=torch.int64)
        tensor = tensor.view(*request.shape)

        cryptensor = curl.from_shares(
            share=tensor, precision=request.precision, ptype=share_type
        )

        self.requests.put(((cryptensor, request.model, model_type), False))
        if self.rank == 0:
            logging.info(
                f"[Party {self.rank}] {request.model} request added to queue. Backlog: [{len(self.requests.queue)}]"
            )

        response = self.responses.get()

        if self.rank == 0:
            logging.info(f"[Party {self.rank}] {request.model} response sent to client")
        return sspb2.Shares(
            shares=response.flatten().tolist(),
            shape=response.shape,
            precision=request.precision,
            type=request.type,
            model=request.model,
            model_type=request.model_type,
        )

    def GetPreprocessing(self, request, context):
        model_type = cfg.from_grpc(request.model_type)
        logging.info(f"Received PreprocessingRequest for model {model_type}")

        self.requests.put(
            (
                self.preprocessing_manager.produce_request_for_model(
                    model_type=model_type
                ),
                True,
            )
        )
        logging.debug(
            f"{model_type} request added to queue. Backlog [{len(self.requests.queue)}]"
        )
        return grpcEmpty()

    def add_response(self, response):
        if (
            not self.preprocessing_manager.preprocessing
            and not self.preprocessing_manager.keep_alive
        ):
            logging.debug("Preprocessing not in progress, added to queue")
            self.responses.put(response)
        else:
            logging.debug("Preprocessing in progress, response not added to queue")

    def get_request(self, timeout=None):
        if self.rank > 0:  # Only the first party schedules preprocessing
            timeout = None
        try:
            return self.requests.get(timeout=timeout)
        except Empty as e:

            model_type = self.preprocessing_manager.produce_request()

            if model_type is None:
                # No preprocessing to do
                return None, None
            # Send information to each of the other nodes
            schedule_preprocessing(self.proxy, model_type)
            return None, None


def schedule_preprocessing(addr, model_type):
    with grpc.insecure_channel(addr) as channel:
        stub = ssgrpc.ProxyStub(channel)
        stub.GetPreprocessing(
            sspb2.PreprocessingRequest(model_type=cfg.to_grpc(model_type))
        )
