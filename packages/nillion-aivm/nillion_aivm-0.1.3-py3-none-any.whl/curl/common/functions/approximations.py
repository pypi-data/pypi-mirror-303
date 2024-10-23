#!/usr/bin/env python3

# Copyright (c) Facebook, Inc. and its affiliates.
#
# This source code is licensed under the MIT license found in the
# LICENSE file in the root directory of this source tree.

import logging
import math

import curl
import numpy as np
import pywt
import torch
from curl.common.functions.lut import LookupTables
from curl.config import cfg
from curl.cuda import CUDALongTensor

__all__ = [
    "exp",
    "log",
    "reciprocal",
    "inv_sqrt",
    "sqrt",
    "_eix",
    "cossin",
    "cos",
    "sin",
    "sigmoid",
    "tanh",
    "erf",
    "gelu",
    "silu",
    "softmax",
    "log_softmax",
]


def _nexp_lut(self, method):
    r"""Approximates the negative exponential function using a limit approximation"""
    luts = LookupTables()
    lut_config = luts.get_config()
    precision = 1 << cfg.encoder.precision_bits
    size = lut_config.config["exp"]["neg_lut_size"]

    if method == "split":
        x = self.div(precision / 1 << 4 / size)
        d = x < 1
        bits = x.encoder._precision_bits
        x.encoder._precision_bits = 0
        c = d * x + (1 - d) * (precision - 1)
        x.encoder._precision_bits = bits
        c0 = c  # c0 = c.mod(size)
        c1 = c.div(size)
        t0 = c0.evaluate_lut("nexp", "low")
        t1 = c1.evaluate_lut("nexp", "high")
        return t0 * t1
    elif method == "haar":
        check = self < 1 << lut_config.config["exp"]["lut_max_bits"]
        truncation = (
            lut_config.config["exp"]["lut_max_bits"]
            + cfg.encoder.precision_bits
            - lut_config.config["exp"]["bior_size_bits"]
        )
        if cfg.encoder.trunc_method.lut == "crypten":
            msb = self.div(1 << truncation)
        else:
            msb = self.egk_trunc_pr(62, truncation)  # 62 is used because 63 overflows
        lut = msb.evaluate_lut("nexp", "haar")
        return check * lut
    elif method == "bior":
        check = self < 1 << lut_config.config["exp"]["lut_max_bits"]
        truncation = (
            lut_config.config["exp"]["lut_max_bits"]
            + cfg.encoder.precision_bits
            - lut_config.config["exp"]["bior_size_bits"]
        )
        if cfg.encoder.trunc_method.lut == "crypten":
            msb, lsb = self.divmod(1 << truncation)
        else:
            msb, lsb = self.egk_truncmod_pr(
                62, truncation
            )  # 62 is used because 63 overflows
        lut = msb.evaluate_bior_lut("nexp", "bior", lsb, truncation)
        return check * lut
    else:
        raise ValueError(f"Invalid method {method} given for nexp function")


# Iterative methods:
def exp(self):
    r"""Approximates the exponential function using a limit approximation:

    .. math::

        exp(x) = \lim_{n \\rightarrow \\infty} (1 + x / n) ^ n

    Here we compute exp by choosing n = 2 ** d for some large d equal to
    `iterations`. We then compute (1 + x / n) once and square `d` times.

    Set the number of iterations for the limit approximation with
    config.exp_iterations.
    """  # noqa: W605
    luts = LookupTables()
    lut_config = luts.get_config()
    method = lut_config.config["exp"]["method"]

    if method in ("split", "haar", "bior"):
        if lut_config.config["exp"]["all_neg"]:
            return _nexp_lut(-self, method)
        if method == "haar":
            truncation = (
                lut_config.config["exp"]["lut_max_bits"]
                + cfg.encoder.precision_bits
                - lut_config.config["exp"]["haar_size_bits"]
            )
            if cfg.encoder.trunc_method.lut == "crypten":
                msb = self.div(1 << truncation)
            else:
                msb = self.egk_trunc_pr(62, truncation)
            return msb.evaluate_lut("exp", "haar")
        elif method == "bior":
            truncation = (
                lut_config.config["exp"]["lut_max_bits"]
                + cfg.encoder.precision_bits
                - lut_config.config["exp"]["bior_size_bits"]
            )
            if cfg.encoder.trunc_method.lut == "crypten":
                msb, lsb = self.divmod(1 << truncation)
            else:
                msb, lsb = self.egk_truncmod_pr(62, truncation)
            return msb.evaluate_bior_lut("exp", "bior", lsb, truncation)
    elif method == "limit":
        iters = lut_config.config["exp"]["iterations"]
        result = 1 + self.div(1 << iters)
        for _ in range(iters):
            result = result.square()
        return result
    else:
        raise ValueError(f"Invalid method {method} given for exp function")


def log(self, input_in_01=False, use_lut=False):
    r"""
    Approximates the natural logarithm using 8th order modified
    Householder iterations. This approximation is accurate within 2% relative
    error on [0.0001, 250].

    Iterations are computed by: :math:`h = 1 - x * exp(-y_n)`

    .. math::

        y_{n+1} = y_n - \sum_k^{order}\frac{h^k}{k}

    Args:
        input_in_01 (bool) : Allows a user to indicate that the input is in the domain [0, 1],
            causing the function optimize for this domain. This is useful for computing
            log-probabilities for entropy functions.

            We shift the domain of convergence by a constant :math:`a` using the following identity:

            .. math::

                \ln{u} = \ln {au} - \ln{a}

            Since the domain of convergence for CrypTen's log() function is approximately [1e-4, 1e2],
            we can set :math:`a=100`.

    Configuration parameters:
        iterations (int): number of Householder iterations for the approximation
        exp_iterations (int): number of iterations for limit approximation of exp
        order (int): number of polynomial terms used (order of Householder approx)
    """
    if input_in_01:
        return log(self.mul(100)) - 4.605170

    luts = LookupTables()
    lut_config = luts.get_config()

    # Initialization to a decent estimate (found by qualitative inspection):
    #                ln(x) = x/120 - 20exp(-2x - 1.0) + 3.0
    iterations = lut_config.config["log"]["iterations"]
    exp_iterations = lut_config.config["log"]["exp_iterations"]
    order = lut_config.config["log"]["order"]
    method = lut_config.config["log"]["method"]

    if method in ("haar", "bior"):
        luts = LookupTables()
        if method == "haar":
            log_truncation = (
                lut_config.config["log"]["lut_max_bits"]
                + cfg.encoder.precision_bits
                - lut_config.config["log"]["haar_size_bits"]
            )
            if cfg.encoder.trunc_method.lut == "crypten":
                msb = self.div(1 << log_truncation)
            else:
                msb = self.egk_trunc_pr(62, log_truncation)
            return msb.evaluate_lut("log", "haar")
        elif method == "bior":
            log_total_bits = (
                lut_config.config["log"]["lut_max_bits"] + cfg.encoder.precision_bits
            )
            log_truncation = log_total_bits - lut_config.config["log"]["bior_size_bits"]
            if cfg.encoder.trunc_method.lut == "crypten":
                msb, lsb = self.divmod(1 << log_truncation)
            else:
                msb, lsb = self.egk_truncmod_pr(62, log_truncation)
            return msb.evaluate_bior_lut("log", "bior", lsb, log_truncation)
    elif method == "iter":
        term1 = self.div(120)
        term2 = exp(self.mul(2).add(1.0).neg()).mul(20)
        y = term1 - term2 + 3.0

        # 8th order Householder iterations
        with lut_config.temp_override({"exp": {"iterations": exp_iterations}}):
            for _ in range(iterations):
                h = 1 - self * exp(-y)
                y -= h.polynomial([1 / (i + 1) for i in range(order)])
        return y
    else:
        raise ValueError(f"Invalid method {method} given for log function")


def reciprocal(self, input_in_01=False):
    r"""
    Args:
        input_in_01 (bool) : Allows a user to indicate that the input is in the range [0, 1],
                    causing the function optimize for this range. This is useful for improving
                    the accuracy of functions on probabilities (e.g. entropy functions).

    Methods:
        'NR' : `Newton-Raphson`_ method computes the reciprocal using iterations
                of :math:`x_{i+1} = (2x_i - self * x_i^2)` and uses
                :math:`3*exp(1 - 2x) + 0.003` as an initial guess by default

        'log' : Computes the reciprocal of the input from the observation that:
                :math:`x^{-1} = exp(-log(x))`

    Configuration params:
        reciprocal_method (str):  One of 'NR' or 'log' or 'lut'.
        reciprocal_nr_iters (int):  determines the number of Newton-Raphson iterations to run
                        for the `NR` method
        reciprocal_log_iters (int): determines the number of Householder
            iterations to run when computing logarithms for the `log` method
        reciprocal_all_pos (bool): determines whether all elements of the
            input are known to be positive, which optimizes the step of
            computing the sign of the input.
        reciprocal_initial (tensor): sets the initial value for the
            Newton-Raphson method. By default, this will be set to :math:
            `3*exp(-(x-.5)) + 0.003` as this allows the method to converge over
            a fairly large domain

    .. _Newton-Raphson:
        https://en.wikipedia.org/wiki/Newton%27s_method
    """
    luts = LookupTables()
    lut_config = luts.get_config()
    pos_override = {"reciprocal": {"all_pos": True}}
    if input_in_01:
        with lut_config.temp_override(pos_override):
            rec = reciprocal(self.mul(64)).mul(64)
        return rec

    # Get config options
    method = lut_config.config["reciprocal"]["method"]
    all_pos = lut_config.config["reciprocal"]["all_pos"]
    initial = lut_config.config["reciprocal"]["initial"]

    if not all_pos:
        sgn = self.sign()
        pos = sgn * self
        with lut_config.temp_override(pos_override):
            return sgn * reciprocal(pos)

    if method in ("haar", "bior"):
        if method == "haar":
            reciprocal_truncation = (
                lut_config.config["reciprocal"]["lut_max_bits"]
                + cfg.encoder.precision_bits
                - lut_config.config["reciprocal"]["haar_size_bits"]
            )
            if cfg.encoder.trunc_method.lut == "crypten":
                msb = self.div(1 << reciprocal_truncation)
            else:
                msb = self.egk_trunc_pr(62, reciprocal_truncation)
            return msb.evaluate_lut("reciprocal", "haar")
        elif method == "bior":
            reciprocal_truncation = (
                lut_config.config["reciprocal"]["lut_max_bits"]
                + cfg.encoder.precision_bits
                - lut_config.config["reciprocal"]["bior_size_bits"]
            )
            if cfg.encoder.trunc_method.lut == "crypten":
                msb, lsb = self.divmod(1 << reciprocal_truncation)
            else:
                msb, lsb = self.egk_truncmod_pr(62, reciprocal_truncation)
            return msb.evaluate_bior_lut(
                "reciprocal",
                "bior",
                lsb,
                reciprocal_truncation,
            )
    elif method == "NR":
        nr_iters = lut_config.config["reciprocal"]["nr_iters"]
        if initial is None:
            # Initialization to a decent estimate (found by qualitative inspection):
            #                1/x = 3exp(1 - 2x) + 0.003
            result = 3 * (1 - 2 * self).exp() + 0.003
        else:
            result = initial
        for _ in range(nr_iters):
            if hasattr(result, "square"):
                result += result - result.square().mul_(self)
            else:
                result = 2 * result - result * result * self
        return result
    elif method == "log":
        log_iters = lut_config.config["reciprocal"]["log_iters"]
        with lut_config.temp_override({"reciprocal": {"log_iters": log_iters}}):
            return exp(-log(self))
    else:
        raise ValueError(f"Invalid method {method} given for reciprocal function")


def inv_sqrt(self):
    r"""
    Computes the inverse square root of the input using the Newton-Raphson method.

    Configuration params:
        sqrt_nr_iters (int):  determines the number of Newton-Raphson iterations to run.
        sqrt_nr_initial (tensor): sets the initial value for the Newton-Raphson iterations.
                    By default, this will be set to allow the method to converge over a
                    fairly large domain.

    .. _Newton-Raphson:
        https://en.wikipedia.org/wiki/Fast_inverse_square_root#Newton's_method
    """
    luts = LookupTables()
    lut_config = luts.get_config()

    initial = lut_config.config["sqrt"]["nr_initial"]
    iters = lut_config.config["sqrt"]["nr_iters"]
    method = lut_config.config["inv_sqrt"]["method"]

    if method in ("haar", "bior", "tailored_haar"):
        if method == "haar":
            truncation = (
                lut_config.config["inv_sqrt"]["lut_max_bits"]
                + cfg.encoder.precision_bits
                - lut_config.config["inv_sqrt"]["haar_size_bits"]
            )
            if cfg.encoder.trunc_method.lut == "crypten":
                msb = self.div(1 << truncation)
            else:
                msb = self.egk_trunc_pr(62, truncation)
            return msb.evaluate_lut("inv_sqrt", "haar")
        elif method == "bior":
            truncation = (
                lut_config.config["inv_sqrt"]["lut_max_bits"]
                + cfg.encoder.precision_bits
                - lut_config.config["inv_sqrt"]["bior_size_bits"]
            )
            if cfg.encoder.trunc_method.lut == "crypten":
                msb, lsb = self.divmod(1 << truncation)
            else:
                msb, lsb = self.egk_truncmod_pr(62, truncation)
            return msb.evaluate_bior_lut("inv_sqrt", "bior", lsb, truncation)
        elif method == "tailored_haar":
            truncation_0 = (
                lut_config.config["inv_sqrt"]["tailored_0_lut_max_bits"]
                + cfg.encoder.precision_bits
                - lut_config.config["inv_sqrt"]["tailored_0_haar_size_bits"]
            )
            truncation_1 = (
                lut_config.config["inv_sqrt"]["tailored_1_lut_max_bits"]
                + cfg.encoder.precision_bits
                - lut_config.config["inv_sqrt"]["tailored_1_haar_size_bits"]
            )
            if cfg.encoder.trunc_method.lut == "crypten":
                msb_0 = self.div(1 << truncation_0)
                msb_1 = self.div(1 << truncation_1)
            else:
                msb_0 = self.egk_trunc_pr(62, truncation_0)
                msb_1 = self.egk_trunc_pr(62, truncation_1)
            y_0 = msb_0.evaluate_lut("inv_sqrt", "tailored_haar_0")
            y_1 = msb_1.evaluate_lut("inv_sqrt", "tailored_haar_1")
            b = self < 1
            return b * y_0 + (1 - b) * y_1
    elif method == "NR":
        # Initialize using decent approximation
        if initial is None:
            y = exp(self.div(2).add(0.2).neg()).mul(2.2).add(0.2)
            y -= self.div(1024)
        else:
            y = initial

        # Newton Raphson iterations for inverse square root
        for _ in range(iters):
            y = y.mul_(3 - self * y.square()).div_(2)
        return y
    else:
        raise ValueError(f"Invalid method {method} given for inv_sqrt function")


def sqrt(self):
    r"""
    Computes the square root of the input by computing its inverse square root using
    the Newton-Raphson method and multiplying by the input.

    Configuration params:
        sqrt_nr_iters (int):  determines the number of Newton-Raphson iterations to run
        sqrt_initial (tensor): sets the initial value for the inverse square root
            Newton-Raphson iterations. By default, this will be set to allow convergence
            over a fairly large domain.

    .. _Newton-Raphson:
        https://en.wikipedia.org/wiki/Fast_inverse_square_root#Newton's_method
    """
    luts = LookupTables()
    lut_config = luts.get_config()
    method = lut_config.config["sqrt"]["method"]

    if method in ("haar", "bior"):
        if method == "haar":
            truncation = (
                lut_config.config["sqrt"]["lut_max_bits"]
                + cfg.encoder.precision_bits
                - lut_config.config["sqrt"]["haar_size_bits"]
            )
            if cfg.encoder.trunc_method.lut == "crypten":
                msb = self.div(1 << truncation)
            else:
                msb = self.egk_trunc_pr(62, truncation)
            return msb.evaluate_lut("sqrt", "haar")
        elif method == "bior":
            truncation = (
                lut_config.config["sqrt"]["lut_max_bits"]
                + cfg.encoder.precision_bits
                - lut_config.config["sqrt"]["bior_size_bits"]
            )
            if cfg.encoder.trunc_method.lut == "crypten":
                msb, lsb = self.divmod(1 << truncation)
            else:
                msb, lsb = self.egk_truncmod_pr(62, truncation)
            return msb.evaluate_bior_lut("sqrt", "bior", lsb, truncation)
    elif method == "NR":
        return inv_sqrt(self).mul_(self)
    else:
        raise ValueError(f"Invalid method {method} given for sqrt function")


def _eix(self):
    r"""Computes e^(i * self) where i is the imaginary unit.
    Returns (Re{e^(i * self)}, Im{e^(i * self)} = cos(self), sin(self)
    """
    luts = LookupTables()
    lut_config = luts.get_config()
    iterations = lut_config["trigonometry"]["iterations"]

    re = 1
    im = self.div(1 << iterations)

    # First iteration uses knowledge that `re` is public and = 1
    re -= im.square()
    im *= 2

    # Compute (a + bi)^2 -> (a^2 - b^2) + (2ab)i `iterations` times
    for _ in range(iterations - 1):
        a2 = re.square()
        b2 = im.square()
        im = im.mul_(re)
        im._tensor *= 2
        re = a2 - b2

    return re, im


def cossin(self):
    r"""Computes cosine and sine of input via exp(i * x).

    Args:
        iterations (int): for approximating exp(i * x)
    """

    luts = LookupTables()
    lut_config = luts.get_config()

    method = lut_config.config["trigonometry"]["method"]
    if method in ("haar", "bior"):
        sgn = self.sign()
        self = sgn * self
        self = self * (1.0 / (2 * np.pi))
        self = self.mod(1 << cfg.encoder.precision_bits)
        if method == "haar":
            trig_truncation = (
                cfg.encoder.precision_bits
                - lut_config.config["trigonometry"]["haar_size_bits"]
            )
            if cfg.encoder.trunc_method.lut == "crypten":
                msb = self.div(1 << trig_truncation)
            else:
                msb = self.egk_trunc_pr(62, trig_truncation)
            cos = msb.evaluate_lut("cos", "haar")
            sin = msb.evaluate_lut("sin", "haar")
        elif method == "bior":
            trig_truncation = (
                cfg.encoder.precision_bits
                - lut_config.config["trigonometry"]["bior_size_bits"]
            )
            if cfg.encoder.trunc_method.lut == "crypten":
                msb, lsb = self.divmod(1 << trig_truncation)
            else:
                msb, lsb = self.egk_truncmod_pr(62, trig_truncation)
            cos = msb.evaluate_bior_lut("cos", "bior", lsb, trig_truncation)
            sin = msb.evaluate_bior_lut("sin", "bior", lsb, trig_truncation)
        sin = sgn * sin
        return cos, sin
    elif method in ("haar-lut-only", "bior-lut-only"):  # using only LUT
        luts = LookupTables()
        self = self + 2 ** (lut_config.config["trigonometry"]["lut_max_bits"])
        if method == "haar-lut-only":
            truncation = (
                lut_config.config["trigonometry"]["lut_max_bits"]
                + cfg.encoder.precision_bits
                - lut_config.config["trigonometry"]["haar_size_bits"]
            )
            if cfg.encoder.trunc_method.lut == "crypten":
                msb = self.div(1 << truncation)
            else:
                msb = self.egk_trunc_pr(62, truncation)
            cos = msb.evaluate_lut("cos", "haar_lut_only")
            sin = msb.evaluate_lut("sin", "haar_lut_only")
            return cos, sin
        elif method == "bior-lut-only":
            total_bits = (
                lut_config.config["trigonometry"]["lut_max_bits"]
                + cfg.encoder.precision_bits
            )
            truncation = (
                total_bits - lut_config.config["trigonometry"]["bior_size_bits"]
            )
            if cfg.encoder.trunc_method.lut == "crypten":
                msb, lsb = self.divmod(1 << truncation)
            else:
                msb, lsb = self.egk_truncmod_pr(62, truncation)
            cos = msb.evaluate_bior_lut("cos", "bior_lut_only", lsb, truncation)
            # CHECK: The line below was originally "cos_bior_lut_only" but it was changed to "sin_bior_lut_only"
            sin = msb.evaluate_bior_lut("sin", "bior_lut_only", lsb, truncation)
            return cos, sin
    elif method == "NR":
        return self._eix()
    else:
        raise ValueError(f"Invalid method {method} given for cossin function")


def cos(self):
    r"""Computes the cosine of the input using cos(x) = Re{exp(i * x)}

    Args:
        iterations (int): for approximating exp(i * x)
    """
    return cossin(self)[0]


def sin(self):
    r"""Computes the sine of the input using sin(x) = Im{exp(i * x)}

    Args:
        iterations (int): for approximating exp(i * x)
    """
    return cossin(self)[1]


# Logistic Functions
def sigmoid(self):
    r"""Computes the sigmoid function using the following definition

    .. math::
        \sigma(x) = (1 + e^{-x})^{-1}

    If a valid method is given, this function will compute sigmoid
        using that method:

    "chebyshev" - computes tanh via Chebyshev approximation with
        truncation and uses the identity:

    .. math::
        \sigma(x) = \frac{1}{2}tanh(\frac{x}{2}) + \frac{1}{2}

    "reciprocal" - computes sigmoid using :math:`1 + e^{-x}` and computing
        the reciprocal

    """  # noqa: W605
    luts = LookupTables()
    lut_config = luts.get_config()
    method = lut_config.config["sigmoid_tanh"]["method"]

    if method in ("haar", "bior"):
        ltz = self._ltz()
        sgn = 1 - 2 * ltz
        abs = sgn * self
        if method == "haar":
            st_truncation = (
                lut_config["sigmoid_tanh"]["sigmoid_lut_max_bits"]
                + cfg.encoder.precision_bits
                - lut_config.config["sigmoid_tanh"]["haar_size_bits"]
            )
            if cfg.encoder.trunc_method.lut == "crypten":
                msb = abs.div(1 << st_truncation)
            else:
                msb = abs.egk_trunc_pr(62, st_truncation)
            lut = msb.evaluate_lut("sigmoid", "haar")
        elif method == "bior":
            st_truncation = (
                lut_config["sigmoid_tanh"]["sigmoid_lut_max_bits"]
                + cfg.encoder.precision_bits
                - lut_config.config["sigmoid_tanh"]["bior_size_bits"]
            )
            if cfg.encoder.trunc_method.lut == "crypten":
                msb, lsb = abs.divmod(1 << st_truncation)
            else:
                msb, lsb = abs.egk_truncmod_pr(62, st_truncation)
            lut = msb.evaluate_bior_lut("sigmoid", "bior", lsb, st_truncation)
        eval = ltz + sgn * lut
        limit = 1 - ltz
        check = abs < 1 << lut_config["sigmoid_tanh"]["sigmoid_lut_max_bits"] - 1
        return limit + check * (eval - limit)

    elif method in ("haar-lut-only", "bior-lut-only"):  # using only LUT
        self = self + 2 ** (lut_config["sigmoid_tanh"]["sigmoid_lut_max_bits"])
        if method == "haar-lut-only":
            truncation = (
                lut_config["sigmoid_tanh"]["sigmoid_lut_max_bits"]
                + cfg.encoder.precision_bits
                - lut_config.config["sigmoid_tanh"]["haar_size_bits"]
            )
            if cfg.encoder.trunc_method.lut == "crypten":
                msb = self.div(1 << truncation)
            else:
                msb = self.egk_trunc_pr(62, truncation)
            return msb.evaluate_lut("sigmoid", "haar_lut_only")
        elif method == "bior-lut-only":
            total_bits = (
                lut_config["sigmoid_tanh"]["sigmoid_lut_max_bits"]
                + cfg.encoder.precision_bits
            )
            truncation = (
                total_bits - lut_config.config["sigmoid_tanh"]["bior_size_bits"]
            )
            if cfg.encoder.trunc_method.lut == "crypten":
                msb, lsb = self.divmod(1 << truncation)
            else:
                msb, lsb = self.egk_truncmod_pr(62, truncation)
            return msb.evaluate_bior_lut(
                "sigmoid",
                "bior_lut_only",
                lsb,
                truncation,
            )
    elif method == "chebyshev":
        tanh_approx = tanh(self.div(2))
        return tanh_approx.div(2) + 0.5
    elif method == "reciprocal":
        ltz = self._ltz()
        sgn = 1 - 2 * ltz

        pos_input = self.mul(sgn)
        denominator = pos_input.neg().exp().add(1)

        # TODO: Set these with configurable parameters
        with lut_config.temp_override(
            {
                "exp": {"iterations": 9},
                "reciprocal": {"nr_iters": 3, "all_pos": True, "initial": 0.75},
            }
        ):
            pos_output = denominator.reciprocal()

        result = pos_output.where(1 - ltz, 1 - pos_output)
        # TODO: Support addition with different encoder scales
        # result = pos_output + ltz - 2 * pos_output * ltz
        return result
    else:
        raise ValueError(f"Unrecognized method {method} for sigmoid")


def tanh(self):
    r"""Computes the hyperbolic tangent function using the identity

    .. math::
        tanh(x) = 2\sigma(2x) - 1

    If a valid method is given, this function will compute tanh using that method:

    "chebyshev" - computes tanh via Chebyshev approximation with truncation.

    .. math::
        tanh(x) = \sum_{j=1}^terms c_{2j - 1} P_{2j - 1} (x / maxval)

    where c_i is the ith Chebyshev series coefficient and P_i is ith polynomial.
    The approximation is truncated to +/-1 outside [-1, 1].

    Args:
        terms (int): highest degree of Chebyshev polynomials.
                        Must be even and at least 6.
    """
    luts = LookupTables()
    lut_config = luts.get_config()

    method = lut_config.config["sigmoid_tanh"]["method"]

    if method in ("haar", "bior"):
        sgn = self.sign()
        abs = sgn * self
        if method == "haar":
            st_truncation = (
                lut_config["sigmoid_tanh"]["tanh_lut_max_bits"]
                + cfg.encoder.precision_bits
                - lut_config.config["sigmoid_tanh"]["haar_size_bits"]
            )
            if cfg.encoder.trunc_method.lut == "crypten":
                msb = abs.div(1 << st_truncation)
            else:
                msb = abs.egk_trunc_pr(62, st_truncation)
            lut = msb.evaluate_lut("tanh", "haar")
        elif method == "bior":
            st_truncation = (
                lut_config["sigmoid_tanh"]["tanh_lut_max_bits"]
                + cfg.encoder.precision_bits
                - lut_config.config["sigmoid_tanh"]["bior_size_bits"]
            )
            if cfg.encoder.trunc_method.lut == "crypten":
                msb, lsb = abs.divmod(1 << st_truncation)
            else:
                msb, lsb = abs.egk_truncmod_pr(62, st_truncation)
            lut = msb.evaluate_bior_lut("tanh", "bior", lsb, st_truncation)
        check = abs < 1 << lut_config["sigmoid_tanh"]["tanh_lut_max_bits"] - 1
        return sgn * (1 - check + lut * check)
    elif method in ("haar-lut-only", "bior-lut-only"):  # using only LUT
        luts = LookupTables()
        self = self + 2 ** (lut_config["sigmoid_tanh"]["tanh_lut_max_bits"])
        if method == "haar-lut-only":
            truncation = (
                lut_config["sigmoid_tanh"]["tanh_lut_max_bits"]
                + cfg.encoder.precision_bits
                - lut_config.config["sigmoid_tanh"]["haar_size_bits"]
            )
            if cfg.encoder.trunc_method.lut == "crypten":
                msb = self.div(1 << truncation)
            else:
                msb = self.egk_trunc_pr(62, truncation)
            return msb.evaluate_lut("tanh", "haar_lut_only")
        elif method == "bior-lut-only":
            total_bits = (
                lut_config["sigmoid_tanh"]["tanh_lut_max_bits"]
                + cfg.encoder.precision_bits
            )
            truncation = (
                total_bits - lut_config.config["sigmoid_tanh"]["bior_size_bits"]
            )
            if cfg.encoder.trunc_method.lut == "crypten":
                msb, lsb = self.divmod(1 << truncation)
            else:
                msb, lsb = self.egk_truncmod_pr(62, truncation)
            return msb.evaluate_bior_lut("tanh", "bior_lut_only", lsb, truncation)
    elif method == "reciprocal":
        return self.mul(2).sigmoid().mul(2).sub(1)
    elif method == "chebyshev":
        terms = lut_config.config["sigmoid_tanh"]["terms"]
        coeffs = curl.common.util.chebyshev_series(torch.tanh, 1, terms)[1::2]
        tanh_polys = _chebyshev_polynomials(self, terms)
        tanh_polys_flipped = (
            tanh_polys.unsqueeze(dim=-1).transpose(0, -1).squeeze(dim=0)
        )
        out = tanh_polys_flipped.matmul(coeffs)

        # truncate outside [-maxval, maxval]
        return out.hardtanh()
    else:
        raise ValueError(f"Unrecognized method {method} for tanh")


def _chebyshev_polynomials(self, terms):
    r"""Evaluates odd degree Chebyshev polynomials at x

    Chebyshev Polynomials of the first kind are defined as

    .. math::
        P_0(x) = 1, P_1(x) = x, P_n(x) = 2 P_{n - 1}(x) - P_{n-2}(x)

    Args:
        self (MPCTensor): input at which polynomials are evaluated
        terms (int): highest degree of Chebyshev polynomials.
                        Must be even and at least 6.
    Returns:
        MPCTensor of polynomials evaluated at self of shape `(terms, *self)`
    """
    if terms % 2 != 0 or terms < 6:
        raise ValueError("Chebyshev terms must be even and >= 6")

    polynomials = [self.clone()]
    y = 4 * self.square() - 2
    z = y - 1
    polynomials.append(z.mul(self))

    for k in range(2, terms // 2):
        next_polynomial = y * polynomials[k - 1] - polynomials[k - 2]
        polynomials.append(next_polynomial)

    return curl.stack(polynomials)


def erf(self):
    r"""
    Approximates the error function of the input tensor using a Taylor approximation.
    """
    luts = LookupTables()
    lut_config = luts.get_config()
    method = lut_config.config["erf"]["method"]

    if method in ("haar", "bior"):
        sgn = self.sign()
        abs = sgn * self
        if method == "haar":
            erf_truncation = (
                lut_config.config["erf"]["lut_max_bits"]
                + cfg.encoder.precision_bits
                - lut_config.config["erf"]["haar_size_bits"]
            )
            if cfg.encoder.trunc_method.lut == "crypten":
                msb = abs.div(1 << erf_truncation)
            else:
                msb = abs.egk_trunc_pr(62, erf_truncation)
            lut = msb.evaluate_lut("erf", "haar")
        elif method == "bior":
            erf_truncation = (
                lut_config.config["erf"]["lut_max_bits"]
                + cfg.encoder.precision_bits
                - lut_config.config["erf"]["bior_size_bits"]
            )
            if cfg.encoder.trunc_method.lut == "crypten":
                msb, lsb = abs.divmod(1 << erf_truncation)
            else:
                msb, lsb = abs.egk_truncmod_pr(62, erf_truncation)
            lut = msb.evaluate_bior_lut("erf", "bior", lsb, erf_truncation)
        check = abs < 1 << lut_config.config["erf"]["lut_max_bits"] - 1
        return sgn * (1 - check + lut * check)
    elif method in ("haar-lut-only", "bior-lut-only"):  # using only LUT
        self = self + 2 ** (lut_config.config["erf"]["lut_max_bits"])
        if method == "haar-lut-only":
            truncation = (
                lut_config.config["erf"]["lut_max_bits"]
                + cfg.encoder.precision_bits
                - lut_config.config["erf"]["haar_size_bits"]
            )
            if cfg.encoder.trunc_method.lut == "crypten":
                msb = self.div(1 << truncation)
            else:
                msb = self.egk_trunc_pr(62, truncation)
            return msb.evaluate_lut("erf", "haar_lut_only")
        elif method == "bior-lut-only":
            total_bits = (
                lut_config.config["erf"]["lut_max_bits"] + cfg.encoder.precision_bits
            )
            truncation = total_bits - lut_config.config["erf"]["bior_size_bits"]
            if cfg.encoder.trunc_method.lut == "crypten":
                msb, lsb = self.divmod(1 << truncation)
            else:
                msb, lsb = self.egk_truncmod_pr(62, truncation)
            return msb.evaluate_bior_lut("erf", "bior_lut_only", lsb, truncation)
    elif method == "Taylor":
        iters = lut_config.config["erf"]["iterations"]

        output = self.clone()
        for n in range(1, iters + 1):
            multiplier = ((-1) ** n) / (math.factorial(n) * (2 * n + 1))
            output = output.add(self.pos_pow(2 * n + 1).mul(multiplier))
        return output.mul(2.0 / math.sqrt(math.pi))
        # NOTE: This approximation is not unstable for large tensor values.
    else:
        raise ValueError(f"Unrecognized method {method} for erf")


def gelu(self):
    r"""
    Approximates the gelu function of the input tensor.
    """
    luts = LookupTables()
    lut_config = luts.get_config()
    method = lut_config.config["gelu"]["method"]

    if method in ("haar", "bior"):
        sgn = self.sign()
        abs = sgn * self
        drelu = 1 - self._ltz()
        relu = self * drelu
        if method == "haar":
            truncation = (
                lut_config.config["gelu"]["lut_max_bits"]
                + cfg.encoder.precision_bits
                - lut_config.config["gelu"]["haar_size_bits"]
            )
            if cfg.encoder.trunc_method.lut == "crypten":
                msb = abs.div(1 << truncation)
            else:
                msb = abs.egk_trunc_pr(62, truncation)
            lut = msb.evaluate_lut("gelu", "haar")
        elif method == "bior":
            truncation = (
                lut_config.config["gelu"]["lut_max_bits"]
                + cfg.encoder.precision_bits
                - lut_config.config["gelu"]["bior_size_bits"]
            )
            if cfg.encoder.trunc_method.lut == "crypten":
                msb, lsb = abs.divmod(1 << truncation)
            else:
                msb, lsb = abs.egk_truncmod_pr(62, truncation)
            lut = msb.evaluate_bior_lut("gelu", "bior", lsb, truncation)
        check = abs < 1 << lut_config.config["gelu"]["lut_max_bits"]
        return relu - lut * check
    elif method in ("haar-lut-only", "bior-lut-only"):  # using only LUT for gelu
        self = self + 2 ** (lut_config.config["gelu"]["lut_max_bits"])
        if method == "haar-lut-only":
            truncation = (
                lut_config.config["gelu"]["lut_max_bits"]
                + cfg.encoder.precision_bits
                - lut_config.config["gelu"]["haar_size_bits"]
            )
            if cfg.encoder.trunc_method.lut == "crypten":
                msb = self.div(1 << truncation)
            else:
                msb = self.egk_trunc_pr(62, truncation)
            return msb.evaluate_lut("gelu", "haar_lut_only")
        elif method == "bior-lut-only":
            total_bits = (
                lut_config.config["gelu"]["lut_max_bits"] + cfg.encoder.precision_bits
            )
            truncation = total_bits - lut_config.config["gelu"]["bior_size_bits"]
            if cfg.encoder.trunc_method.lut == "crypten":
                msb, lsb = self.divmod(1 << truncation)
            else:
                msb, lsb = self.egk_truncmod_pr(62, truncation)
            return msb.evaluate_bior_lut("gelu", "bior_lut_only", lsb, truncation)
    elif method == "erf":
        gelu = self * (1 + (self / math.sqrt(2)).erf()) / 2
        return gelu
    else:
        raise ValueError(f"Unrecognized method {method} for gelu")


def silu(self):
    r"""
    Approximates the silu function of the input tensor.
    """
    luts = LookupTables()
    lut_config = luts.get_config()
    method = lut_config.config["silu"]["method"]

    if method in ("haar", "bior"):
        sgn = self.sign()
        abs = sgn * self
        drelu = 1 - self._ltz()
        relu = self * drelu
        if method == "haar":
            truncation = (
                lut_config.config["silu"]["lut_max_bits"]
                + cfg.encoder.precision_bits
                - lut_config.config["silu"]["haar_size_bits"]
            )
            if cfg.encoder.trunc_method.lut == "crypten":
                msb = abs.div(1 << truncation)
            else:
                msb = abs.egk_trunc_pr(62, truncation)
            lut = msb.evaluate_lut("silu", "haar")
        elif method == "bior":
            truncation = (
                lut_config.config["silu"]["lut_max_bits"]
                + cfg.encoder.precision_bits
                - lut_config.config["silu"]["bior_size_bits"]
            )
            if cfg.encoder.trunc_method.lut == "crypten":
                msb, lsb = abs.divmod(1 << truncation)
            else:
                msb, lsb = abs.egk_truncmod_pr(62, truncation)
            lut = msb.evaluate_bior_lut("silu", "bior", lsb, truncation)
        check = abs < 1 << lut_config.config["silu"]["lut_max_bits"] - 1
        return relu - lut * check
    elif method in ("haar-lut-only", "bior-lut-only"):  # using only LUT
        self = self + 2 ** (lut_config.config["silu"]["lut_max_bits"])
        if method == "haar-lut-only":
            truncation = (
                lut_config.config["silu"]["lut_max_bits"]
                + cfg.encoder.precision_bits
                - lut_config.config["silu"]["haar_size_bits"]
            )
            if cfg.encoder.trunc_method.lut == "crypten":
                msb = self.div(1 << truncation)
            else:
                msb = self.egk_trunc_pr(62, truncation)
            return msb.evaluate_lut("silu", "haar_lut_only")
        elif method == "bior-lut-only":
            total_bits = (
                lut_config.config["silu"]["lut_max_bits"] + cfg.encoder.precision_bits
            )
            truncation = total_bits - lut_config.config["silu"]["bior_size_bits"]
            if cfg.encoder.trunc_method.lut == "crypten":
                msb, lsb = self.divmod(1 << truncation)
            else:
                msb, lsb = self.egk_truncmod_pr(62, truncation)
            return msb.evaluate_bior_lut("silu", "bior_lut_only", lsb, truncation)
    elif method == "sigmoid":
        silu = self * self.sigmoid()
        return silu
    else:
        raise ValueError(f"Unrecognized method {method} for silu")


def softmax(self, dim, **kwargs):
    r"""Compute the softmax of a tensor's elements along a given dimension"""
    # 0-d case
    luts = LookupTables()
    lut_config = luts.get_config()
    if self.dim() == 0:
        assert dim == 0, "Improper dim argument"
        return self.new(torch.ones_like((self.data)))

    if self.size(dim) == 1:
        return self.new(torch.ones_like(self.data))

    maximum_value = self.max(dim, keepdim=True)[0]
    logits = self - maximum_value
    with lut_config.temp_override({"exp": {"all_neg": True}}):
        numerator = logits.exp()
    with lut_config.temp_override({"reciprocal": {"all_pos": True}}):
        inv_denominator = numerator.sum(dim, keepdim=True).reciprocal()
    return numerator * inv_denominator


def log_softmax(self, dim, **kwargs):
    r"""Applies a softmax followed by a logarithm.
    While mathematically equivalent to log(softmax(x)), doing these two
    operations separately is slower, and numerically unstable. This function
    uses an alternative formulation to compute the output and gradient correctly.
    """
    # 0-d case
    if self.dim() == 0:
        assert dim == 0, "Improper dim argument"
        return self.new(torch.zeros((), device=self.device))

    if self.size(dim) == 1:
        return self.new(torch.zeros_like(self.data))

    maximum_value = self.max(dim, keepdim=True)[0]
    logits = self - maximum_value
    normalize_term = exp(logits).sum(dim, keepdim=True)
    result = logits - normalize_term.log()
    return result
