### grpc hello world

A hello world example, let python client communicate with nodejs server.

### usage
1. generate code from `.proto`
```sh
env -C packages/generated-helloworld make
```

2. start nodejs server
```sh
env -C packages/nodejs-server make
```

2. start python client
```sh
env -C packages/python-client make
```
