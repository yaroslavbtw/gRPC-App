import app_pb2
import app_pb2_grpc
import grpc


def run():
    with grpc.insecure_channel('localhost:50052') as channel:
        stub = app_pb2_grpc.UsersStub(channel)
        response = stub.GetUsers(app_pb2.GetUsersRequest())
        print(response)


if __name__ == "__main__":
    run()
