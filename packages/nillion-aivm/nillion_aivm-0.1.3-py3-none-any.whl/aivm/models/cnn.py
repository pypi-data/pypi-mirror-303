import logging
import os

import curl
import torch

from aivm.models.cnn_models.lenet5 import LeNet5
from aivm.models.cnn_models.lenet5 import LUTConfig as CNNLUTConfig
from aivm.models.model_benchmark import BaseModelBenchmark
from aivm_config import cfg


class CNNs(BaseModelBenchmark):
    def __init__(self, device="cpu"):
        super().__init__(device)
        models = [
            ("LeNet5MNIST", CNNLUTConfig()),
        ]
        for model_name, lut_config in models:
            logging.debug(f"Creating model {model_name}...")
            curl.init_luts(model_name, lut_config)
            self.models[model_name] = LeNet5()
            self.models[model_name].load_state_dict(
                torch.load(
                    os.path.join(
                        os.path.dirname(__file__),
                        cfg.config["models"][model_name]["weights"],
                    ),
                    weights_only=False,
                )
            )
            self.models[model_name] = (
                self.models[model_name].to(self.device).encrypt(src=0)
            )

    def new_model(self, model_name, model_type, model_path):

        if model_name in self.models:
            logging.warning(f"Model {model_name} already exists.")
            return
        curl.init_luts(model_name, CNNLUTConfig())
        self.models[model_name] = LeNet5()
        self.models[model_name].load_state_dict(
            torch.load(
                model_path,
                weights_only=False,
            )
        )
        self.models[model_name] = self.models[model_name].to(self.device).encrypt(src=0)
