from concurrent import futures

import aivm_grpc.share_service_pb2 as sspb2
import aivm_grpc.share_service_pb2_grpc as ssgrpc
import grpc
from google.protobuf.empty_pb2 import Empty


class ShareServicer(ssgrpc.ShareServicer):

    def __init__(self):
        super().__init__()

        self.received_shares = None

    def GetServerConfiguration(self, request, context):
        config = sspb2.ServerConfiguration(
            world_size=2,
            precision=16,
            models=["LeNet5", "BertTiny"],
            model_types=[sspb2.ModelType.LeNet5, sspb2.ModelType.BertTiny],
        )
        return config

    def GetPrediction(self, request, context):
        share_type = (
            "Arithmetic" if request.type == sspb2.ShareType.ARITHMETIC else "Binary"
        )
        print(
            "Received shares:",
            share_type,
            request.shares,
            request.shape,
            request.precision,
            request.model,
        )
        self.received_shares = request.shares
        return request

    def GetPreprocessing(self, request, context):
        print(
            "Received prep request:",
            request.model_type,
        )
        return Empty()


class ModelServicer(ssgrpc.ModelServicer):
    def __init__(self):
        self.model_file = "/tmp/received_model.onnx"  # Destination file for the model

    def SendModel(self, request_iterator, context):
        print("Receiving model...")
        try:
            with open(self.model_file, "wb") as f:
                for chunk in request_iterator:
                    print(f"Received chunk {chunk.chunk_number}")
                    f.write(chunk.data)  # Write each chunk's data to the file
            print("Received model")
            return sspb2.ModelResponse(message="Model received successfully")
        except Exception as e:
            context.set_code(grpc.StatusCode.INTERNAL)
            return sspb2.ModelResponse(message=f"Error receiving model: {e}")


def serve():
    server = grpc.server(futures.ThreadPoolExecutor(max_workers=10))
    ssgrpc.add_ShareServicer_to_server(ShareServicer(), server)
    ssgrpc.add_ModelServicer_to_server(ModelServicer(), server)
    server.add_insecure_port("[::]:50051")
    server.start()
    print("Server started on port 50051")
    server.wait_for_termination()


if __name__ == "__main__":
    serve()
