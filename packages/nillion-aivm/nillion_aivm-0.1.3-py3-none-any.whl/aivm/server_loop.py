import logging

import curl
import curl.communicator as comm
import torch
from curl.config import cfg

from aivm.benchmark import CSVLogger
from aivm.models import CNNs, ONNXModels, Utils


def run_llm(
    cfg_dict,
    aivm_servicer,
    world_size,
    rank,
    communication=False,
    device=None,
):
    # First cold run.
    curl.init(cfg_dict=cfg_dict, device=device, world_size=world_size, rank=rank)
    if world_size == rank:
        return  # Only doing the initialization

    csv_logger = CSVLogger(f"/tmp/runtimes_{rank}.csv")
    if communication:
        comm.get().set_verbosity(True)

    functions_data = cfg.config.get("functions", {})
    filtered_data = {
        key: value for key, value in functions_data.items() if "_method" in key
    }
    logging.debug("\t'{}'".format(filtered_data))

    cnns = CNNs(device=device)
    utils = Utils(device=device)  # Used to prevent timeouts
    onnx = ONNXModels(device=device)

    prep_manager = aivm_servicer.client_servicer.preprocessing_manager
    try:
        logging.info("[READY] Started server loop")
        while True:

            logging.debug("Waiting for a request...")
            request, preprocessing = aivm_servicer.client_servicer.get_request(
                timeout=5
            )

            new_model_request = aivm_servicer.model_servicer.get_model_upload()
            while new_model_request:
                if new_model_request[1] == "LeNet5":
                    cnns.new_model(
                        model_name=new_model_request[0],
                        model_type=new_model_request[1],
                        model_path=new_model_request[2],
                    )
                elif new_model_request[1] == "BertTiny":
                    onnx.new_model(
                        model_name=new_model_request[0],
                        model_type=new_model_request[1],
                        model_path=new_model_request[2],
                    )
                else:
                    logging.error(f"Model type {new_model_request[1]} not supported")

                logging.info(
                    f"[Party {rank}] Done integrating uploaded models: {new_model_request[0]} of type {new_model_request[1]}"
                )
                new_model_request = aivm_servicer.model_servicer.get_model_upload()

            if request is None:
                # No preprocessing to do
                continue
            shares = request[0]
            model = request[1]
            model_type = request[2]
            logging.info(
                f"[{'🧪' if preprocessing else '🏃'}] Model: {model}, Model Type: {model_type}, Shape: {shares.shape}"
            )
            with prep_manager.set_mode(model, model_type, preprocessing):
                if model in cnns.models:
                    handler = cnns
                elif model in utils.models:
                    handler = utils
                elif model in onnx.models:
                    handler = onnx

                result, runtime = handler.run(model, shares)
                csv_logger.log(
                    model, runtime, preprocessing, prep_manager.use_preprocessing
                )
                aivm_servicer.client_servicer.add_response(result.share)
                logging.debug("=" * 60 + f"\n{handler}\n" + "=" * 60)

            logging.debug("=" * 60 + f"\n{prep_manager}\n" + "=" * 60)
    except KeyboardInterrupt:
        logging.debug(f"Party {rank} got KeyboardInterrupt")
        if communication:
            comm.get().print_communication_stats()
            exit(0)

        logging.info(f"[Party {rank}] Shutting down server...")
        curl.uninit()  # End communication
        aivm_servicer.stop()
