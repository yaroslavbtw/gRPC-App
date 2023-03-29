import grpc
import app_pb2
import app_pb2_grpc
from concurrent import futures


def run():
    with grpc.insecure_channel('0.0.0.0:50052') as channel:
        stub = app_pb2_grpc.SquareRootServiceStub(channel)
        response = stub.squareRoot(app_pb2.Number(input=int(input())))
        print(response.res)


if __name__ == '__main__':
    run()
