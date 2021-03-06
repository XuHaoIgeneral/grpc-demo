# Generated by the gRPC Python protocol compiler plugin. DO NOT EDIT!
import grpc

from . import auth_pb2 as auth__pb2


class AUTHStub(object):
  """定义可以被远程调用的函数
  """

  def __init__(self, channel):
    """Constructor.

    Args:
      channel: A grpc.Channel.
    """
    self.AuthLogin = channel.stream_stream(
        '/auth.AUTH/AuthLogin',
        request_serializer=auth__pb2.Request.SerializeToString,
        response_deserializer=auth__pb2.Response.FromString,
        )


class AUTHServicer(object):
  """定义可以被远程调用的函数
  """

  def AuthLogin(self, request_iterator, context):
    # missing associated documentation comment in .proto file
    pass
    context.set_code(grpc.StatusCode.UNIMPLEMENTED)
    context.set_details('Method not implemented!')
    raise NotImplementedError('Method not implemented!')


def add_AUTHServicer_to_server(servicer, server):
  rpc_method_handlers = {
      'AuthLogin': grpc.stream_stream_rpc_method_handler(
          servicer.AuthLogin,
          request_deserializer=auth__pb2.Request.FromString,
          response_serializer=auth__pb2.Response.SerializeToString,
      ),
  }
  generic_handler = grpc.method_handlers_generic_handler(
      'auth.AUTH', rpc_method_handlers)
  server.add_generic_rpc_handlers((generic_handler,))
