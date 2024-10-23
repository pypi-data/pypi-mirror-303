# AIVM

This guide will walk you through the process of running AIVM locally on your machine, with Docker, Docker Compose, and AWS. Each method allows you to set up a multi-node environment for private inference.

## Table of Contents

- [Running AIVM Locally](#running-aivm-locally)
  - [Using Poetry](#using-poetry)
- [Running AIVM with Docker](#running-aivm-with-docker)
- [Running AIVM with Docker Compose](#running-aivm-with-docker-compose)
- [Running AIVM on AWS](#running-aivm-on-aws)

---

## Running AIVM Locally

### Using Poetry

To run AIVM locally with separate nodes, follow the steps below. Ensure [Poetry](https://python-poetry.org/) is installed on your machine.

1. **Generate the Configuration**  
   First, generate the necessary configuration files for the run:

   ```bash
   cd aivm
   poetry install
   poetry run aivm_config_gen aivm-config/aivm_config/launch_config/localhost.yaml --prefix localhost --output_dir /tmp/
   ```

2. **Start the Nodes and TTP**  
   Open multiple terminal windows and run the following commands in each shell:

   - **Shell 1: Start Node 0**

     ```bash
     poetry run aivm_node --node_config /tmp/localhost_node_0_config.yaml
     ```

   - **Shell 2: Start Node 1**

     ```bash
     poetry run aivm_node --node_config /tmp/localhost_node_1_config.yaml
     ```

   - **Shell 3: Start the TTP**

     ```bash
     poetry run aivm_ttp --node_config /tmp/localhost_ttp_config.yaml
     ```

   - **Shell 4 (and beyond): Run the Client**

     ```bash
     poetry run aivm_client --config /tmp/localhost_client_config.yaml --num_requests 2
     ```

---

## Running AIVM with Docker

If you prefer using Docker, follow these steps to build and run AIVM in Docker containers.

1. **Build the Docker Images**

   Navigate to the Docker folder and build all required images:

   ```bash
   cd aivm/docker
   docker build --target coordinator -t aivm-coordinator -f Dockerfile .. \
   && docker build --target node -t aivm-node -f Dockerfile .. \
   && docker build --target ttp -t aivm-ttp -f Dockerfile .. \
   && docker build --target client -t aivm-client -f Dockerfile ..
   ```

2. **Run the Containers**

   Open separate terminal windows for each container and run the following commands:

   - **Shell 1: Start the Coordinator**

     ```bash
     docker run -it --rm --net host aivm-coordinator
     ```

   - **Shell 2: Start the Node**

     ```bash
     docker run -it --rm --net host aivm-node
     ```

   - **Shell 3: Start the TTP**

     ```bash
     docker run -it --rm --net host aivm-ttp
     ```

   - **Shell 4: Start the Client**

     ```bash
     docker run -it --rm --net host aivm-client
     ```

---

## Running AIVM with Docker Compose

Docker Compose simplifies running multiple services in Docker. Follow these steps to run AIVM with Docker Compose.

1. **Run Docker Compose**

   Ensure Docker and Docker Compose are installed on your machine. Then, run the following command to spin up the AIVM components:

   ```bash
   docker compose up --build master worker-1 ttp client
   ```

---

## Running AIVM on AWS

To run AIVM on AWS, ensure that all necessary ports are open between the AWS instances. AIVM uses Gloo for communication, which requires multiple port connections.

1. **Modify the AWS Configuration**

   Update the configuration file `aivm/aws/config/aws.yaml` with the correct IP addresses for your AWS nodes.

2. **Generate the Configuration**

   Run the following commands to generate the configuration for the AWS environment:

   ```bash
   cd aivm
   poetry install
   poetry run aivm_config_gen aivm-config/aivm_config/launch_config/aws.yaml --prefix aws --output_dir /tmp/
   ```

3. **Run the Nodes and TTP**

   Open multiple terminal windows and run the following commands on your AWS instances:

   - **Shell 1: Start Node 0**

     ```bash
     poetry run aivm_node --node_config /tmp/aws_node_0_config.yaml
     ```

   - **Shell 2: Start Node 1**

     ```bash
     poetry run aivm_node --node_config /tmp/aws_node_1_config.yaml
     ```

   - **Shell 3: Start the TTP**

     ```bash
     poetry run aivm_ttp --node_config /tmp/aws_ttp_config.yaml
     ```

   - **Shell 4 (and beyond): Run the Client**

     ```bash
     poetry run aivm_client --config /tmp/aws_client_config.yaml --num_requests 2
     ```
