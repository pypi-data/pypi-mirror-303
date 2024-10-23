from curl_client.encoder import FixedPointEncoder, is_int_tensor
from curl_client.rng import generate_random_ring_element


# MPC tensor where shares additive-sharings.
class ArithmeticSharedTensor:
    """
    Encrypted tensor object that uses additive sharing to perform computations.

    Additive shares are computed by splitting each value of the input tensor
    into n separate random values that add to the input tensor, where n is
    the number of parties present in the protocol (world_size).
    """

    # constructors:
    def __init__(
        self,
        tensor,
        num_shares=2,
        precision=None,
        empty=False,
    ):
        """
        Creates the shared tensor from the input `tensor` provided by party `src`.

        The other parties can specify a `tensor` or `size` to determine the size
        of the shared tensor object to create. In this case, all parties must
        specify the same (tensor) size to prevent the party's shares from varying
        in size, which leads to undefined behavior.

        Alternatively, the parties can set `broadcast_size` to `True` to have the
        `src` party broadcast the correct size. The parties who do not know the
        tensor size beforehand can provide an empty tensor as input. This is
        guaranteed to produce correct behavior but requires an additional
        communication round.

        The parties can also set the `precision` and `device` for their share of
        the tensor. If `device` is unspecified, it is set to `tensor.device`.
        """

        if empty:
            return

        # if device is unspecified, try and get it from tensor:
        if tensor is None:
            raise ValueError("ArithmeticSharedTensor requires a tensor input.")

        self.num_shares = num_shares
        # encode the input tensor:
        self.encoder = FixedPointEncoder(precision_bits=precision)

        if is_int_tensor(tensor) and precision != 0:
            tensor = tensor.float()
        tensor = self.encoder.encode(tensor)
        size = tensor.size()

        self.shares = [
            generate_random_ring_element(size) for _ in range(self.num_shares - 1)
        ]
        self.shares = [tensor - sum(self.shares)] + self.shares

    def reconstruct(self):
        """Reconstructs the shared tensor from shares."""
        return self.encoder.decode(sum(self.shares))

    @staticmethod
    def from_shares(shares, precision=None):
        """Creates a shared tensor from shares."""
        new = ArithmeticSharedTensor(None, empty=True)
        new.encoder = FixedPointEncoder(precision_bits=precision)
        new.shares = shares
        new.num_shares = len(shares)
        return new


if __name__ == "__main__":
    a = ArithmeticSharedTensor([1, 2, 3, 4, 5, 6, 7, 8, 9, 10], num_shares=3)

    print(a.reconstruct())
    for i in range(a.num_shares):
        print(a.shares[i])
