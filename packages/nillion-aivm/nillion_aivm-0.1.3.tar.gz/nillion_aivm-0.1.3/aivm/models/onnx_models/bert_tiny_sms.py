import tempfile

import curl
import onnx
import torch
from transformers import AutoModelForSequenceClassification, AutoTokenizer

__all__ = ["model", "tokenizer"]


def initialize_model():
    MODEL_NAME = "mrm8488/bert-tiny-finetuned-sms-spam-detection"
    model = AutoModelForSequenceClassification.from_pretrained(MODEL_NAME)
    tokenizer = AutoTokenizer.from_pretrained(MODEL_NAME)
    return model, tokenizer


def convert_pytorch_to_onnx_with_tokenizer(model, tokenizer, max_length):
    """
    Converts a PyTorch model to ONNX format, using tokenizer output as input.

    Args:
    model (torch.nn.Module): The PyTorch model to be converted.
    tokenizer: The tokenizer used to preprocess the input.
    onnx_file_path (str): The file path where the ONNX model will be saved.
    max_length (int): Maximum sequence length for the tokenizer.

    Returns:
    None
    """
    model.eval()

    # Prepare dummy input using the tokenizer
    dummy_input = "This is a sample input text for ONNX conversion."
    inputs = tokenizer(
        dummy_input,
        max_length=max_length,
        padding="max_length",
        truncation=True,
        return_tensors="pt",
    )

    # # Get the input names
    input_names = list(inputs.keys())
    input_names = ["input_ids", "attention_mask"]

    onnx_file_path = tempfile.mktemp(suffix=".onnx")
    dynamic_axes = {name: {0: "batch_size"} for name in input_names}
    dynamic_axes.update({f"logits": {0: "batch_size"}})
    # Export the model
    torch.onnx.export(
        model,  # model being run
        tuple(inputs[k] for k in input_names),  # model inputs
        onnx_file_path,  # where to save the model
        export_params=True,  # store the trained parameter weights inside the model file
        opset_version=20,  # the ONNX version to export the model to
        do_constant_folding=True,  # whether to execute constant folding for optimization
        input_names=input_names,  # the model's input names
        output_names=["logits"],  # the model's output names
        dynamic_axes=dynamic_axes,
    )  # variable length axes

    # Verify the exported model
    onnx_model = onnx.load(onnx_file_path)
    onnx.checker.check_model(onnx_model)
    return onnx_file_path, input_names


def init():
    model, tokenizer = initialize_model()
    hidden_size = model.config.hidden_size
    onnx_file_path, _ = convert_pytorch_to_onnx_with_tokenizer(
        model, tokenizer, max_length=hidden_size
    )

    tokenizer_partial = lambda x: tokenizer(
        x,
        return_tensors="pt",
        padding="max_length",
        truncation=True,
        max_length=hidden_size,
    )

    return onnx_file_path, tokenizer_partial


onnx_file_path, tokenizer = init()


# Use DefaultLUTConfig as LUTConfig from lut_config.py
from curl.config.lut_config import DefaultLUTConfig


def LUTConfig():
    config = DefaultLUTConfig()

    # Update LUTConfig with custom values
    config.apply_dict(
        {
            "reciprocal": {
                "haar_size_bits": 10,
                "lut_max_bits": 5,
            },
            "sqrt": {"bior_size_bits": 10, "lut_max_bits": 7},
        }
    )
    return config
