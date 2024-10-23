import logging
import os

import curl
import torch

from aivm.models.model_benchmark import BaseModelBenchmark, time_me
from aivm_config import cfg


class ONNXModels(BaseModelBenchmark):
    def __init__(self, device="cpu"):
        super().__init__(device)
        from aivm.models.onnx_models.bert_tiny_sms import \
            LUTConfig as BertTinyLUTConfig
        from aivm.models.onnx_models.bert_tiny_sms import \
            onnx_file_path as BertTinySMSONNX
        from aivm.models.onnx_models.bert_tiny_sms import \
            tokenizer as BertTinyTokenizer

        models = [
            ("BertTinySMS", BertTinyLUTConfig(), BertTinySMSONNX),
        ]
        for model_name, lut_config, onnx_file_path in models:
            logging.debug(f"Creating model {model_name}...")
            curl.init_luts(model_name, lut_config)
            with open(onnx_file_path, "rb") as f:
                private_model = curl.nn.from_onnx(f, track_execution=False)
                private_model.encrypt()
            self.models[model_name] = private_model

    @staticmethod
    @time_me
    def time_llm(x, model):
        # Overwrite the time_llm function to use the correct inputs
        tokens = x[0].reshape(1, -1)
        attention_mask = x[1].reshape(1, -1)
        return model(tokens, attention_mask)

    def new_model(self, model_name, model_type, model_path):
        if model_name in self.models:
            logging.warning(f"Model {model_name} already exists.")
            return
        from aivm.models.onnx_models.bert_tiny_sms import \
            LUTConfig as BertTinyLUTConfig

        curl.init_luts(model_name, BertTinyLUTConfig())
        with open(model_path, "rb") as f:
            private_model = curl.nn.from_onnx(f, track_execution=False)
            private_model.encrypt()
        self.models[model_name] = private_model
