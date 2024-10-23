import os

import aivm_grpc.share_service_pb2 as sspb2
import aivm_grpc.share_service_pb2_grpc as ssgrpc
import grpc
from google.protobuf.empty_pb2 import Empty


def model_file_iterator(file_path, chunk_size=1024 * 1024):  # 1 MB chunks
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
                model="LeNet5",
                model_type=sspb2.ModelType.LeNet5,
            )
            chunk_number += 1


def send_model_to_server(stub, file_path):
    """Send model file to gRPC server."""
    # Check if the file exists and is not empty
    if not os.path.isfile(file_path):
        print(f"Error: File '{file_path}' does not exist.")
        return

    if os.path.getsize(file_path) == 0:
        print(f"Error: File '{file_path}' is empty.")
        return

    response = stub.SendModel(model_file_iterator(file_path))
    print(response.message)


def run():
    with grpc.insecure_channel("localhost:50050") as channel:
        stub = ssgrpc.ProxyStub(channel)

        # GetServerConfiguration
        config = stub.GetServerConfiguration(Empty())
        print(
            f"Server configuration: World Size={config.world_size}, Precision={config.precision}"
        )

        # GetPrediction
        shares = [
            sspb2.Shares(
                shares=[1, 2, 3],
                shape=[3],
                precision=16,
                type=sspb2.ShareType.ARITHMETIC,
                model="GPT2",
            )
        ]
        print("SHARES:", stub.GetPrediction(sspb2.ClientShares(shares=shares)))

        stub.GetPreprocessing(
            sspb2.PreprocessingRequest(model_type=sspb2.ModelType.LeNet5)
        )

        model_path = (
            "../../examples/test_model.onnx"  # Replace with your ONNX model path
        )
        send_model_to_server(stub, model_path)


if __name__ == "__main__":
    run()
