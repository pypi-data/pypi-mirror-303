### Recreating GRPCs:

```shell
poetry run python3 -m grpc_tools.protoc -I. --python_out=. --grpc_python_out=. aivm_grpc/share_service.proto
```


### Testing Network:

```shell
# On Shell 1
python3 aivm_grpc/test/server.py
```

```shell
# On Shell 2
python3 aivm_grpc/test/client.py
```

