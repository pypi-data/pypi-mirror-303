import logging
import math

import curl
import numpy as np
import pywt
import torch
from curl.config import cfg
from curl.cuda import CUDALongTensor


class LookupTables:

    LUTs = {}

    """Use to create a singleton"""

    def __new__(cls, *args, **kwds):
        """
        >>> s = Singleton()
        >>> p = Singleton()
        >>> id(s) == id(p)
        True
        """
        it_id = "__it__"
        # getattr will dip into base classes, so __dict__ must be used
        it = cls.__dict__.get(it_id, None)
        if it is not None:
            return it
        it = object.__new__(cls)
        setattr(cls, it_id, it)
        it.init(*args, **kwds)
        # it.initialize_luts(device=device)
        return it

    def init(self, *args, **kwds):

        self.lut_configs = {}  # maps the name of the program to the LUT configuration
        self.current_config = None

    def get_config(self):
        if self.current_config is None:
            raise ValueError("No LUT configuration set")
        return self.current_config

    def get_config_by_name(self, name):
        return self.lut_configs[name]

    def set_config(self, config):
        self.current_config = config

    def set_config_by_name(self, name):
        self.set_config(self.lut_configs[name])

    def initialize_config(self, name, lut_config, device=None):
        logging.debug("Initializing LUTs for", name)
        self.initialize_luts(lut_config, device=device)
        self.lut_configs[name] = lut_config

    def initialize_default(self, device=None):
        self.initialize_config(
            "default", curl.config.lut_config.DefaultLUTConfig(), device=device
        )

    def set_default(self):
        self.set_config_by_name("default")

    @classmethod
    def generate_haar(cls, max_bits, lut_bits, function, name, negative_values=False):
        if name in cls.LUTs:
            return None  # already initialized a LUT with same name and thus properties
        scale = 1 << cfg.encoder.precision_bits
        max_element = 1 << max_bits
        depth = max_bits + cfg.encoder.precision_bits - lut_bits
        if negative_values:
            full = function(
                np.linspace(
                    -max_element + 1 / scale, max_element, (2 * max_element * scale)
                )
            )
        else:
            full = function(np.linspace(1.0 / scale, max_element, max_element * scale))
        coeffs, *_ = pywt.wavedec(full, "haar", level=depth)
        cls.LUTs[name] = torch.tensor(coeffs * 2 ** (-depth / 2) * scale).long()

    @classmethod
    def generate_bior(cls, max_bits, lut_bits, function, name, negative_values=False):
        if name in cls.LUTs:
            return None  # already initialized a LUT with same name and thus properties
        scale = 1 << cfg.encoder.precision_bits
        max_element = 1 << max_bits
        depth = max_bits + cfg.encoder.precision_bits - lut_bits
        if negative_values:
            full = function(
                np.linspace(
                    -max_element + 1 / scale, max_element, (2 * max_element * scale)
                )
            )
            coeffs, *_ = pywt.wavedec(full, "bior2.2", level=depth)
            coeffs = np.stack(
                [
                    np.roll(coeffs, -2)[: 2 ** (lut_bits + 1)],
                    np.roll(coeffs, -3)[: 2 ** (lut_bits + 1)],
                ]
            )
        else:
            full = function(np.linspace(1.0 / scale, max_element, max_element * scale))
            coeffs, *_ = pywt.wavedec(full, "bior2.2", level=depth)
            coeffs = np.stack(
                [
                    np.roll(coeffs, -2)[: 1 << lut_bits],
                    np.roll(coeffs, -3)[: 1 << lut_bits],
                ]
            )
        cls.LUTs[name] = torch.tensor((coeffs * scale) * 2 ** (depth * 0.5)).long()

    @classmethod
    def init_exp(cls, lut_config, scale, max_element):
        haar_name = lut_config.new_name("exp", "haar")
        bior_name = lut_config.new_name("exp", "bior")

        if haar_name in cls.LUTs and bior_name in cls.LUTs:
            return None  # already initialized a LUT with same name and thus properties

        depth = (
            1
            + lut_config.config["exp"]["lut_max_bits"]
            + cfg.encoder.precision_bits
            - lut_config.config["exp"]["haar_size_bits"]
        )
        full = np.exp(
            np.linspace(
                -max_element, max_element - 1.0 / scale, 2 * max_element * scale
            )
        )
        if haar_name not in cls.LUTs:
            max_element = 1 << lut_config.config["exp"]["lut_max_bits"]
            # HAAR

            coeffs, *_ = pywt.wavedec(full, "haar", level=depth)
            cls.LUTs[haar_name] = torch.tensor(
                coeffs * 2 ** (-depth / 2) * scale
            ).long()

        if bior_name not in cls.LUTs:
            # BIOR
            depth = (
                1
                + lut_config.config["exp"]["lut_max_bits"]
                + cfg.encoder.precision_bits
                - lut_config.config["exp"]["bior_size_bits"]
            )
            coeffs, *_ = pywt.wavedec(full, "bior2.2", level=depth)
            coeffs = coeffs[: 1 << lut_config.config["exp"]["bior_size_bits"]]
            coeffs = np.stack([np.roll(coeffs, -2), np.roll(coeffs, -3)])
            cls.LUTs[bior_name] = torch.tensor(coeffs * scale).long()

    @classmethod
    def init_nexp(cls, lut_config, scale):
        # NEXP
        size = lut_config.config["exp"]["neg_lut_size"]
        full = np.exp(-np.linspace(1.0 / size, 1 / 1 << 4, size))
        cls.LUTs[lut_config.new_name("nexp", "low")] = torch.tensor(full * scale).long()
        full = np.exp(-np.linspace(1.0 * 1 << 4 / size, 1 << 4, size))
        cls.LUTs[lut_config.new_name("nexp", "high")] = torch.tensor(
            full * scale
        ).long()
        # NEXP-BIOR
        cls.generate_haar(
            lut_config.config["exp"]["lut_max_bits"],
            lut_config.config["exp"]["haar_size_bits"],
            lambda x: np.exp(-x),
            lut_config.new_name("nexp", "haar"),
        )
        # NEXP-BIOR
        cls.generate_bior(
            lut_config.config["exp"]["lut_max_bits"],
            lut_config.config["exp"]["bior_size_bits"],
            lambda x: np.exp(-x),
            lut_config.new_name("nexp", "bior"),
        )

    @classmethod
    def initialize_luts(cls, lut_config, device=None):
        r"""Initialize LUTs for different approximation functions:
        * exp: Exponential
        * log: Logarithm
        * reciprocal: Reciprocal
        * sqrt: Square root
        * inv_sqrt: Inverse square root
        * sin: Sine
        * cos: Cosine
        * sigmoid: Sigmoid
        * tanh: hyperbolic tangent function
        * erf: Error function
        * gelu: Gaussian Error Linear Units
        * silu: Sigmoid Linear Units
        """
        sigmoid = lambda x: 1 / (1 + np.exp(-x))
        relu = lambda x: x * (x > 0)

        """Exp LUT"""
        if lut_config.config["exp"]["method"] in (
            "haar",
            "bior",
            "haar-lut-only",
            "bior-lut-only",
        ):
            scale = 1 << cfg.encoder.precision_bits
            cls.init_exp(lut_config, scale)
            cls.init_nexp(lut_config, scale)

        """Logarithm LUT"""
        if lut_config.config["log"]["method"] in (
            "haar",
            "bior",
            "haar-lut-only",
            "bior-lut-only",
        ):
            cls.generate_haar(
                lut_config.config["log"]["lut_max_bits"],
                lut_config.config["log"]["haar_size_bits"],
                np.log,
                lut_config.new_name("log", "haar"),
            )
            cls.generate_bior(
                lut_config.config["log"]["lut_max_bits"],
                lut_config.config["log"]["bior_size_bits"],
                np.log,
                lut_config.new_name("log", "bior"),
            )

        """Reciprocal LUT"""
        if lut_config.config["reciprocal"]["method"] in (
            "haar",
            "bior",
            "haar-lut-only",
            "bior-lut-only",
        ):
            cls.generate_haar(
                lut_config.config["reciprocal"]["lut_max_bits"],
                lut_config.config["reciprocal"]["haar_size_bits"],
                np.reciprocal,
                lut_config.new_name("reciprocal", "haar"),
            )
            cls.generate_bior(
                lut_config.config["reciprocal"]["lut_max_bits"],
                lut_config.config["reciprocal"]["bior_size_bits"],
                np.reciprocal,
                lut_config.new_name("reciprocal", "bior"),
            )

        """Sqrt LUT"""
        if lut_config.config["sqrt"]["method"] in (
            "haar",
            "bior",
            "haar-lut-only",
            "bior-lut-only",
        ):
            cls.generate_haar(
                lut_config.config["sqrt"]["lut_max_bits"],
                lut_config.config["sqrt"]["haar_size_bits"],
                np.sqrt,
                lut_config.new_name("sqrt", "haar"),
            )
            cls.generate_bior(
                lut_config.config["sqrt"]["lut_max_bits"],
                lut_config.config["sqrt"]["bior_size_bits"],
                np.sqrt,
                lut_config.new_name("sqrt", "bior"),
            )

        """Inv Sqrt LUT"""
        if lut_config.config["inv_sqrt"]["method"] in (
            "haar",
            "bior",
            "haar-lut-only",
            "bior-lut-only",
            "tailored_haar",
        ):
            cls.generate_haar(
                lut_config.config["inv_sqrt"]["lut_max_bits"],
                lut_config.config["inv_sqrt"]["haar_size_bits"],
                lambda x: np.reciprocal(np.sqrt(x)),
                lut_config.new_name("inv_sqrt", "haar"),
            )
            cls.generate_haar(
                lut_config.config["inv_sqrt"]["tailored_0_lut_max_bits"],
                lut_config.config["inv_sqrt"]["tailored_0_haar_size_bits"],
                lambda x: np.reciprocal(np.sqrt(x)),
                lut_config.new_name("inv_sqrt", "tailored_haar_0"),
            )
            cls.generate_haar(
                lut_config.config["inv_sqrt"]["tailored_1_lut_max_bits"],
                lut_config.config["inv_sqrt"]["tailored_1_haar_size_bits"],
                lambda x: np.reciprocal(np.sqrt(x)),
                lut_config.new_name("inv_sqrt", "tailored_haar_1"),
            )
            cls.generate_bior(
                lut_config.config["inv_sqrt"]["lut_max_bits"],
                lut_config.config["inv_sqrt"]["bior_size_bits"],
                lambda x: np.reciprocal(np.sqrt(x)),
                lut_config.new_name("inv_sqrt", "bior"),
            )

        """Trigonometry LUTs: Sin, Cos"""
        if lut_config.config["trigonometry"]["method"] in (
            "haar",
            "bior",
            "haar-lut-only",
            "bior-lut-only",
        ):
            # sin
            cls.generate_haar(
                0,
                lut_config.config["trigonometry"]["haar_size_bits"],
                lambda x: np.sin(x * np.pi * 2),
                lut_config.new_name("sin", "haar"),
            )
            cls.generate_bior(
                0,
                lut_config.config["trigonometry"]["bior_size_bits"],
                lambda x: np.sin(x * np.pi * 2),
                lut_config.new_name("sin", "bior"),
            )
            cls.generate_haar(
                lut_config.config["trigonometry"]["lut_max_bits"],
                lut_config.config["trigonometry"]["haar_size_bits"],
                lambda x: np.sin(x * np.pi * 2),
                lut_config.new_name("sin", "haar_lut_only"),
                negative_values=True,
            )
            cls.generate_bior(
                lut_config.config["trigonometry"]["lut_max_bits"],
                lut_config.config["trigonometry"]["bior_size_bits"],
                lambda x: np.sin(x * np.pi * 2),
                lut_config.new_name("sin", "bior_lut_only"),
                negative_values=True,
            )
            # cos
            cls.generate_haar(
                0,
                lut_config.config["trigonometry"]["haar_size_bits"],
                lambda x: np.cos(x * np.pi * 2),
                lut_config.new_name("cos", "haar"),
            )
            cls.generate_bior(
                0,
                lut_config.config["trigonometry"]["bior_size_bits"],
                lambda x: np.cos(x * np.pi * 2),
                lut_config.new_name("cos", "bior"),
            )
            cls.generate_haar(
                lut_config.config["trigonometry"]["lut_max_bits"],
                lut_config.config["trigonometry"]["haar_size_bits"],
                lambda x: np.cos(x * np.pi * 2),
                lut_config.new_name("cos", "haar_lut_only"),
                negative_values=True,
            )
            cls.generate_bior(
                lut_config.config["trigonometry"]["lut_max_bits"],
                lut_config.config["trigonometry"]["bior_size_bits"],
                lambda x: np.cos(x * np.pi * 2),
                lut_config.new_name("cos", "bior_lut_only"),
                negative_values=True,
            )

        """Sigmoid & Tanh LUT"""
        if lut_config.config["sigmoid_tanh"]["method"] in (
            "haar",
            "bior",
            "haar-lut-only",
            "bior-lut-only",
        ):
            # Sigmoid
            cls.generate_haar(
                lut_config.config["sigmoid_tanh"]["sigmoid_lut_max_bits"],
                lut_config.config["sigmoid_tanh"]["haar_size_bits"],
                sigmoid,
                lut_config.new_name("sigmoid", "haar"),
            )
            cls.generate_bior(
                lut_config.config["sigmoid_tanh"]["sigmoid_lut_max_bits"],
                lut_config.config["sigmoid_tanh"]["bior_size_bits"],
                sigmoid,
                lut_config.new_name("sigmoid", "bior"),
            )
            cls.generate_haar(
                lut_config.config["sigmoid_tanh"]["sigmoid_lut_max_bits"],
                lut_config.config["sigmoid_tanh"]["haar_size_bits"],
                sigmoid,
                lut_config.new_name("sigmoid", "haar_lut_only"),
                negative_values=True,
            )
            cls.generate_bior(
                lut_config.config["sigmoid_tanh"]["sigmoid_lut_max_bits"],
                lut_config.config["sigmoid_tanh"]["bior_size_bits"],
                sigmoid,
                lut_config.new_name("sigmoid", "bior_lut_only"),
                negative_values=True,
            )
            # Tanh
            cls.generate_haar(
                lut_config.config["sigmoid_tanh"]["tanh_lut_max_bits"],
                lut_config.config["sigmoid_tanh"]["haar_size_bits"],
                np.tanh,
                lut_config.new_name("tanh", "haar"),
            )
            cls.generate_bior(
                lut_config.config["sigmoid_tanh"]["tanh_lut_max_bits"],
                lut_config.config["sigmoid_tanh"]["bior_size_bits"],
                np.tanh,
                lut_config.new_name("tanh", "bior"),
            )
            cls.generate_haar(
                lut_config.config["sigmoid_tanh"]["sigmoid_lut_max_bits"],
                lut_config.config["sigmoid_tanh"]["haar_size_bits"],
                np.tanh,
                lut_config.new_name("tanh", "haar_lut_only"),
                negative_values=True,
            )
            cls.generate_bior(
                lut_config.config["sigmoid_tanh"]["sigmoid_lut_max_bits"],
                lut_config.config["sigmoid_tanh"]["bior_size_bits"],
                np.tanh,
                lut_config.new_name("tanh", "bior_lut_only"),
                negative_values=True,
            )

        """Erf LUT"""
        if lut_config.config["erf"]["method"] in (
            "haar",
            "bior",
            "haar-lut-only",
            "bior-lut-only",
        ):
            cls.generate_haar(
                lut_config.config["erf"]["lut_max_bits"],
                lut_config.config["erf"]["haar_size_bits"],
                lambda x: np.array([math.erf(x_) for x_ in x]),
                lut_config.new_name("erf", "haar"),
            )
            cls.generate_bior(
                lut_config.config["erf"]["lut_max_bits"],
                lut_config.config["erf"]["bior_size_bits"],
                lambda x: np.array([math.erf(x_) for x_ in x]),
                lut_config.new_name("erf", "bior"),
            )
            cls.generate_haar(
                lut_config.config["erf"]["lut_max_bits"],
                lut_config.config["erf"]["haar_size_bits"],
                lambda x: np.array([math.erf(x_) for x_ in x]),
                lut_config.new_name("erf", "haar_lut_only"),
                negative_values=True,
            )
            cls.generate_bior(
                lut_config.config["erf"]["lut_max_bits"],
                lut_config.config["erf"]["bior_size_bits"],
                lambda x: np.array([math.erf(x_) for x_ in x]),
                lut_config.new_name("erf", "bior_lut_only"),
                negative_values=True,
            )

        """Gelu LUT"""
        if lut_config.config["gelu"]["method"] in (
            "haar",
            "bior",
            "haar-lut-only",
            "bior-lut-only",
        ):
            gelu = (
                lambda x: x
                * (1 + np.array([math.erf(x_ / math.sqrt(2)) for x_ in x]))
                / 2
            )
            cls.generate_haar(
                lut_config.config["gelu"]["lut_max_bits"],
                lut_config.config["gelu"]["haar_size_bits"],
                lambda x: relu(x) - gelu(x),
                lut_config.new_name("gelu", "haar"),
            )
            cls.generate_bior(
                lut_config.config["gelu"]["lut_max_bits"],
                lut_config.config["gelu"]["bior_size_bits"],
                lambda x: relu(x) - gelu(x),
                lut_config.new_name("gelu", "bior"),
            )
            cls.generate_haar(
                lut_config.config["gelu"]["lut_max_bits"],
                lut_config.config["gelu"]["haar_size_bits"],
                lambda x: gelu(x),
                lut_config.new_name("gelu", "haar_lut_only"),
                negative_values=True,
            )
            cls.generate_bior(
                lut_config.config["gelu"]["lut_max_bits"],
                lut_config.config["gelu"]["bior_size_bits"],
                lambda x: gelu(x),
                lut_config.new_name("gelu", "bior_lut_only"),
                negative_values=True,
            )

        """Silu LUT"""
        if lut_config.config["silu"]["method"] in (
            "haar",
            "bior",
            "haar-lut-only",
            "bior-lut-only",
        ):
            silu = lambda x: x * sigmoid(x)
            cls.generate_haar(
                lut_config.config["silu"]["lut_max_bits"],
                lut_config.config["silu"]["haar_size_bits"],
                lambda x: relu(x) - silu(x),
                lut_config.new_name("silu", "haar"),
            )
            cls.generate_bior(
                lut_config.config["silu"]["lut_max_bits"],
                lut_config.config["silu"]["bior_size_bits"],
                lambda x: relu(x) - silu(x),
                lut_config.new_name("silu", "bior"),
            )
            cls.generate_haar(
                lut_config.config["silu"]["lut_max_bits"],
                lut_config.config["silu"]["haar_size_bits"],
                lambda x: silu(x),
                lut_config.new_name("silu", "haar_lut_only"),
                negative_values=True,
            )
            cls.generate_bior(
                lut_config.config["silu"]["lut_max_bits"],
                lut_config.config["silu"]["bior_size_bits"],
                lambda x: silu(x),
                lut_config.new_name("silu", "bior_lut_only"),
                negative_values=True,
            )

        cls.move_device(device)

    @classmethod
    def move_device(cls, device=None):
        if device is None:
            device = "cpu"
        else:
            device = str(device)
        if "cuda" in device:
            for lut in cls.LUTs:
                cls.LUTs[lut] = CUDALongTensor(cls.LUTs[lut], device=device)
        else:
            for lut in cls.LUTs:
                cls.LUTs[lut] = cls.LUTs[lut].to(device)
        logging.debug(f"[Device] LUTs initialized for {device}\n")
