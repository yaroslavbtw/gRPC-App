import app_pb2
import app_pb2_grpc
import grpc
from concurrent import futures


class Users(app_pb2_grpc.UsersServicer):

    def GetUsers(self, request, context):
        return app_pb2.GetUsersResponse(users=[
            app_pb2.User(id='1', name='John Doe', email='abobus@gmail.com', password='12345678'),
            app_pb2.User(id='2', name='Artur Kek', email='kek@gmail.com', password='87654321'),
        ])

    def GetUserById(self, request, context):
        return app_pb2.GetUserByIdResponse(users=app_pb2.User(id='1', name='John Doe', email='abobus@gmail.com',
                                                              password='12345678'))


def serve():
    server = grpc.server(futures.ThreadPoolExecutor(max_workers=10))
    app_pb2_grpc.add_UsersServicer_to_server(Users(), server)
    server.add_insecure_port('[::]:50052')
    server.start()
    server.wait_for_termination()


if __name__ == '__main__':
    serve()
