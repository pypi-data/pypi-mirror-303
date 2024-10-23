import logging
import os

import yaml
from aivm_grpc.share_service_pb2 import ModelType


class AIVMGlobalConfig:
    __instance = None
    __initialized = False

    GRPC_TO_AIVM = {
        ModelType.LeNet5: "LeNet5",
        ModelType.BertTiny: "BertTiny",
        ModelType.MeshKeepAlive: "MeshKeepAlive",
    }

    AIVM_TO_GRPC = {v: k for k, v in GRPC_TO_AIVM.items()}

    def __new__(cls):
        if cls.__instance is None:
            cls.__instance = super().__new__(cls)
        return cls.__instance

    def __init__(self, path=None):
        if not self.__initialized:  # Ensure initialization runs only once
            if path is None:
                path = os.path.join(
                    os.path.dirname(os.path.abspath(__file__)), "config/global.yaml"
                )
            with open(path, "r") as f:
                self.config = yaml.safe_load(f)
            self._models = {
                model_name: self.config["models"][model_name]["type"]
                for model_name, model_type in self.config["models"].items()
            }
            self.__initialized = True  # Mark as initialized

    def new_model(self, model_name, model_type):
        if model_name in self._models:
            raise ValueError(f"Model {model_name} already exists")
        self._models[model_name] = model_type
        self.config["models"][model_name] = {"type": model_type}
        logging.debug(
            f"New model added {model_name} {model_type} M:{self._models} MTT:{self.model_to_type}"
        )

    @staticmethod
    def _translate(value, transform):
        if isinstance(value, dict):
            return {
                AIVMGlobalConfig._translate(k, transform): AIVMGlobalConfig._translate(
                    v, transform
                )
                for k, v in value.items()
            }
        elif isinstance(value, list):
            return [AIVMGlobalConfig._translate(v, transform) for v in value]
        elif isinstance(value, (str, int)) and value in transform:
            return transform[value]
        else:
            return value

    @staticmethod
    def to_grpc(dic):
        return AIVMGlobalConfig._translate(dic, AIVMGlobalConfig.AIVM_TO_GRPC)

    @staticmethod
    def from_grpc(dic):
        return AIVMGlobalConfig._translate(dic, AIVMGlobalConfig.GRPC_TO_AIVM)

    @property
    def models(self):
        return self._models

    @property
    def model_types(self):
        return list(self.config["model_types"].keys())

    @property
    def model_to_type(self):
        return {
            model_name: model_type["type"]
            for model_name, model_type in self.config["models"].items()
        }


cfg = AIVMGlobalConfig()
