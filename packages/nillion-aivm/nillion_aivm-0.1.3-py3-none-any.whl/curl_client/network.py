import logging
import os
import random
from concurrent.futures import ThreadPoolExecutor, as_completed

import aivm_grpc.share_service_pb2 as sspb2
import aivm_grpc.share_service_pb2_grpc as ssgrpc
import grpc
import torch
from google.protobuf.empty_pb2 import Empty

ModelType = sspb2.ModelType
__all__ = ["NetworkManager", "ModelType"]


class NetworkManager:

    def __init__(self, host=["localhost:50050"]):
        self.host = host
        self.stub = self.init_stub(host)
        self.__server_configuration = None

    @property
    def server_configuration(self):
        if self.__server_configuration is None:
            self.__server_configuration = self.get_server_configuration()
        return self.__server_configuration

    def retrieve_server_configuration(self):
        self.__server_configuration = self.get_server_configuration()

    def init_stub(self, host):
        channel = grpc.insecure_channel(host)
        stub = ssgrpc.ProxyStub(channel)
        return stub

    def get_prediction(self, shares, model, precision_bits, model_type):
        if not model in self.server_configuration.models:
            raise ValueError(
                f"Model {model} not supported by server: Supported {self.server_configuration.models}"
            )

        share_messages = []
        for party_shares in shares:
            share_message = sspb2.Shares(
                shares=party_shares.flatten().tolist(),
                shape=party_shares.shape,
                precision=precision_bits,
                type=sspb2.ShareType.ARITHMETIC,
                model=model,
                model_type=model_type,
            )
            share_messages.append(share_message)

        messages = sspb2.ClientShares(shares=share_messages)
        try:
            results = self.stub.GetPrediction(messages)
        except grpc.RpcError as e:
            logging.error(e)
            return None
        results = [
            torch.tensor(result.shares, dtype=torch.int64).view(*result.shape)
            for result in results.shares
        ]

        return results

    def get_server_configuration(self):
        return self.stub.GetServerConfiguration(Empty())

    @staticmethod
    def model_file_iterator(
        file_path, model_name, model_type, chunk_size=1024 * 1024
    ):  # 1 MB chunks
        """Generator to yield file chunks for gRPC upload."""
        chunk_number = 0
        with open(file_path, "rb") as f:
            while True:
                chunk = f.read(chunk_size)
                if not chunk:
                    break
                yield sspb2.ModelChunk(
                    data=chunk,
                    chunk_number=chunk_number,
                    model=model_name,
                    model_type=model_type,
                )
                chunk_number += 1

    def upload_model(self, model_path, model_name, model_type):
        """Send model file to gRPC server."""
        # Check if the file exists and is not empty
        if not os.path.isfile(model_path):
            logging.error(f"Error: File '{model_path}' does not exist.")
            return

        if os.path.getsize(model_path) == 0:
            logging.error(f"Error: File '{model_path}' is empty.")
            return

        results = self.stub.SendModel(
            NetworkManager.model_file_iterator(model_path, model_name, model_type),
        )

        return results


if __name__ == "__main__":
    nm = NetworkManager(["localhost:50051"])
    print(nm.get_server_configuration())
    print(nm.get_prediction(torch.tensor([[1, 2, 3], [4, 5, 6]]), "BertTiny", 16))
    print(
        nm.upload_model("/tmp/tmpa347ym8s.onnx", "BertTinySMS", "Bert_tiny")
    )  # Replace with your ONNX model path
