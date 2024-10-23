#!/usr/bin/env python3

# Copyright (c) Facebook, Inc. and its affiliates.
#
# This source code is licensed under the MIT license found in the
# LICENSE file in the root directory of this source tree.

from .config import CurlConfig
from .lut_config import ApproximationsConfig, DefaultLUTConfig, LLMLUTConfig

cfg = CurlConfig()

__all__ = ["cfg", "DefaultLUTConfig", "LLMLUTConfig", "ApproximationsConfig"]
