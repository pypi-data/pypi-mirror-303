from transformers import AutoTokenizer


def tokenize(sentence):
    MODEL_NAME = "mrm8488/bert-tiny-finetuned-sms-spam-detection"
    tokenizer = AutoTokenizer.from_pretrained(MODEL_NAME)
    inputs = tokenizer(
        sentence,
        max_length=128,
        padding="max_length",
        truncation=True,
        return_tensors="pt",
    )
    return (inputs["input_ids"], inputs["attention_mask"])
