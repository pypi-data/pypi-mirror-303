import asyncio
from concurrent import futures
from typing import Dict, List

import grpc
from aivm_grpc import share_service_pb2 as sspb2
from aivm_grpc import share_service_pb2_grpc as ssgrpc
from google.protobuf.empty_pb2 import Empty


class ProxyServicer(ssgrpc.ProxyServicer):
    def __init__(self, server_addresses: List[str]):
        self.server_addresses = server_addresses
        self.lock = asyncio.Lock()
        self.channels: Dict[str, grpc.aio.Channel] = {}
        self.share_stubs: Dict[str, ssgrpc.ShareStub] = {}
        self.model_stubs: Dict[str, ssgrpc.ModelStub] = {}

    async def start(self):
        """Initialize all channels and stubs."""
        for address in self.server_addresses:
            self.channels[address] = grpc.aio.insecure_channel(address)
            self.share_stubs[address] = ssgrpc.ShareStub(self.channels[address])
            self.model_stubs[address] = ssgrpc.ModelStub(self.channels[address])

    async def stop(self):
        """Properly close all channels."""
        for channel in self.channels.values():
            await channel.close()

    async def GetServerConfiguration(
        self, request: Empty, context
    ) -> sspb2.ServerConfiguration:
        # Get configuration from the first server (assuming all servers have same config)
        print("GetServerConfiguration")
        first_server = self.server_addresses[0]
        try:
            return await self.share_stubs[first_server].GetServerConfiguration(Empty())
        except grpc.RpcError as e:
            context.set_code(e.code())
            context.set_details(e.details())
            raise

    async def GetPrediction(
        self, request: sspb2.ClientShares, context
    ) -> sspb2.ClientShares:
        # Distribute shares across servers
        tasks = []
        print("GetPrediction")
        # Create tasks for each server that needs to process shares
        for i, address in enumerate(self.server_addresses):
            if i < len(request.shares):
                tasks.append(self.share_stubs[address].GetPrediction(request.shares[i]))

        try:
            # Locking only the critical part that could have concurrent access
            async with self.lock:
                # Wait for all predictions and combine results
                results = await asyncio.gather(*tasks)
            response = sspb2.ClientShares()
            for result in results:
                response.shares.append(result)
            return response
        except grpc.RpcError as e:
            context.set_code(e.code())
            context.set_details(e.details())
            raise

    async def GetPreprocessing(
        self, request: sspb2.PreprocessingRequest, context
    ) -> Empty:
        print("GetPreprocessing")
        # Send preprocessing request to all servers
        tasks = []
        for address in self.server_addresses:
            tasks.append(self.share_stubs[address].GetPreprocessing(request))

        try:
            # Locking only the critical part that could have concurrent access
            async with self.lock:
                # Wait for all predictions and combine results
                await asyncio.gather(*tasks)
            return Empty()
        except grpc.RpcError as e:
            context.set_code(e.code())
            context.set_details(e.details())
            raise

    async def SendModel(self, request_iterator, context):
        # Forward model chunks to all servers
        tasks = []
        print("SendModel")

        async def forward_chunks(address):
            async def chunk_generator():
                # Create a buffer to store chunks
                chunks = []
                async for chunk in request_iterator:
                    chunks.append(chunk)
                    yield chunk
                # Replay chunks for other servers
                for chunk in chunks:
                    yield chunk

            return await self.model_stubs[address].SendModel(chunk_generator())

        # Create tasks for all servers
        for address in self.server_addresses:
            tasks.append(forward_chunks(address))

        try:
            # Wait for all servers to process the model
            results = await asyncio.gather(*tasks)
            # Return response from the first server
            return results[0]
        except grpc.RpcError as e:
            context.set_code(e.code())
            context.set_details(e.details())
            return Empty()


class ProxyServer:
    def __init__(self, server_addresses: List[str], proxy_addr: str, proxy_port: int):
        self.server_addresses = server_addresses
        self.proxy_addr = proxy_addr
        self.proxy_port = proxy_port
        self.server = grpc.aio.server(futures.ThreadPoolExecutor(max_workers=10))
        self.servicer = ProxyServicer(server_addresses)

    async def start(self):
        """Start the proxy server."""
        await self.servicer.start()
        ssgrpc.add_ProxyServicer_to_server(self.servicer, self.server)
        listen_addr = f"{self.proxy_addr}:{self.proxy_port}"
        self.server.add_insecure_port(listen_addr)
        await self.server.start()
        print(f"Proxy server listening on {listen_addr}")

    async def stop(self):
        """Stop the proxy server and cleanup resources."""
        print("Stopping proxy server...")
        await self.servicer.stop()
        await self.server.stop(grace=5)  # Allow 5 seconds for graceful shutdown
        print("Proxy server stopped.")


async def run_server():

    server = ProxyServer(["localhost:50051"], "localhost", "50050")

    await server.start()

    try:
        await asyncio.Future()  # Run forever
    except asyncio.CancelledError:
        pass
    finally:
        await server.stop()


def main():
    try:
        asyncio.run(run_server())
    except KeyboardInterrupt:
        print("Server shutdown due to keyboard interrupt.")


if __name__ == "__main__":
    main()
