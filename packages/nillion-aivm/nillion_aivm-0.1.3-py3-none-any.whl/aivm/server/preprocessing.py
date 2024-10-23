import logging
import os
import shutil
from uuid import uuid4

import curl
import torch

from aivm_config import cfg


class PreprocessingManager(object):
    """This class is responsible for managing the preprocessing elements."""

    _instance = None
    keep_alive_model = "MeshKeepAlive"

    def __new__(cls, *args, **kwargs):
        """This is a singleton class."""
        if cls._instance is None:
            cls._instance = super(PreprocessingManager, cls).__new__(cls)
        return cls._instance

    def __init__(self, max_elements=10):
        """At bootstrap it produces a dictionary of lists of models."""
        # Prevent reinitialization on subsequent instantiations
        if not hasattr(self, "initialized"):
            self.models = {model_type: list() for model_type in cfg.model_types}
            self.max_elements = max_elements
            self.initialized = True  # Add an attribute to mark initialization

        self.preprocessing = False
        self.use_preprocessing = False
        self.model = None
        self.model_type = None
        self.num_timeouts = 0
        self.keep_alive = False

    def set_mode(self, model, model_type, preprocessing):
        """Set the model and the preprocessing mode."""
        self.model = model
        self.model_type = model_type
        if model == PreprocessingManager.keep_alive_model:
            preprocessing = False
            self.keep_alive = True
        self.preprocessing = preprocessing

        return self

    def __str__(self):
        s = "=" * 10
        s += f"\nPreprocessingManager:"
        for model in self.models:
            s += f"\n{model}: {len(self.models[model])}"
        return s

    def __repr__(self):
        return self.__str__()

    def produce_request(self):
        """Produces a request for the preprocessing elements for the model with least params
        and less than max_elements. This is executed only on the Coordinator node."""
        min_model_type, min_elements = None, self.max_elements
        if not cfg.config["disable_preprocessing"]:
            for model in self.models:
                prep_elements = len(self.models[model])
                if (
                    prep_elements
                    < cfg.config["model_types"][model]["preprocessing_elements"]
                    and prep_elements < min_elements
                ):
                    min_model_type, min_elements = model, prep_elements

        if not min_model_type is None:
            self.num_timeouts = 0
            return min_model_type

        if self.num_timeouts > 10:
            self.num_timeouts = 0
            return PreprocessingManager.keep_alive_model
        self.num_timeouts += 1
        return None

    def produce_request_for_model(self, model_type):
        """Produces a request for the preprocessing elements for the given model.
        This is executed on the Worker nodes."""
        logging.debug(f"Produce request for model {model_type} in {self.models}")
        if model_type in self.models:
            return (
                curl.cryptensor(
                    torch.ones(cfg.config["model_types"][model_type]["input_shape"])
                ),
                cfg.config["model_types"][model_type]["preprocessing_model"],
                model_type,
            )
        elif model_type == PreprocessingManager.keep_alive_model:
            return (
                curl.cryptensor(torch.ones((1,))),
                PreprocessingManager.keep_alive_model,
                PreprocessingManager.keep_alive_model,
            )
        raise ValueError(f"Model {model_type} not supported by server")

    def __enter__(self):
        if self.preprocessing:
            self.use_preprocessing = False
            curl.trace(True)
        else:
            # Check if we have cached prep elements
            if self.model_type in self.models and len(self.models[self.model_type]) > 0:
                logging.debug(f"Loading from cache: {self.models[self.model_type]}")

                self.use_preprocessing = True
                # Load them if we do
                filepath = self.models[self.model_type].pop()
                curl.load_cache(filepath)
                # Remove from list
                shutil.rmtree(filepath)
            else:
                logging.debug(f"No cache found for {self.model_type}")
                # If we don't have any cached elements, we set the flag to False
                self.use_preprocessing = False

        return self

    def __exit__(self, type, value, traceback):
        if type or value or traceback:  # If there's an error we don't want to cache
            return False

        if self.preprocessing:

            # We fill the tuple cache
            curl.fill_cache()
            uuid = uuid4()
            # We generate a unique file path
            file_path = os.path.join("/tmp/", f"cache-{uuid}.pth")
            # We create the directory if it doesn't exist
            os.makedirs(file_path, exist_ok=True)
            # We save the cache
            curl.save_cache(file_path)
            self.models[self.model_type].append(file_path)
            logging.debug(f"Saving to cache: {self.models[self.model_type]}")
        # If there's any cache, we empty it to avoid a "memory leak" like situation
        curl.empty_cache()
        curl.trace(False)
        self.keep_alive = False
        self.preprocessing = False
