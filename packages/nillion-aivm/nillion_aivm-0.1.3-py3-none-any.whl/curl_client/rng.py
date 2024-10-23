import torch

__RING_SIZE__ = 1 << 64


def generate_random_ring_element(size):
    """Helper function to generate a random number from a signed ring"""
    rand_value = torch.randint(
        -(__RING_SIZE__ // 2),
        0,
        size,
        dtype=torch.long,
    )
    rand_sign = torch.randint(
        -1,
        1,
        size,
        dtype=torch.long,
    )
    rand_element = (2 * rand_sign + 1) * (rand_value - rand_sign)
    return rand_element


def generate_random_binary_ring_element(size):
    """Helper function to generate a random number from a signed ring"""
    rand_value = torch.randint(
        0,
        2,
        size,
        dtype=torch.long,
    )
    return rand_value
