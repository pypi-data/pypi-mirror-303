import curl_client as curl

from aivm_config import default_config, generate_client_config

config = generate_client_config(default_config)

# Initialize curl with the specified hosts
print(f"Connecting to proxy {config['proxy_addr']}:{config['proxy_port']}")
curl.init(f"{config['proxy_addr']}:{config['proxy_port']}")

from aivm_client.bert_tiny_tokenizer import tokenize
from aivm_client.client import (BertTinyCryptensor, LeNet5Cryptensor,
                                cryptensor, get_prediction, get_supported_models)
from aivm_client.model import (upload_bert_tiny_model, upload_lenet5_model,
                               upload_model)

ModelType = curl.ModelType
init = curl.init

__all__ = [
    "cryptensor",
    "get_prediction",
    "BertTinyCryptensor",
    "LeNet5Cryptensor",
    "upload_model",
    "upload_bert_tiny_model",
    "upload_lenet5_model",
    "tokenize",
    "ModelType",
    "get_supported_models",
]
