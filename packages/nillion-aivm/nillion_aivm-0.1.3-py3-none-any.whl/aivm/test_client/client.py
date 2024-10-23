import argparse
import time

import curl_client as curl
import numpy as np
import torch
import torch.nn.functional as F
import torchvision.datasets as dset
import torchvision.transforms as transforms
import yaml

import aivm_client as aic


def load_mnist(batch_size=1):
    trans = transforms.Compose(
        [
            transforms.ToTensor(),
            transforms.Resize((28, 28)),
            transforms.Normalize((0.5,), (1.0,)),
        ]
    )
    train_set = dset.MNIST(
        root="/tmp/mnist", train=True, transform=trans, download=True
    )
    # test_set = dset.MNIST(root='./data', train=False, transform=trans)

    train_loader = torch.utils.data.DataLoader(
        dataset=train_set, batch_size=batch_size
    )  # ,shuffle=True)
    # test_loader = torch.utils.data.DataLoader(dataset=test_set,batch_size=batch_size,shuffle=False)
    return train_loader


def get_cnn_prediction_from_server(args):

    total_correct = 0
    total = 0
    total_time = 0
    # try:
    for i, batch in enumerate(load_mnist(1)):
        inputs, labels = batch
        inputs = aic.LeNet5Cryptensor(inputs)
        start = time.time()
        result = aic.get_prediction(inputs, "LeNet5MNIST")
        end = time.time()
        sm = torch.softmax(result, dim=1)
        results = torch.argmax(sm, dim=1)
        correct = (results == labels[0]).sum().item()
        accuracy = correct / len(labels)
        print("[LeNet5] Client Time: ", end - start)
        print(
            f"[LeNet5] Accuracy [{i}]: {accuracy * 100}% Correct: {correct} out of {len(labels)}"
        )
        total_correct += correct
        total += len(labels)
        total_time += end - start
        if i == 10:
            break


def get_llm_prediction_from_server(args, sentence="Hello, my dog is cute"):

    from aivm.models.onnx_models.bert_tiny_sms import tokenizer

    cleartext = tokenizer(sentence)

    print("Cleartext:", sentence)
    encrypted_inputs = aic.BertTinyCryptensor(
        cleartext["input_ids"], cleartext["attention_mask"]
    )
    start = time.time()
    prediction = aic.get_prediction(encrypted_inputs, "BertTinySMS").numpy()
    end = time.time()
    print("Prediction:", prediction)
    print("Prediction:", "SPAM" if np.argmax(prediction) == 1 else "HAM")
    print("[Bert Tiny] Client Time: ", end - start)


def read_yaml(config_path):
    with open(config_path, "r") as file:
        config = yaml.safe_load(file)
    return config


def upload_and_test_bert_tiny(args, model_path, sentence="Hello, my dog is cute"):
    try:
        aic.upload_bert_tiny_model(model_path, "ASDF")
    except Exception as e:
        print("Error uploading model:", e)

    from aivm.models.onnx_models.bert_tiny_sms import tokenizer

    cleartext = tokenizer(sentence)

    print("Cleartext:", sentence)
    encrypted_inputs = aic.BertTinyCryptensor(
        cleartext["input_ids"], cleartext["attention_mask"]
    )
    start = time.time()
    prediction = aic.get_prediction(encrypted_inputs, "ASDF").numpy()
    end = time.time()
    print("Prediction:", prediction)
    print("Prediction:", "SPAM" if np.argmax(prediction) == 1 else "HAM")
    print("[Bert Tiny] Client Time: ", end - start)


def main():
    argparser = argparse.ArgumentParser()
    argparser.add_argument("--model", type=str, default="all")
    argparser.add_argument("--host", type=str, nargs="+", default=["localhost:50050"])
    argparser.add_argument("--config", type=str, default=None)
    argparser.add_argument(
        "--wait", type=int, default=0, help="Wait time before requests"
    )
    argparser.add_argument("--num_requests", type=int, default=1)
    args = argparser.parse_args()

    if args.config is not None:
        config = read_yaml(args.config)
        args.host = f"{config['proxy_addr']}:{config['proxy_port']}"
    if args.model not in ["all", "BertTiny", "GPT2", "LeNet5"]:
        raise ValueError(f"Model {args.model} not supported by server")

    aic.init(args.host)
    time.sleep(args.wait)

    for i in range(args.num_requests):
        if args.model == "BertTiny":
            get_llm_prediction_from_server(args)
        elif args.model == "LeNet5":
            get_cnn_prediction_from_server(args)
        else:
            upload_and_test_bert_tiny(
                args, "./examples/test_model.onnx", "Hello, my dog is cute"
            )

            get_llm_prediction_from_server(args)
            get_llm_prediction_from_server(
                args,
                "Your free ringtone is waiting to be collected. Simply text the password 'MIX' to 85069 to verify. Get Usher and Britney. FML, PO Box 5249, MK17 92H. 450Ppw 16",
            )
            get_cnn_prediction_from_server(args)


if __name__ == "__main__":
    main()
