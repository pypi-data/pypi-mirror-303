import curl_client as curl
import torch

# Function aliases for curl prediction and cryptensor creation
get_prediction = curl.get_prediction
cryptensor = curl.cryptensor


class BertTinyCryptensor(curl.ArithmeticSharedTensor):
    """
    A custom wrapper around ArithmeticSharedTensor for BertTiny model inputs.

    The BertTiny model expects a concatenation of token tensor and attention mask.
    This class concatenates the two tensors along the first dimension and
    inherits from ArithmeticSharedTensor to enable cryptographic operations.

    Args:
        *inputs (torch.Tensor): Two tensors (tokens and attention_mask), each of shape (1, 128).
    """

    def __init__(self, *inputs):
        # The inputs to BertTiny are expected to be a list of two tensors: tokens and attention_mask.
        # Concatenating inputs to form a single tensor of shape (2, 128).
        inputs = torch.cat(inputs)
        super().__init__(inputs, precision=0)

    def forward(self, model_name):
        return curl.get_prediction(self, model_name, curl.ModelType.BertTiny)


class LeNet5Cryptensor(curl.ArithmeticSharedTensor):
    """
    A custom wrapper around ArithmeticSharedTensor for LeNet-5 model inputs.

    This class directly inherits from ArithmeticSharedTensor and takes in
    input tensors to enable cryptographic operations for the LeNet-5 model.

    Args:
        inputs (torch.Tensor): Input tensor for the LeNet-5 model.
    """

    def __init__(self, inputs):
        # Reshape the input tensor to match the expected shape of the LeNet-5 model.
        # If the input tensor is of shape (28, 28), reshape it to (1, 1, 28, 28).
        # If it fails to reshape, raise a ValueError.
        super().__init__(inputs.reshape(1, 1, 28, 28))

    def forward(self, model_name):
        return curl.get_prediction(self, model_name, curl.ModelType.LeNet5)


def get_prediction(inputs, model, model_type=None):
    """
    Get predictions from a model using encrypted tensors.

    This function checks if the input is an instance of a supported cryptensor type
    and then fetches the prediction using the curl prediction mechanism.

    Args:
        inputs: Input tensor for the model. Must be a cryptensor type.
        model: Model to be used for predictions. Supported models include LeNet-5 and BertTiny.

    Returns:
        Prediction result from the model.

    Raises:
        ValueError: If inputs are not of a supported cryptensor type.
    """
    if isinstance(inputs, BertTinyCryptensor):
        return curl.get_prediction(inputs, model, curl.ModelType.BertTiny)
    elif isinstance(inputs, LeNet5Cryptensor):
        return curl.get_prediction(inputs, model, curl.ModelType.LeNet5)
    elif isinstance(inputs, curl.ArithmeticSharedTensor) and model_type is not None:
        return curl.get_prediction(inputs, model, model_type)
    raise ValueError(
        "Either the input tensor type is BertTinyCryptensor or LeNet5Cryptensor or you must provide a model_type with your cryptensor."
    )


def get_supported_models():
    """
    Retrieve a list of supported models for prediction.

    This function calls the curl client's `get_supported_models` to fetch a list
    of models that are available for inference.

    Returns:
        list: List of supported model names.
    """
    return curl.get_supported_models()
