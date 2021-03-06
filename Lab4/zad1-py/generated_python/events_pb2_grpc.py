# Generated by the gRPC Python protocol compiler plugin. DO NOT EDIT!
import grpc

import events_pb2 as events__pb2


class EventsServiceStub(object):
    """Missing associated documentation comment in .proto file"""

    def __init__(self, channel):
        """Constructor.

        Args:
            channel: A grpc.Channel.
        """
        self.Subscribe = channel.stream_stream(
                '/events.EventsService/Subscribe',
                request_serializer=events__pb2.TypeArg.SerializeToString,
                response_deserializer=events__pb2.Data.FromString,
                )


class EventsServiceServicer(object):
    """Missing associated documentation comment in .proto file"""

    def Subscribe(self, request_iterator, context):
        """Missing associated documentation comment in .proto file"""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')


def add_EventsServiceServicer_to_server(servicer, server):
    rpc_method_handlers = {
            'Subscribe': grpc.stream_stream_rpc_method_handler(
                    servicer.Subscribe,
                    request_deserializer=events__pb2.EventTypeArgument.FromString,
                    response_serializer=events__pb2.Data.SerializeToString,
            ),
    }
    generic_handler = grpc.method_handlers_generic_handler(
            'events.EventsService', rpc_method_handlers)
    server.add_generic_rpc_handlers((generic_handler,))


 # This class is part of an EXPERIMENTAL API.
class EventsService(object):
    """Missing associated documentation comment in .proto file"""

    @staticmethod
    def Subscribe(request_iterator,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.stream_stream(request_iterator, target, '/events.EventsService/Subscribe',
            events__pb2.EventTyeArgument.SerializeToString,
            events__pb2.EventInfo.FromString,
            options, channel_credentials,
            call_credentials, compression, wait_for_ready, timeout, metadata)
