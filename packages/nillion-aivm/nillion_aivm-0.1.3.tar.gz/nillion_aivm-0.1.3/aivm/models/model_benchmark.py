import functools
import logging
import timeit
from collections import namedtuple

import curl
import curl.communicator as comm
import numpy as np
import pandas as pd
import torch
import torch.optim
import torch.utils.data
import torch.utils.data.distributed

Runtime = namedtuple("Runtime", "mid q1 q3")


def time_me(func=None, n_loops=1):
    """Decorator returning average runtime in seconds over n_loops

    Args:
        func (function): invoked with given args / kwargs
        n_loops (int): number of times to invoke function for timing

    Returns: tuple of (time in seconds, inner quartile range, function return value).
    """
    if func is None:
        return functools.partial(time_me, n_loops=n_loops)

    @functools.wraps(func)
    def timing_wrapper(*args, **kwargs):
        times = []
        for _ in range(n_loops):
            start = timeit.default_timer()
            return_val = func(*args, **kwargs)
            times.append(timeit.default_timer() - start)
        mid_runtime = np.quantile(times, 0.5)
        q1_runtime = np.quantile(times, 0.25)
        q3_runtime = np.quantile(times, 0.75)
        runtime = Runtime(mid_runtime, q1_runtime, q3_runtime)
        return runtime, return_val

    return timing_wrapper


class BaseModelBenchmark:
    def __init__(self, device="cpu"):
        self.device = torch.device(device)
        self.models = {}
        self.df = None

    def __repr__(self):
        if self.df is not None:
            return self.df.to_string(index=False, justify="left")
        return "No Function Benchmarks"

    @staticmethod
    @time_me
    def time_llm(x, model):
        return model(x)

    def get_inference_result(self, model_name, inputs):
        """Runs the inference on a model and returns the results"""
        model_name = model_name
        model = self.models[model_name]
        rank = comm.get().get_rank()
        logging.debug(f"[Device] Party-{rank} running in {self.device}")

        model.eval()
        runtime_enc, return_val = self.time_llm(inputs, model)
        logging.debug(f"Runtime: {runtime_enc}")

        return [runtime_enc], return_val

    def run(self, model_name, inputs):
        """Runs and stores benchmarks in self.df and logs to CSV"""
        curl.load_luts(model_name)
        runtimes_enc, return_val = self.get_inference_result(model_name, inputs)

        self.df = pd.DataFrame.from_dict(
            {
                "function": model_name,
                "runtime": [r.mid for r in runtimes_enc],
            }
        )
        return return_val, runtimes_enc[0]
