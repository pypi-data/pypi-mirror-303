import logging

import curl
import torch


class ForwardHook:

    def __init__(self, debug=False, logging_level=logging.debug):
        self.debug = debug
        self.logging_level = logging_level
        self.tabs = 0
        self.fc = 0

    def forward_decorator(self, original_forward):
        if not self.debug:
            # Return original forward function if debug is disabled
            return original_forward
        hook = self

        # Define new forward function
        def new_forward(self, *args, **kwargs):
            hook.fc += 1
            hook.logging_level(
                "\\t" * hook.tabs + f"[>>>][{hook.fc}][{self.__class__.__name__}]"
            )

            # Loop through positional arguments
            for arg in args:
                if not isinstance(arg, list):
                    arg = [arg]

                for i, arg_i in enumerate(arg):
                    if hasattr(arg_i, "shape"):
                        # Generalized to handle any object with 'shape' attribute
                        hook.logging_level(
                            "\\t" * hook.tabs
                            + f"[{self.__class__.__name__}] Input {i}: {type(arg_i)} {arg_i.shape}"
                        )
                    else:
                        hook.logging_level(
                            "\\t" * hook.tabs
                            + f"[{self.__class__.__name__}] Input {i}: {type(arg_i)}"
                        )
                    if isinstance(arg_i, (torch.Tensor, curl.mpc.mpc.MPCTensor)):
                        arg[i] = arg_i.clone()

            for key, value in kwargs.items():
                if hasattr(value, "shape"):
                    hook.logging_level(
                        "\\t" * hook.tabs
                        + f"[{self.__class__.__name__}] Kwarg {key}: {type(value)} {value.shape}"
                    )
                else:
                    hook.logging_level(
                        "\\t" * hook.tabs
                        + f"[{self.__class__.__name__}] Kwarg {key}: {type(value)}"
                    )

            hook.tabs += 1
            # Call the original forward function
            output = original_forward(self, *args, **kwargs)
            hook.tabs -= 1
            # Print output information
            if hasattr(output, "shape"):
                hook.logging_level(
                    "\\t" * hook.tabs
                    + f"[{self.__class__.__name__}] Output: {type(output)} {output.shape}"
                )
            else:
                hook.logging_level(
                    "\\t" * hook.tabs
                    + f"[{self.__class__.__name__}] Output: {type(output)}"
                )
            hook.logging_level(
                "\\t" * hook.tabs + f"[<<<][{hook.fc}][{self.__class__.__name__}]"
            )

            return output

        return new_forward
