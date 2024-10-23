#!/usr/bin/env python3

# Copyright (c) Facebook, Inc. and its affiliates.
#
# This source code is licensed under the MIT license found in the
# LICENSE file in the root directory of this source tree.

import os
from contextlib import contextmanager

import yaml
from omegaconf import OmegaConf


class CurlConfig:
    """
    Configuration object used to store configurable parameters for CrypTen.

    This object acts as a nested dictionary, but can be queried using dot-notation(
    e.g. querying or setting `cfg.a.b` is equivalent to `cfg['a']['b']`).

    Users can load a CrypTen config from a file using `cfg.load_config(filepath)`.

    Users can temporarily override a config parameter using the contextmanager temp_override:

        .. code-block:: python

        cfg.a.b = outer     # sets cfg["a"]["b"] to outer value

        with cfg.temp_override("a.b", inner):
            print(cfg.a.b)  # prints inner value

        print(cfg.a.b)  # prints outer value
    """

    __DEFAULT_CONFIG = {
        "communicator": {"verbose": False},
        "debug": {"debug_mode": False, "validation_mode": False},
        "encoder": {
            "precision_bits": 16,
            "trunc_method": {"prod": "egk", "lut": "egk"},
        },
        "mpc": {"active_security": False, "provider": "TFP", "protocol": "beaver"},
        "nn": {
            "dpsmpc": {
                "protocol": "layer_estimation",
                "skip_loss_forward": True,
                "cache_pred_size": True,
            }
        },
    }

    def __init__(self, config_dict=None):
        self.load_config(config_dict)

    @classmethod
    def get_default_config(cls):
        return cls.__DEFAULT_CONFIG

    def load_config(self, config_dict):
        """Loads config from a dictionary"""
        if config_dict is None:
            config_dict = CurlConfig.get_default_config()
        self.config = OmegaConf.create(config_dict)

    def set_config(self, config):
        if isinstance(config, CurlConfig):
            self.config = config.config
        else:
            self.config = config

    def __getattribute__(self, name):
        try:
            return object.__getattribute__(self, name)
        except AttributeError:
            keys = name.split(".")
            result = getattr(self.config, keys[0])
            for key in keys[1:]:
                result = getattr(result, key)
            return result

    def __getitem__(self, name):
        return self.__getattribute__(name)

    def __setattr__(self, name, value):
        if name == "config":
            object.__setattr__(self, name, value)
        try:
            # Can only set attribute if already exists
            object.__getattribute__(self, name)
            object.__setattr__(self, name, value)
        except AttributeError:
            dotlist = [f"{name}={value}"]
            update = OmegaConf.from_dotlist(dotlist)
            self.config = OmegaConf.merge(self.config, update)

    def __setitem__(self, name, value):
        self.__setattr__(name, value)

    @contextmanager
    def temp_override(self, override_dict):
        old_config = self.config
        try:
            dotlist = [f"{k}={v}" for k, v in override_dict.items()]
            update = OmegaConf.from_dotlist(dotlist)
            self.config = OmegaConf.merge(self.config, update)
            yield
        finally:
            self.config = old_config
