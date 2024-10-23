import logging

import curl
import pandas as pd

from aivm.models.model_benchmark import BaseModelBenchmark


class Utils(BaseModelBenchmark):
    def __init__(self, device="cpu"):
        super().__init__(device)
        from aivm.models.mesh_keep_alive_model.mesh_keep_alive import \
            LUTConfig as MKALUTConfig
        from aivm.models.mesh_keep_alive_model.mesh_keep_alive import \
            MeshKeepAlive

        self.model_name = "MeshKeepAlive"
        logging.debug(f"Creating Mesh Keep Alive...")
        curl.init_luts(self.model_name, MKALUTConfig())
        self.models[self.model_name] = MeshKeepAlive()
        self.models[self.model_name] = (
            self.models[self.model_name].to(self.device).encrypt(src=0)
        )
