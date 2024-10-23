import logging
import tempfile
from queue import Empty, Queue

import aivm_grpc.share_service_pb2 as sspb2
import aivm_grpc.share_service_pb2_grpc as ssgrpc
import grpc

from aivm_config import cfg


class ModelServicer(ssgrpc.ModelServicer):
    def __init__(
        self,
    ):
        self.model_queue = Queue()

    def SendModel(self, request_iterator, context):
        logging.debug("Receiving model...")
        try:
            onnx_file_path = tempfile.mktemp(suffix=".onnx")
            model_name = None
            with open(onnx_file_path, "wb") as f:
                for chunk in request_iterator:
                    if model_name is None:
                        model_name = chunk.model
                    if model_name != chunk.model:
                        raise ValueError("Model name mismatch between chunks")
                    logging.debug(f"Received chunk {chunk.chunk_number}")
                    f.write(chunk.data)  # Write each chunk's data to the file
            logging.info(f"Received model {onnx_file_path} for {chunk.model}")
            # Add the model to the global configuration
            cfg.new_model(
                model_name=chunk.model, model_type=cfg.from_grpc(chunk.model_type)
            )
            logging.info(
                f"Model added to global configuration {cfg.model_to_type} {cfg.models}"
            )
            # Add the model to the model queue
            self.model_queue.put(
                (chunk.model, cfg.from_grpc(chunk.model_type), onnx_file_path)
            )
            return sspb2.ModelResponse(message="Model received successfully")
        except Exception as e:
            logging.error(f"Error receiving model: {e}")
            context.set_code(grpc.StatusCode.INTERNAL)
            context.set_details(f"Error receiving model: {e}")
            return sspb2.ModelResponse(message=f"Error receiving model: {e}")

    def get_model_upload(self):
        if not self.model_queue.empty():
            return self.model_queue.get()
