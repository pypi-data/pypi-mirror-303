import copy
from contextlib import contextmanager

import curl


class LUTConfig:
    """
    A base class that implements the Singleton pattern.
    """

    def __init__(self):
        self.config_names = {}

    @staticmethod
    def dict_fingerprint(dict):
        fingerprint = "".join(f"[{k}:{v}]" for k, v in dict.items())
        return fingerprint

    def get_function_fingerprint(self, name, prefix):
        key = name
        if key in ["sin", "cos"]:
            key = "trigonometry"
        elif key in ["tanh", "sigmoid"]:
            key = "sigmoid_tanh"
        if key not in self.config:
            raise ValueError(f"Function {key}:{name} not found in config")
        return f"{prefix}_{name}_{LUTConfig.dict_fingerprint(self.config[key])}"

    def new_name(self, name, prefix):
        key = f"{prefix}_{name}"
        if key in self.config_names:
            print("Config names: ", self.config_names.keys())
            raise ValueError(f"Function {key} already exists in LUT config")
        fingerprint = self.get_function_fingerprint(name, prefix)
        self.config_names[f"{prefix}_{name}"] = fingerprint
        return fingerprint

    def get_name(self, name, prefix):
        key = f"{prefix}_{name}"
        if key not in self.config_names:
            raise ValueError(f"Function {name} not found in LUT config")
        return self.config_names[key]

    @staticmethod
    def _apply_dict(config, dic):
        for key, value in dic.items():
            if key not in config:
                raise ValueError(f"{key} not found in LUT config")
            if isinstance(value, dict):
                LUTConfig._apply_dict(config[key], value)
            else:
                config[key] = value
        return config

    def apply_dict(self, dic):
        self.config = LUTConfig._apply_dict(self.config, dic)

    @contextmanager
    def temp_override(self, override_dict):
        old_config = copy.deepcopy(self.config)
        try:
            self.apply_dict(override_dict)
            yield
        finally:
            self.config = old_config

    @staticmethod
    def _get_dict(dic, keys):
        result = {}
        for key in keys:
            if key not in dic:
                raise ValueError(f"{key} not found in LUT config")
            dic = dic[key]
            if isinstance(dic, dict):
                result[key] = LUTConfig._get_dict(dic, keys[key])
            else:
                result[key] = dic
        return result

    def get_dict(self, keys):
        return LUTConfig._get_dict(self.config, keys)

    def __getitem__(self, index):
        if isinstance(index, dict):
            return self.get_dict(index)

        if index not in self.config:
            raise ValueError(f"{index} not found in LUT config")
        return self.config[index]

    def __setitem__(self, index, value):
        if index not in self.config:
            raise ValueError(f"{index} not found in LUT config")
        self.config[index] = value

    def __repr__(self):
        # Return the raw dictionary in string form for __repr__
        return str(self.config)

    def __str__(self):
        indent = 4
        result = []

        def recursive_print(d, level=0):
            spacing = " " * (level * indent)
            if isinstance(d, dict):
                for key, value in d.items():
                    if isinstance(value, dict):
                        result.append(f"{spacing}{key}:")
                        recursive_print(value, level + 1)
                    else:
                        result.append(f"{spacing}{key}: {value}")
            else:
                result.append(f"{spacing}{d}")

        recursive_print(self.config)
        return "\n".join(result)


class DefaultLUTConfig(LUTConfig):

    def __init__(self):

        self.config = {
            "max": {
                "method": "log_reduction",
            },
            "exp": {
                "method": "limit",
                "iterations": 8,
                "haar_size_bits": 5,
                "bior_size_bits": 5,
                "lut_max_bits": 6,
                "all_neg": True,
                "neg_lut_size": 256,
            },
            "log": {
                "method": "bior",
                "iterations": 2,
                "exp_iterations": 8,
                "order": 8,
                "haar_size_bits": 8,
                "bior_size_bits": 7,
                "lut_max_bits": 6,
            },
            "reciprocal": {
                "method": "haar",
                "nr_iters": 10,
                "log_iters": 1,
                "all_pos": True,
                "initial": None,
                "haar_size_bits": 8,
                "bior_size_bits": 7,
                "lut_max_bits": 6,
            },
            "sqrt": {
                "method": "bior",
                "nr_iters": 5,
                "nr_initial": None,
                "haar_size_bits": 7,
                "bior_size_bits": 7,
                "lut_max_bits": 8,
            },
            "inv_sqrt": {
                "method": "tailored_haar",
                "haar_size_bits": 11,
                "bior_size_bits": 11,
                "lut_max_bits": 8,
                "tailored_0_lut_max_bits": 0,
                "tailored_0_haar_size_bits": 12,
                "tailored_1_lut_max_bits": 8,
                "tailored_1_haar_size_bits": 8,
            },
            "sigmoid_tanh": {
                "method": "haar",
                "terms": 32,
                "haar_size_bits": 6,
                "bior_size_bits": 5,
                "sigmoid_lut_max_bits": 4,  # [-16, 16] for "bior"
                "tanh_lut_max_bits": 3,  # [-8, 8]
            },
            "trigonometry": {
                "method": "bior",
                "haar_size_bits": 5,
                "bior_size_bits": 5,
                "lut_max_bits": 6,
                "iterations": 10,
            },
            "erf": {
                "method": "bior",
                "iterations": 8,
                "haar_size_bits": 5,
                "bior_size_bits": 7,
                "lut_max_bits": 2,  # [-4, 4]
            },
            "gelu": {
                "method": "bior",
                "haar_size_bits": 4,
                "bior_size_bits": 4,
                "lut_max_bits": 2,
            },
            "silu": {
                "method": "bior",
                "haar_size_bits": 4,
                "bior_size_bits": 6,
                "lut_max_bits": 4,  # [-16, 16] for "bior"
            },
        }

        super().__init__()


class LLMLUTConfig(LUTConfig):

    def __init__(self):
        self.config = {
            "max": {
                "method": "log_reduction",
            },
            "exp": {
                "method": "limit",
                "iterations": 8,
                "haar_size_bits": 5,
                "bior_size_bits": 5,
                "lut_max_bits": 6,
                "all_neg": True,
                "neg_lut_size": 256,
            },
            "log": {
                "method": "bior",
                "iterations": 2,
                "exp_iterations": 8,
                "order": 8,
                "haar_size_bits": 8,
                "bior_size_bits": 8,
                "lut_max_bits": 6,
            },
            "reciprocal": {
                "method": "bior",
                "nr_iters": 10,
                "log_iters": 1,
                "all_pos": True,
                "initial": None,
                "haar_size_bits": 8,
                "bior_size_bits": 7,
                "lut_max_bits": 6,
            },
            "sqrt": {
                "method": "bior",
                "nr_iters": 3,
                "nr_initial": None,
                "haar_size_bits": 6,
                "bior_size_bits": 6,
                "lut_max_bits": 6,
            },
            "inv_sqrt": {
                "method": "bior",
                "haar_size_bits": 16,
                "bior_size_bits": 10,
                "lut_max_bits": 1,
            },
            "sigmoid_tanh": {
                "method": "bior",
                "terms": 32,
                "haar_size_bits": 8,
                "bior_size_bits": 8,
                "sigmoid_lut_max_bits": 6,
                "tanh_lut_max_bits": 5,
            },
            "trigonometry": {
                "method": "bior",
                "haar_size_bits": 8,
                "bior_size_bits": 8,
                "lut_max_bits": 5,
                "iterations": 10,
            },
            "erf": {
                "method": "bior",
                "iterations": 8,
                "haar_size_bits": 8,
                "bior_size_bits": 8,
                "lut_max_bits": 5,
            },
            "gelu": {
                "method": "bior-lut-only",
                "haar_size_bits": 4,
                "bior_size_bits": 4,
                "lut_max_bits": 2,
            },
            "silu": {
                "method": "bior-lut-only",
                "haar_size_bits": 4,
                "bior_size_bits": 4,
                "lut_max_bits": 4,
            },
        }

        super().__init__()


class ApproximationsConfig(LUTConfig):

    def __init__(self):
        self.config = {
            "max": {
                "method": "log_reduction",
            },
            "exp": {
                "method": "limit",
                "iterations": 8,
            },
            "log": {
                "method": "iter",
                "iterations": 2,
                "exp_iterations": 8,
                "order": 8,
            },
            "reciprocal": {
                "method": "NR",
                "nr_iters": 10,
                "log_iters": 1,
                "all_pos": True,
                "initial": None,
            },
            "sqrt": {
                "method": "NR",
                "nr_iters": 3,
                "nr_initial": None,
            },
            "inv_sqrt": {
                "method": "NR",
            },
            "sigmoid_tanh": {
                "method": "reciprocal",
                "terms": 32,
            },
            "trigonometry": {
                "method": "NR",
                "iterations": 10,
            },
            "erf": {
                "method": "Taylor",
                "iterations": 8,
            },
            "gelu": {
                "method": "erf",
            },
            "silu": {
                "method": "sigmoid",
            },
        }
        super().__init__()
