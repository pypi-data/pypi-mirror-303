import curl.nn as nn


class MeshKeepAlive(nn.Module):
    def __init__(
        self,
    ):
        super(MeshKeepAlive, self).__init__()
        self.fc = nn.Linear(1, 1)

    def forward(self, x, target=None):
        x = self.fc(x)
        return x


# Use DefaultLUTConfig as LUTConfig from lut_config.py
from curl.config.lut_config import DefaultLUTConfig

LUTConfig = DefaultLUTConfig
