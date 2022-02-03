import os
import sys

import grpc

basedir = os.path.abspath(os.path.dirname(sys.argv[0]))
sys.path.insert(
    0, os.path.join(basedir, "..", "generated-helloworld", "generated", "python")
)

import helloworld_pb2
import helloworld_pb2_grpc


def main():
    responses = []
    with grpc.insecure_channel("localhost:50051") as channel:
        stub = helloworld_pb2_grpc.GreeterStub(channel)
        for i in range(1000):
            response = stub.SayHello(helloworld_pb2.HelloRequest(name=f'user{i}'))
            responses.append(response)
    for response in responses:
        print("Greeter client received: " + response.message)


if __name__ == "__main__":
    main()
