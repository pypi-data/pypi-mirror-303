#!/usr/bin/env python3

import argparse
import glob
import logging
import multiprocessing
import os
import shutil
import signal

import curl
import yaml

from aivm.server import AIVMServicer
from aivm_config import generate_nodes_config
from aivm_config.logging import setup_logger


def load_config(config_path):
    with open(config_path, "r") as file:
        config = yaml.safe_load(file)
    return config


def _run_experiment(config, loop_fn, logging_level=logging.INFO):
    setup_logger(config["rank"], logging_level)

    os.environ["RENDEZVOUS"] = (
        f"tcp://{config['gloo_coordinator_addr']}:{config['gloo_coordinator_port']}"
    )

    aivm_servicer = None
    if not config.get("disable_client", False):
        aivm_servicer = AIVMServicer(
            precision=16,
            world_size=config["world_size"],
            rank=config["rank"],
            host=config["grpc_client_addr"],
            port=config["grpc_client_port"],
            nodes=config["gloo_nodes"],
            proxy=f"{config['proxy_addr']}:{config['proxy_port']}",
        )
        aivm_servicer.serve()

    cfg_dict = curl.config.CurlConfig.get_default_config()
    cfg_dict["mpc"]["provider"] = "TTP"
    loop_fn(
        cfg_dict,
        aivm_servicer,
        config["world_size"],
        config["rank"],
        device=config["device"],
    )

    if aivm_servicer:
        aivm_servicer.wait_to_end()


def main():
    from aivm.server_loop import run_llm

    # Set up argparse to receive the base config file as an argument
    parser = argparse.ArgumentParser(
        description="Generate configuration files for nodes."
    )
    parser.add_argument(
        "--node_config",
        type=str,
        help="Path to the YAML config file (e.g., aivm/config/node_1.yaml)",
    )
    args = parser.parse_args()
    config = load_config(args.node_config)
    logging.debug(f"Loaded config: {config}")
    _run_experiment(config, run_llm)


def devnet():
    from aivm.server_loop import run_llm
    from aivm_config import default_config
    from aivm_proxy import devnet_main

    # Argument parsing for optional ports
    parser = argparse.ArgumentParser(
        description="Start AIVM devnet with optional ports."
    )
    parser.add_argument(
        "--proxy-port",
        type=int,
        default=50050,
        help="Port for the proxy (default: 50050)",
    )
    parser.add_argument(
        "--coordinator-port",
        type=int,
        default=50051,
        help="Port for the coordinator (default: 50051)",
    )
    parser.add_argument(
        "--node-port",
        type=int,
        default=50052,
        help="Port for the node (default: 50052)",
    )

    args = parser.parse_args()

    initial_config = default_config.copy()

    initial_config["grpc_client_ports"][0] = args.coordinator_port
    initial_config["grpc_client_ports"][1] = args.node_port
    initial_config["proxy_port"] = args.proxy_port

    configs = generate_nodes_config(initial_config)

    # Create processes for running the experiments
    processes = []
    for config in configs.values():
        process = multiprocessing.Process(
            target=_run_experiment, args=(config, run_llm, logging.DEBUG)
        )
        processes.append(process)

    processes.append(
        multiprocessing.Process(target=devnet_main, args=(initial_config,))
    )

    # Start all processes
    for process in processes:
        process.start()

    def signal_handler(sig, frame):
        print("Interruption received. Stopping AIVM...")
        for process in processes:
            if process.is_alive():
                process.terminate()
        print("Waiting for all processes to finish...")
        for process in processes:
            process.join()

        print("Removing temporary files...")
        # Remove all temporary files in
        ## /tmp/cache-*.pth directories
        for directory in glob.glob("/tmp/cache-*.pth"):
            shutil.rmtree(directory, ignore_errors=True)
        ##  /tmp/*.onnx files
        for file in glob.glob("/tmp/*.onnx"):
            os.remove(file)
        print("AIVM stopped.")
        exit(0)

    # Set up the signal handler for graceful interruption
    signal.signal(signal.SIGINT, signal_handler)

    # Wait for all processes to finish
    for process in processes:
        process.join()


if __name__ == "__main__":
    main()
