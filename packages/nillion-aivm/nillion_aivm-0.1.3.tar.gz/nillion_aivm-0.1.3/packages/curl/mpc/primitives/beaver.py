#!/usr/bin/env python3

# Copyright (c) Facebook, Inc. and its affiliates.
#
# This source code is licensed under the MIT license found in the
# LICENSE file in the root directory of this source tree.

import logging

import curl
import curl.communicator as comm
import torch
from curl.common.util import count_wraps
from curl.config import cfg


class IgnoreEncodings:
    """Context Manager to ignore tensor encodings"""

    def __init__(self, list_of_tensors):
        self.list_of_tensors = list_of_tensors
        self.encodings_cache = [tensor.encoder.scale for tensor in list_of_tensors]

    def __enter__(self):
        for tensor in self.list_of_tensors:
            tensor.encoder._scale = 1

    def __exit__(self, exc_type, exc_value, exc_traceback):
        for i, tensor in enumerate(self.list_of_tensors):
            tensor.encoder._scale = self.encodings_cache[i]


def __beaver_protocol(op, x, y, *args, **kwargs):
    """Performs Beaver protocol for additively secret-shared tensors x and y

    1. Obtain uniformly random sharings [a],[b] and [c] = [a * b]
    2. Additively hide [x] and [y] with appropriately sized [a] and [b]
    3. Open ([epsilon] = [x] - [a]) and ([delta] = [y] - [b])
    4. Return [z] = [c] + (epsilon * [b]) + ([a] * delta) + (epsilon * delta)
    """
    assert op in {
        "mul",
        "matmul",
        "conv1d",
        "conv2d",
        "conv_transpose1d",
        "conv_transpose2d",
    }
    if x.device != y.device:
        raise ValueError(f"x lives on device {x.device} but y on device {y.device}")

    provider = curl.mpc.get_default_provider()
    a, b, c = provider.generate_additive_triple(
        x.size(), y.size(), op, device=x.device, *args, **kwargs
    )

    logging.debug(f"[<=>][BEAVER] C[{op}] tensor shape: {c.size()}")
    from .arithmetic import ArithmeticSharedTensor

    if provider.compute_online():
        if cfg.mpc.active_security:
            """
            Reference: "Multiparty Computation from Somewhat Homomorphic Encryption"
            Link: https://eprint.iacr.org/2011/535.pdf
            """
            f, g, h = provider.generate_additive_triple(
                x.size(), y.size(), op, device=x.device, *args, **kwargs
            )

            t = ArithmeticSharedTensor.PRSS(a.size(), device=x.device)
            t_plain_text = t.get_plain_text()

            rho = (t_plain_text * a - f).get_plain_text()
            sigma = (b - g).get_plain_text()
            triples_check = t_plain_text * c - h - sigma * f - rho * g - rho * sigma
            triples_check = triples_check.get_plain_text()

            if torch.any(triples_check != 0):
                raise ValueError("Beaver Triples verification failed!")

        # Vectorized reveal to reduce rounds of communication
        with IgnoreEncodings([a, b, x, y]):
            epsilon, delta = ArithmeticSharedTensor.reveal_batch([x - a, y - b])

        # z = c + (a * delta) + (epsilon * b) + epsilon * delta
        c._tensor += getattr(torch, op)(epsilon, b._tensor, *args, **kwargs)
        c._tensor += getattr(torch, op)(a._tensor, delta, *args, **kwargs)
        c += getattr(torch, op)(epsilon, delta, *args, **kwargs)

        logging.debug(f"[<=>][BEAVER] Output tensor shape: {c.size()}")
        return c

    ret = ArithmeticSharedTensor.from_shares(
        torch.zeros_like(c.share, dtype=x.share.dtype)
    )
    logging.debug(f"[<=>][BEAVER] Output tensor shape: {ret.size()}")
    return ret


def mul(x, y):
    return __beaver_protocol("mul", x, y)


def matmul(x, y):
    return __beaver_protocol("matmul", x, y)


def conv1d(x, y, **kwargs):
    return __beaver_protocol("conv1d", x, y, **kwargs)


def conv2d(x, y, **kwargs):
    return __beaver_protocol("conv2d", x, y, **kwargs)


def conv_transpose1d(x, y, **kwargs):
    return __beaver_protocol("conv_transpose1d", x, y, **kwargs)


def conv_transpose2d(x, y, **kwargs):
    return __beaver_protocol("conv_transpose2d", x, y, **kwargs)


def square(x):
    """Computes the square of `x` for additively secret-shared tensor `x`

    1. Obtain uniformly random sharings [r] and [r2] = [r * r]
    2. Additively hide [x] with appropriately sized [r]
    3. Open ([epsilon] = [x] - [r])
    4. Return z = [r2] + 2 * epsilon * [r] + epsilon ** 2
    """
    logging.debug(f"[<=>][SQUARE] Input tensor shape: {x.size()}")

    provider = curl.mpc.get_default_provider()
    r, r2 = provider.square(x.size(), device=x.device)
    if provider.compute_online():
        with IgnoreEncodings([x, r]):
            epsilon = (x - r).reveal()
        result = r2 + 2 * r * epsilon + epsilon * epsilon
        logging.debug(f"[<=>][SQUARE] Output tensor shape: {result.size()}")
        return result

    from .arithmetic import ArithmeticSharedTensor

    ret = ArithmeticSharedTensor.from_shares(
        torch.zeros_like(x.share, dtype=x.share.dtype)
    )
    logging.debug(f"[<=>][SQUARE] Output tensor shape: {ret.size()}")

    return ret


def wraps(x):
    """Privately computes the number of wraparounds for a set a shares

    To do so, we note that:
        [theta_x] = theta_z + [beta_xr] - [theta_r] - [eta_xr]

    Where [theta_i] is the wraps for a variable i
          [beta_ij] is the differential wraps for variables i and j
          [eta_ij]  is the plaintext wraps for variables i and j

    Note: Since [eta_xr] = 0 with probability 1 - |x| / Q for modulus Q, we
    can make the assumption that [eta_xr] = 0 with high probability.
    """
    logging.debug(f"[<=>][WRAPS] Input tensor shape: {x.size()}")

    provider = curl.mpc.get_default_provider()
    r, theta_r = provider.wrap_rng(x.size(), device=x.device)

    if provider.compute_online():
        beta_xr = theta_r.clone()
        beta_xr._tensor = count_wraps([x._tensor, r._tensor])

        with IgnoreEncodings([x, r]):
            z = x + r
        theta_z = comm.get().gather(z._tensor, 0)
        theta_x = beta_xr - theta_r

        # TODO: Incorporate eta_xr
        if x.rank == 0:
            theta_z = count_wraps(theta_z)
            theta_x._tensor += theta_z

        logging.debug(f"[<=>][WRAPS] Output tensor shape: {theta_x.size()}")
        return theta_x
    from .arithmetic import ArithmeticSharedTensor

    ret = ArithmeticSharedTensor.from_shares(
        torch.zeros_like(x.share, dtype=x.share.dtype)
    )
    logging.debug(f"[<=>][WRAPS] Output tensor shape: {ret.size()}")
    return ret


def truncate(x, y):
    """Protocol to divide an ArithmeticSharedTensor `x` by a constant integer `y`"""
    wrap_count = wraps(x)
    x.share = x.share.div_(y, rounding_mode="trunc")
    # NOTE: The multiplication here must be split into two parts
    # to avoid long out-of-bounds when y <= 2 since (2 ** 63) is
    # larger than the largest long integer.
    correction = wrap_count * 4 * (int(2**62) // y)
    x.share -= correction.share
    return x


def egk_trunc_pr(x, l, m):
    """
    Evaluates probabilistic truncation with no correctness error using [EGK+20]
    protocol.

    Reference: "Improved Primitives for MPC over Mixed Arithmetic-Binary Circuits"
    Figure: 10
    Link: https://eprint.iacr.org/2020/338.pdf

    Args:
        x (torch.Tensor): Input tensor.
        l (int): Max bit size of input tensor, i.e., 0 <= x < 2**l.
        m (int): number of bits to truncate.

    Returns:
        torch.Tensor: Result tensor after applying the LUT.
    """
    logging.debug(f"[<=>][EGK_TRUNC_PR] Input tensor shape: {x.size()}")

    provider = curl.mpc.get_default_provider()
    k = 64
    two_to_l = torch.tensor(
        2**l, dtype=torch.int64, device=x.device
    )  # to prevent overflow
    tensor_size = x.size()

    # Preprocessing
    r, r_p, b = provider.egk_trunc_pr_rng(tensor_size, l, m, device=x.device)
    if provider.compute_online():
        with IgnoreEncodings([x, b]):
            # Step 1
            a_p = x + 2 ** (l - 1)  # allowing negative numbers
            rpp = 2**m * r + r_p
            enc_c = 2 ** (k - l - 1) * (a_p + two_to_l * b + rpp)
            c = enc_c.reveal()
            c_p = c >> (k - l - 1)
            # Step 2
            c_pl = (c_p >> l) & 1  # c'_l, the l-th (last) bit of c'
            v = b + c_pl - 2 * b * c_pl
            # Step 3
            y = 2 ** (l - m) * v - r - 2 ** (l - m - 1) + ((c_p % two_to_l) // 2**m)

        logging.debug(f"[<=>][EGK_TRUNC_PR] Output tensor shape: {y.size()}")
        return y
    from .arithmetic import ArithmeticSharedTensor

    ret = ArithmeticSharedTensor.from_shares(
        torch.zeros_like(x.share, dtype=x.share.dtype)
    )
    logging.debug(f"[<=>][EGK_TRUNC_PR] Output tensor shape: {ret.size()}")
    return ret


def evaluate_lut(x, lut):
    """Evaluates a Look-Up Table (LUT) using an input tensor x.

    Args:
        x (Cryptensor): Input tensor.
        lut (torch.Tensor): Look-Up Table tensor.

    Returns:
        Cryptensor: Result tensor after applying the LUT.
    """
    logging.debug(f"[<=>][LUT] Input tensor shape: {x.size()}")

    provider = curl.mpc.get_default_provider()
    size = lut.size()[0]
    shape = x.size()
    x = x.flatten()

    # Generate one-hot vectors for each element of x
    r, one_hot_r = provider.generate_one_hot(x.size(), size, device=x.device)

    if provider.compute_online():
        # Reveal the shift amounts
        with IgnoreEncodings([x, r]):
            z = x - r
            shift_amount = z.reveal() % size

        if shift_amount.size():
            arange = torch.arange(size).to(device=x.device)
            indices = (arange[None, :] - shift_amount[:, None]) % size
            one_hot_r = one_hot_r.gather(1, indices)
            lookup = one_hot_r * lut
            result = lookup.sum(dim=1)
        else:
            one_hot_r = one_hot_r.roll(int(shift_amount))
            lookup = one_hot_r * lut
            result = lookup.sum()
        result = result.reshape(shape)
        logging.debug(f"[<=>][LUT] Output tensor shape: {result.size()}")
        return result
    x = x.reshape(shape)  # Returning x to avoid errors
    from .arithmetic import ArithmeticSharedTensor

    ret = ArithmeticSharedTensor.from_shares(
        torch.zeros_like(x.share, dtype=x.share.dtype)
    )
    logging.debug(f"[<=>][LUT] Output tensor shape: {ret.size()}")
    return ret


def evaluate_bior_lut(x, luts, scale, bias):
    """Evaluates a Look-Up Table (LUT) using an input tensor x.

    Args:
        x (Cryptensor): Input tensor.
        luts (torch.Tensor): Look-Up Table tensors.
        scale (torch.Tensor): Scaling factor for the lookups.
        bias (int): Bias for the LUT.

    Returns:
        Cryptensor: Result tensor after applying the LUT.
    """
    logging.debug(f"[<=>][BIOR_LUT] Input tensor shape: {x.size()}")
    provider = curl.mpc.get_default_provider()
    size = luts[0].size()[0]
    shape = x.size()
    x = x.flatten()

    # Generate one-hot vectors for each element of x
    r, one_hot_r = provider.generate_one_hot(x.size(), size, device=x.device)

    if provider.compute_online():
        # Reveal the shift amounts
        with IgnoreEncodings([x, r]):
            z = x - r
            shift_amount = z.reveal() % size

        if shift_amount.size():
            arange = torch.arange(size).to(device=x.device)
            indices = (arange[None, :] - shift_amount[:, None]) % size
            one_hot_r = one_hot_r.gather(1, indices)
            lookup0 = one_hot_r * luts[0]
            lut0 = lookup0.sum(dim=1)
            lookup1 = one_hot_r * luts[1]
            lut1 = lookup1.sum(dim=1)
        else:
            one_hot_r = one_hot_r.roll(int(shift_amount))
            lookup0 = one_hot_r * luts[0]
            lut0 = lookup0.sum()
            lookup1 = one_hot_r * luts[1]
            lut1 = lookup1.sum()
        with IgnoreEncodings([scale]):
            scaling = scale.flatten()
            lut = (lut1 - lut0) * scaling + 2**bias * lut0
            result = lut.egk_trunc_pr(62, 2 * bias)  # div by 2**(2*bias)
            result = result.reshape(shape)

        logging.debug(f"[<=>][BIOR_LUT] Output tensor shape: {result.size()}")
        return result

    x * x  # Purposely done to generate the prep elements required by compute BEAVER + EKG
    x = x.reshape(shape)  # Returning x to avoid errors
    from .arithmetic import ArithmeticSharedTensor

    ret = ArithmeticSharedTensor.from_shares(
        torch.zeros_like(x.share, dtype=x.share.dtype)
    )
    logging.debug(f"[<=>][BIOR_LUT] Output tensor shape: {ret.size()}")
    return ret


def evaluate_embed(x, embed):
    """Evaluates an embedding using an input tensor x.

    Args:
        x (torch.Tensor): Input tensor.
        embed (Cryptensor): Embedding tensor.

    Returns:
        Cryptensor: Result tensor after applying the LUT.
    """
    from .arithmetic import ArithmeticSharedTensor

    logging.debug(f"[<=>][EMBED] Input tensor shape: {x.size()}")
    provider = curl.mpc.get_default_provider()
    size = embed.size()[0]
    shape = x.size() + (embed.size()[1],)
    x = x.flatten()

    embed = ArithmeticSharedTensor.from_shares(embed, precision=0)

    # Generate one-hot vectors for each element of x
    r, one_hot_r = provider.generate_one_hot(x.size(), size, device=x.device)

    if provider.compute_online():
        # Reveal the shift amounts
        with IgnoreEncodings([x, r]):
            z = x - r
            shift_amount = z.reveal() % size

        if shift_amount.size():
            arange = torch.arange(size).to(device=x.device)
            indices = (arange[None, :] - shift_amount[:, None]) % size
            one_hot_r = one_hot_r.gather(1, indices)
            lookup = one_hot_r.matmul(embed)
        else:
            one_hot_r = one_hot_r.roll(int(shift_amount))
            lookup = one_hot_r.matmul(embed)
        result = lookup.reshape(shape)
        logging.debug(f"[<=>][EMBED] Output tensor shape: {result.size()}")
        return result

    _ = one_hot_r.matmul(embed)  # Purposely done to generate the prep elements
    ret = ArithmeticSharedTensor.from_shares(
        torch.zeros(shape, dtype=x.share.dtype)
    )  # Returning x to avoid errors
    logging.debug(f"[<=>][EMBED] Output tensor shape: {ret.size()}")
    return ret


def AND(x, y):
    """
    Performs Beaver protocol for binary secret-shared tensors x and y

    1. Obtain uniformly random sharings [a],[b] and [c] = [a & b]
    2. XOR hide [x] and [y] with appropriately sized [a] and [b]
    3. Open ([epsilon] = [x] ^ [a]) and ([delta] = [y] ^ [b])
    4. Return [c] ^ (epsilon & [b]) ^ ([a] & delta) ^ (epsilon & delta)
    """
    from .binary import BinarySharedTensor

    logging.debug(f"[<=>][AND] Input tensor shape: {x.size()}")
    provider = curl.mpc.get_default_provider()
    a, b, c = provider.generate_binary_triple(x.size(), y.size(), device=x.device)
    if provider.compute_online():
        # Stack to vectorize reveal
        eps_del = BinarySharedTensor.reveal_batch([x ^ a, y ^ b])
        epsilon = eps_del[0]
        delta = eps_del[1]
        result = (b & epsilon) ^ (a & delta) ^ (epsilon & delta) ^ c

        logging.debug(f"[<=>][AND] Output tensor shape: {result.size()}")

        return result
    from .arithmetic import ArithmeticSharedTensor

    ret = ArithmeticSharedTensor.from_shares(
        torch.zeros_like(x.share, dtype=x.share.dtype)
    )
    logging.debug(f"[<=>][AND] Output tensor shape: {ret.size()}")
    return ret  # Returning x to avoid errors


def B2A_single_bit(xB):
    """Converts a single-bit BinarySharedTensor xB into an
        ArithmeticSharedTensor. This is done by:

    1. Generate ArithmeticSharedTensor [rA] and BinarySharedTensor =rB= with
        a common 1-bit value r.
    2. Hide xB with rB and open xB ^ rB
    3. If xB ^ rB = 0, then return [rA], otherwise return 1 - [rA]
        Note: This is an arithmetic xor of a single bit.
    """
    from .arithmetic import ArithmeticSharedTensor

    logging.debug(f"[<=>][B2A] Input tensor shape: {xB.size()}")

    if comm.get().get_world_size() < 2:
        return ArithmeticSharedTensor(xB._tensor, precision=0, src=0)

    provider = curl.mpc.get_default_provider()
    rA, rB = provider.B2A_rng(xB.size(), device=xB.device)
    if provider.compute_online():
        z = (xB ^ rB).reveal()
        rA = rA * (1 - 2 * z) + z
        logging.debug(f"[<=>][B2A] Output tensor shape: {rA.size()}")
        return rA
    ret = ArithmeticSharedTensor.from_shares(
        torch.zeros_like(xB.share)
    )  # Returning xB to avoid errors
    logging.debug(f"[<=>][B2A] Output tensor shape: {rA.size()}")
    return ret
