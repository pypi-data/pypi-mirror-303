import torch
from curl_client.arithmetic import ArithmeticSharedTensor
from curl_client.binary import BinarySharedTensor
from curl_client.network import ModelType, NetworkManager

__DEFAULT_CRYPTENSOR_TYPE__ = "arithmetic"
__CRYPTENSOR_TYPES__ = {
    "arithmetic": ArithmeticSharedTensor,
    "binary": BinarySharedTensor,
}

__all__ = [
    "init",
    "get_prediction",
    "cryptensor",
    "save",
    "upload_model",
    "from_shares",
    "get_supported_models",
    "localhost_init",
    "ModelType",
]


class CurlClient:

    def __init__(self):
        self.net = None

    def init(self, hosts):
        """
        Initializes the network manager with the provided hosts and ports.

        Args:
            hosts: List of hostnames
            ports: List of ports
        """
        self.net = NetworkManager(hosts)

    def localhost_init(self, num_nodes=2):
        """
        Initializes the network manager with the default hosts and ports.
        """
        self.init([f"localhost:{50051 + i}" for i in range(num_nodes)])

    def get_prediction(self, tensor, model, model_type):
        """
        Sends shares to the server using the provided gRPC stub.

        Args:
            shares: The shares to be sent
        """
        if self.net is None:
            raise ValueError(
                "Network manager not initialized. Please call init() first."
            )
        self.net.retrieve_server_configuration()  # Update the server configuration

        if not isinstance(tensor, (ArithmeticSharedTensor, BinarySharedTensor)):
            raise ValueError("Input tensor must be a CrypTensor")

        shared_tensor = from_shares(
            self.net.get_prediction(
                tensor.shares, model, tensor.encoder.precision_bits, model_type
            )
        )
        return shared_tensor.reconstruct()

    def upload_model(self, model_path, model_name, model_type):
        """
        Uploads the model to the server.

        Args:
            model_path: Path to the model file
            model_name: Name of the model
            model_type: Type of the model (must be one of the supported models)

        Returns:
            Response from the server
        """

        if self.net is None:
            raise ValueError(
                "Network manager not initialized. Please call init() first."
            )

        return self.net.upload_model(model_path, model_name, model_type)


CLIENT = CurlClient()


def init(hosts):
    """
    Initializes the network manager with the provided hosts and ports.

    Args:
        hosts: List of hostnames
        ports: List of ports
    """
    CLIENT.init(hosts)


def localhost_init(num_nodes=2):
    """
    Initializes the network manager with the default hosts and ports.
    """
    CLIENT.localhost_init(num_nodes)


def get_prediction(tensor, model, model_type):
    """
    Sends shares to the server using the provided gRPC stub.

    Args:
        shares: The shares to be sent
    """
    return CLIENT.get_prediction(tensor, model, model_type)


def get_supported_models():
    """
    Returns the supported models by the server.

    Returns:
        List of supported models
    """
    return CLIENT.net.server_configuration.models


def cryptensor(*args, cryptensor_type=None, **kwargs):
    """
    Factory function to return encrypted tensor of given `cryptensor_type`. If no
    `cryptensor_type` is specified, the default type is used.
    """

    # determine CrypTensor type to use:
    if cryptensor_type is None:
        cryptensor_type = __DEFAULT_CRYPTENSOR_TYPE__
    if cryptensor_type not in __CRYPTENSOR_TYPES__:
        raise ValueError("CrypTensor type %s does not exist." % cryptensor_type)

    # create CrypTensor:
    return __CRYPTENSOR_TYPES__[cryptensor_type](*args, **kwargs)


def from_shares(*args, cryptensor_type=None, **kwargs):
    """
    Factory function to return encrypted tensor of given `cryptensor_type`. If no
    `cryptensor_type` is specified, the default type is used.
    """

    # determine CrypTensor type to use:
    if cryptensor_type is None:
        cryptensor_type = __DEFAULT_CRYPTENSOR_TYPE__
    if cryptensor_type not in __CRYPTENSOR_TYPES__:
        raise ValueError("CrypTensor type %s does not exist." % cryptensor_type)

    # create CrypTensor:
    return __CRYPTENSOR_TYPES__[cryptensor_type].from_shares(*args, **kwargs)


def save(obj, f, save_closure=torch.save, **kwargs):
    """
    Saves the shares of CrypTensor or an encrypted model to a file.

    Args:
        obj: The CrypTensor or PyTorch tensor to be saved
        f: a file-like object (has to implement `read()`, `readline()`,
              `tell()`, and `seek()`), or a string containing a file name
        save_closure: Custom save function that matches the interface of `torch.save`,
        to be used when the tensor is saved with a custom load function in
        `curl.load`. Additional kwargs are passed on to the closure.
    """
    # TODO: Add support for saving to correct device (kwarg: map_location=device)
    save_closure(obj, f, **kwargs)


def upload_model(model_path, model_name, model_type):
    """
    Uploads the model to the server.

    Args:
        model_path: Path to the model file
        model_name: Name of the model

    Returns:
        Response from the server
    """
    return CLIENT.upload_model(model_path, model_name, model_type)
