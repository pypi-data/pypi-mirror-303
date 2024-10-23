import argparse
import os

import yaml

from aivm_config.global_config import AIVMGlobalConfig, cfg
from aivm_config.launch_config_gen import (generate_all_configs,
                                           generate_client_config,
                                           generate_nodes_config,
                                           generate_proxy_config, save_configs)

__all__ = [
    "AIVMGlobalConfig",
    "cfg",
    "generate_nodes_config",
    "generate_client_config",
    "generate_proxy_config",
    "generate_all_configs",
    "save_configs",
    "default_config",
]

default_config = {
    "world_size": 2,
    "node_addr": ["localhost", "localhost", "localhost"],
    "coordinator_port": 12345,
    "grpc_client_ports": [50051, 50052],
    "proxy_addr": "localhost",
    "proxy_port": 50050,
}


def main():
    parser = argparse.ArgumentParser(
        description="Generate configuration files for nodes."
    )
    parser.add_argument(
        "base_config_filename",
        type=str,
        help="Path to the base YAML config file (e.g., aivm/config/base.yaml)",
    )
    parser.add_argument(
        "--prefix",
        type=str,
        help="Prefix to add to the generated configuration files",
        default="",
    )
    parser.add_argument(
        "--output_dir",
        type=str,
        help="Directory to save the generated configuration files",
        default="",
    )
    args = parser.parse_args()

    # Load the base config file
    with open(args.base_config_filename, "r") as f:
        global_config = yaml.safe_load(f)

    # Generate all configurations
    configs = generate_all_configs(global_config)

    # Determine the output directory
    output_dir = (
        args.output_dir
        if args.output_dir
        else os.path.dirname(args.base_config_filename)
    )
    output_dir = os.path.abspath(output_dir)

    # Save the configurations to files
    save_configs(configs, output_dir, args.prefix)

    print("Configuration files generated.")


if __name__ == "__main__":
    main()
