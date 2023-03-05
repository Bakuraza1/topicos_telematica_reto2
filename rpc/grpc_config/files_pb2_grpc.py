# Generated by the gRPC Python protocol compiler plugin. DO NOT EDIT!
"""Client and server classes corresponding to protobuf-defined services."""
import grpc

from . import files_pb2 as files__pb2


class getFilesStub(object):
    """Missing associated documentation comment in .proto file."""

    def __init__(self, channel):
        """Constructor.

        Args:
            channel: A grpc.Channel.
        """
        self.Ready = channel.unary_unary(
                '/getFiles/Ready',
                request_serializer=files__pb2.Nulo.SerializeToString,
                response_deserializer=files__pb2.Nulo.FromString,
                )
        self.ListFiles = channel.unary_unary(
                '/getFiles/ListFiles',
                request_serializer=files__pb2.Nulo.SerializeToString,
                response_deserializer=files__pb2.Files.FromString,
                )
        self.FindFiles = channel.unary_unary(
                '/getFiles/FindFiles',
                request_serializer=files__pb2.Files.SerializeToString,
                response_deserializer=files__pb2.Files.FromString,
                )


class getFilesServicer(object):
    """Missing associated documentation comment in .proto file."""

    def Ready(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def ListFiles(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def FindFiles(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')


def add_getFilesServicer_to_server(servicer, server):
    rpc_method_handlers = {
            'Ready': grpc.unary_unary_rpc_method_handler(
                    servicer.Ready,
                    request_deserializer=files__pb2.Nulo.FromString,
                    response_serializer=files__pb2.Nulo.SerializeToString,
            ),
            'ListFiles': grpc.unary_unary_rpc_method_handler(
                    servicer.ListFiles,
                    request_deserializer=files__pb2.Nulo.FromString,
                    response_serializer=files__pb2.Files.SerializeToString,
            ),
            'FindFiles': grpc.unary_unary_rpc_method_handler(
                    servicer.FindFiles,
                    request_deserializer=files__pb2.Files.FromString,
                    response_serializer=files__pb2.Files.SerializeToString,
            ),
    }
    generic_handler = grpc.method_handlers_generic_handler(
            'getFiles', rpc_method_handlers)
    server.add_generic_rpc_handlers((generic_handler,))


 # This class is part of an EXPERIMENTAL API.
class getFiles(object):
    """Missing associated documentation comment in .proto file."""

    @staticmethod
    def Ready(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/getFiles/Ready',
            files__pb2.Nulo.SerializeToString,
            files__pb2.Nulo.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def ListFiles(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/getFiles/ListFiles',
            files__pb2.Nulo.SerializeToString,
            files__pb2.Files.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def FindFiles(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/getFiles/FindFiles',
            files__pb2.Files.SerializeToString,
            files__pb2.Files.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)
