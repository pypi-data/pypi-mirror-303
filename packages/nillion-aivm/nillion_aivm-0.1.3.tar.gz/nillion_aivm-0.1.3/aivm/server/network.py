import logging
from concurrent import futures

import aivm_grpc.share_service_pb2_grpc as ssgrpc
import grpc

from aivm.server.client_servicer import ClientServicer
from aivm.server.model_servicer import ModelServicer


class AIVMServicer:

    def __init__(
        self,
        world_size,
        rank,
        precision,
        nodes,
        proxy,
        host="[::]",
        port=50051,
    ):
        self.nodes = nodes
        self.host = host
        self.port = port
        self.proxy = proxy

        self.client_servicer = ClientServicer(world_size, rank, precision, self.proxy)
        self.model_servicer = ModelServicer()

        self.server = None

    def serve(
        self,
    ):
        self.server = grpc.server(futures.ThreadPoolExecutor(max_workers=10))
        ssgrpc.add_ShareServicer_to_server(self.client_servicer, self.server)
        ssgrpc.add_ModelServicer_to_server(self.model_servicer, self.server)
        self.server.add_insecure_port(f"{self.host}:{self.port}")
        self.server.start()
        logging.debug(f"Client Connection Server started on port {self.port}")

    def wait_to_end(self):
        if self.server is None:
            raise Exception("Client Server not started")
        self.server.wait_for_termination()

    def stop(self):
        if self.server is None:
            raise Exception("Client Server not started")
        self.server.stop(0)
