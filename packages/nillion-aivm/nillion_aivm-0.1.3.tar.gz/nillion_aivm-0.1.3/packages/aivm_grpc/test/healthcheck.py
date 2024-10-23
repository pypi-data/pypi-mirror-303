import argparse
import logging
import sys

import grpc


def check_grpc_health(host):
    try:
        print(f"Checking the health of gRPC service at {host}")
        # Create a channel and attempt to connect
        with grpc.insecure_channel(host) as channel:
            # Perform a connectivity check
            if grpc.channel_ready_future(channel).result(timeout=5):
                sys.exit(0)
    except grpc.FutureTimeoutError as e:
        # Connection timed out, server might not be running
        print(f"Connection timed out: {e}", file=sys.stderr)
        sys.exit(-1)
    except Exception as e:
        # Handle other exceptions (e.g., network errors)
        print(f"An error occurred: {e}", file=sys.stderr)
        sys.exit(-1)

    print("Healthcheck success")


def main():
    parser = argparse.ArgumentParser(description="Check the health of a gRPC service")
    parser.add_argument(
        "--host",
        type=str,
        default="localhost:50051",
        help="The address of the gRPC service",
    )
    args = parser.parse_args()
    check_grpc_health(args.host)


if __name__ == "__main__":
    main()
