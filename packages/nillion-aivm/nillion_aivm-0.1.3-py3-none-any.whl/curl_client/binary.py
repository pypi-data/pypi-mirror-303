from curl_client.encoder import FixedPointEncoder, is_int_tensor
from curl_client.rng import generate_random_binary_ring_element


def xor(shares):
    """
    Helper function to compute the XOR of a list of shares.

    Args:
        shares (list): A list of tensor shares to be XORed.

    Returns:
        tensor: The result of XORing all the provided shares.
    """
    result = shares[0]
    for share in shares[1:]:
        result = result ^ share
    return result


# MPC tensor where shares additive-sharings.
class BinarySharedTensor:
    """
    Encrypted tensor object that uses additive sharing to perform computations.

    Additive shares are computed by splitting each value of the input tensor
    into n separate random values that add to the input tensor, where n is
    the number of parties present in the protocol (world_size).
    """

    def __init__(
        self,
        tensor,
        num_shares=2,
        precision=None,
        empty=False,
    ):
        """
        Initializes a BinarySharedTensor with additive shares.

        Args:
            tensor (tensor): The input binary tensor to be shared.
            size (tuple, optional): The size of the shared tensor. Defaults to None.
            num_shares (int, optional): The number of shares to generate. Defaults to 2.
            precision (int, optional): The precision for encoding. Defaults to None.

        Raises:
            ValueError: If the input tensor is not binary or not provided.
        """
        if empty:
            return

        if tensor is None:
            raise ValueError("BinarySharedTensor requires a tensor input.")

        if any([x != 0 and x != 1 for x in tensor]):
            raise ValueError("BinarySharedTensor requires a binary tensor input.")

        self.num_shares = num_shares
        self.encoder = FixedPointEncoder(precision_bits=0)

        if is_int_tensor(tensor) and precision != 0:
            tensor = tensor.float()
        tensor = self.encoder.encode(tensor)
        size = tensor.size()

        self.shares = [
            generate_random_binary_ring_element(size)
            for _ in range(self.num_shares - 1)
        ]
        self.shares = [tensor ^ xor(self.shares)] + self.shares

    def reconstruct(self):
        """
        Reconstructs the original tensor from its shares.

        Returns:
            tensor: The decoded tensor reconstructed from the shares.
        """
        return xor(self.shares)

    @classmethod
    def from_shares(shares, precision=None):
        """Creates a shared tensor from shares."""
        new = BinarySharedTensor(None, empty=True)
        new.encoder = FixedPointEncoder(precision_bits=precision)
        new.shares = shares
        new.num_shares = len(shares)
        return new


if __name__ == "__main__":
    value = [1, 0, 1, 0, 1, 0]
    a = BinarySharedTensor(value, num_shares=3)
    print("Original: ", value)
    print("Reconstructed: ", a.reconstruct())
    for i in range(a.num_shares):
        print(a.shares[i])
