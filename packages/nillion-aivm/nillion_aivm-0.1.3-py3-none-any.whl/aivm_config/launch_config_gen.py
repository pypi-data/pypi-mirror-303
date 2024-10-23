import os

import yaml


def generate_node_config(global_config, rank, world_size):
    config_dict = {
        "world_size": world_size,
        "device": "cpu",
        "rank": rank,
        "gloo_nodes": [],
        "gloo_coordinator_addr": global_config["node_addr"][0],
        "gloo_coordinator_port": global_config["coordinator_port"],
        "grpc_client_addr": "0.0.0.0",
        "grpc_client_port": -1,
        "disable_client": False,
        "proxy_addr": global_config["proxy_addr"],
        "proxy_port": global_config["proxy_port"],
    }

    config_dict["gloo_nodes"] = [
        f"{address}:{port}"
        for j, (address, port) in enumerate(
            zip(global_config["node_addr"], global_config["grpc_client_ports"])
        )
        if j != rank and j != world_size
    ]

    if rank == world_size:
        # Trusted third party
        config_dict["disable_client"] = True
    else:
        # Client
        config_dict["grpc_client_port"] = global_config["grpc_client_ports"][rank]

    return config_dict


def generate_client_config(global_config):
    return {
        "world_size": global_config["world_size"],
        "device": "cpu",
        "nodes": [
            f"{address}:{port}"
            for j, (address, port) in enumerate(
                zip(global_config["node_addr"], global_config["grpc_client_ports"])
            )
            if j != global_config["world_size"]
        ],
        "proxy_addr": global_config["proxy_addr"],
        "proxy_port": global_config["proxy_port"],
    }


def generate_nodes_config(global_config):
    configs = {}
    world_size = global_config["world_size"]

    for i in range(world_size + 1):
        config_name = f"ttp_config" if i == world_size else f"node_{i}_config"
        configs[config_name] = generate_node_config(global_config, i, world_size)

    return configs


def generate_proxy_config(global_config):
    return generate_client_config(global_config)


def generate_all_configs(global_config):
    configs = generate_nodes_config(global_config)
    configs["client_config"] = generate_client_config(global_config)
    configs["proxy_config"] = generate_proxy_config(global_config)
    return configs


def save_configs(configs, directory, prefix):
    if prefix and not prefix.endswith("_"):
        prefix += "_"

    for name, config in configs.items():
        filename = os.path.join(directory, f"{prefix}{name}.yaml")
        with open(filename, "w") as f:
            yaml.dump(config, f)
        print(f"Generated: {filename}")
