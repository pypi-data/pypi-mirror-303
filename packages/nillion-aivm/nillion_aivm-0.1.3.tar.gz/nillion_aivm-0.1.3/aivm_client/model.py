import curl_client as curl
import torch


def upload_model(model_path, model_name, model_type):
    """
    Uploads the model to the server.

    Args:
        model_path: Path to the model file
        model_name: Name of the model
        model_type: Type of the model (must be one of the supported models)
    """
    curl.upload_model(model_path, model_name, model_type)


def upload_bert_tiny_model(model_path, model_name):
    """
    Uploads the Bert Tiny model to the server.

    Args:
        model_path: Path to the model file
        model_name: Name of the model
    """
    curl.upload_model(model_path, model_name, curl.ModelType.BertTiny)


def upload_lenet5_model(model_path, model_name):
    """
    Uploads the LeNet-5 model to the server.

    Args:
        model_path: Path to the model file
        model_name: Name of the model
    """

    curl.upload_model(model_path, model_name, curl.ModelType.LeNet5)
