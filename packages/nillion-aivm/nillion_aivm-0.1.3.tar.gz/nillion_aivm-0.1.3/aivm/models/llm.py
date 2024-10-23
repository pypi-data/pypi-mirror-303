import logging
import os

import curl
import torch

from aivm.models.model_benchmark import BaseModelBenchmark


class LLMs(BaseModelBenchmark):
    """LLM benchmarks runtime and error of curl functions against PyTorch

    Args:
        tensor_size (int or tuple): size of tensor for benchmarking runtimes
    """

    def __init__(self, device="cpu"):
        super().__init__(device)

        from aivm.models.llm_models.bert import BertBase, BertLarge, BertTiny
        from aivm.models.llm_models.bert import LUTConfig as BertLUTConfig
        from aivm.models.llm_models.gpt import GPT2, GPTNeo
        from aivm.models.llm_models.gpt import LUTConfig as GPTLUTConfig

        tensor_size = (1, 10)
        all_models = {
            "BertTiny": (BertTiny, BertLUTConfig()),
        }

        self.tensor_size = tensor_size
        for name, (model, model_lut_config) in all_models.items():
            logging.debug(f"Creating model {name}...")
            curl.init_luts(name, model_lut_config)
            m_clear = model(seq_len=tensor_size[1], full=True)
            if hasattr(m_clear, "to"):
                m_clear = m_clear.to(self.device)
            self.models[name] = m_clear.encrypt(src=0)
