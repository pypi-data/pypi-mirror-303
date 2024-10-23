# AIVM Client

**AIVM Client** is a library designed as a wrapper around the client elements required to interact with the AIVM (AI Virtual Machine) infrastructure. This library simplifies communication with the AIVM nodes and provides the cryptographic tools necessary to ensure secure data exchange.

## Features

AIVM Client focuses on providing two main functionalities:

1. **Predictions & Model Uploads**  
   Users can upload custom machine learning models and request predictions from the AIVM infrastructure. This enables private inference where user data remains secure throughout the process.

2. **Cryptographic Communication**  
   The library handles the cryptographic infrastructure needed to facilitate secure communication between the client and the AIVM nodes. This ensures privacy and security during data transfers and model interactions.

## Table of Contents

- [Usage](#usage)
  - [Uploading a Custom Model](#uploading-a-custom-model)
  - [Requesting Predictions](#requesting-predictions)

---

## Usage

The AIVM Client library allows you to upload custom models to the AIVM infrastructure and request predictions on those models.

### Uploading a Custom Model

To upload a custom model, ensure that your model is properly packaged and ready to be sent to the AIVM infrastructure. Use the following example code to upload your model:

```python
import aivm_client as aic

# Initialize the AIVM Client
aic.init()

# Upload your custom model
model_path = "path_to_your_model.onnx"
aic.upload_model(model_path, "my_custom_model")
```

### Requesting Predictions

Once a model is uploaded, you can request predictions from the AIVM infrastructure by sending input data.

```python
import torch
import aivm_client as aic

# Initialize the AIVM Client
aic.init()

# Input data for the prediction
input_data = torch.ones((28, 28))
encrypted_input = aic.cryptensor(input_data)

# Request prediction
prediction = aic.get_prediction(encrypted_input, "my_custom_model")
```