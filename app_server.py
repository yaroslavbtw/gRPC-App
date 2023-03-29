import grpc
import app_pb2
import app_pb2_grpc
from concurrent import futures


class SquareRootServiceServicer(app_pb2_grpc.SquareRootServiceServicer):
    def squareRoot(self, request, context):
        res = request.input * request.input
        return app_pb2.Result(res=res)


def main():
    server = grpc.server(futures.ThreadPoolExecutor(max_workers=10))
    app_pb2_grpc.add_SquareRootServiceServicer_to_server(SquareRootServiceServicer(), server=server)
    server.add_insecure_port('[::]:50052')
    server.start()
    print("Server is running")
    server.wait_for_termination()


if __name__ == '__main__':
    main()
