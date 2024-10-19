# Generated by the gRPC Python protocol compiler plugin. DO NOT EDIT!
"""Client and server classes corresponding to protobuf-defined services."""
import grpc
import warnings

from . import hal_pb_pb2 as hal__pb__pb2

GRPC_GENERATED_VERSION = '1.67.0'
GRPC_VERSION = grpc.__version__
_version_not_supported = False

try:
    from grpc._utilities import first_version_is_lower
    _version_not_supported = first_version_is_lower(GRPC_VERSION, GRPC_GENERATED_VERSION)
except ImportError:
    _version_not_supported = True

if _version_not_supported:
    raise RuntimeError(
        f'The grpc package installed is at version {GRPC_VERSION},'
        + f' but the generated code in hal_pb_pb2_grpc.py depends on'
        + f' grpcio>={GRPC_GENERATED_VERSION}.'
        + f' Please upgrade your grpc module to grpcio>={GRPC_GENERATED_VERSION}'
        + f' or downgrade your generated code using grpcio-tools<={GRPC_VERSION}.'
    )


class ServoControlStub(object):
    """Missing associated documentation comment in .proto file."""

    def __init__(self, channel):
        """Constructor.

        Args:
            channel: A grpc.Channel.
        """
        self.GetPositions = channel.unary_unary(
                '/hal_pb.ServoControl/GetPositions',
                request_serializer=hal__pb__pb2.Empty.SerializeToString,
                response_deserializer=hal__pb__pb2.JointPositions.FromString,
                _registered_method=True)
        self.SetPositions = channel.unary_unary(
                '/hal_pb.ServoControl/SetPositions',
                request_serializer=hal__pb__pb2.JointPositions.SerializeToString,
                response_deserializer=hal__pb__pb2.Empty.FromString,
                _registered_method=True)
        self.SetWifiInfo = channel.unary_unary(
                '/hal_pb.ServoControl/SetWifiInfo',
                request_serializer=hal__pb__pb2.WifiCredentials.SerializeToString,
                response_deserializer=hal__pb__pb2.Empty.FromString,
                _registered_method=True)
        self.GetServoInfo = channel.unary_unary(
                '/hal_pb.ServoControl/GetServoInfo',
                request_serializer=hal__pb__pb2.ServoId.SerializeToString,
                response_deserializer=hal__pb__pb2.ServoInfoResponse.FromString,
                _registered_method=True)
        self.Scan = channel.unary_unary(
                '/hal_pb.ServoControl/Scan',
                request_serializer=hal__pb__pb2.Empty.SerializeToString,
                response_deserializer=hal__pb__pb2.ServoIds.FromString,
                _registered_method=True)
        self.ChangeId = channel.unary_unary(
                '/hal_pb.ServoControl/ChangeId',
                request_serializer=hal__pb__pb2.IdChange.SerializeToString,
                response_deserializer=hal__pb__pb2.ChangeIdResponse.FromString,
                _registered_method=True)


class ServoControlServicer(object):
    """Missing associated documentation comment in .proto file."""

    def GetPositions(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def SetPositions(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def SetWifiInfo(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def GetServoInfo(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def Scan(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def ChangeId(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')


def add_ServoControlServicer_to_server(servicer, server):
    rpc_method_handlers = {
            'GetPositions': grpc.unary_unary_rpc_method_handler(
                    servicer.GetPositions,
                    request_deserializer=hal__pb__pb2.Empty.FromString,
                    response_serializer=hal__pb__pb2.JointPositions.SerializeToString,
            ),
            'SetPositions': grpc.unary_unary_rpc_method_handler(
                    servicer.SetPositions,
                    request_deserializer=hal__pb__pb2.JointPositions.FromString,
                    response_serializer=hal__pb__pb2.Empty.SerializeToString,
            ),
            'SetWifiInfo': grpc.unary_unary_rpc_method_handler(
                    servicer.SetWifiInfo,
                    request_deserializer=hal__pb__pb2.WifiCredentials.FromString,
                    response_serializer=hal__pb__pb2.Empty.SerializeToString,
            ),
            'GetServoInfo': grpc.unary_unary_rpc_method_handler(
                    servicer.GetServoInfo,
                    request_deserializer=hal__pb__pb2.ServoId.FromString,
                    response_serializer=hal__pb__pb2.ServoInfoResponse.SerializeToString,
            ),
            'Scan': grpc.unary_unary_rpc_method_handler(
                    servicer.Scan,
                    request_deserializer=hal__pb__pb2.Empty.FromString,
                    response_serializer=hal__pb__pb2.ServoIds.SerializeToString,
            ),
            'ChangeId': grpc.unary_unary_rpc_method_handler(
                    servicer.ChangeId,
                    request_deserializer=hal__pb__pb2.IdChange.FromString,
                    response_serializer=hal__pb__pb2.ChangeIdResponse.SerializeToString,
            ),
    }
    generic_handler = grpc.method_handlers_generic_handler(
            'hal_pb.ServoControl', rpc_method_handlers)
    server.add_generic_rpc_handlers((generic_handler,))
    server.add_registered_method_handlers('hal_pb.ServoControl', rpc_method_handlers)


 # This class is part of an EXPERIMENTAL API.
class ServoControl(object):
    """Missing associated documentation comment in .proto file."""

    @staticmethod
    def GetPositions(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(
            request,
            target,
            '/hal_pb.ServoControl/GetPositions',
            hal__pb__pb2.Empty.SerializeToString,
            hal__pb__pb2.JointPositions.FromString,
            options,
            channel_credentials,
            insecure,
            call_credentials,
            compression,
            wait_for_ready,
            timeout,
            metadata,
            _registered_method=True)

    @staticmethod
    def SetPositions(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(
            request,
            target,
            '/hal_pb.ServoControl/SetPositions',
            hal__pb__pb2.JointPositions.SerializeToString,
            hal__pb__pb2.Empty.FromString,
            options,
            channel_credentials,
            insecure,
            call_credentials,
            compression,
            wait_for_ready,
            timeout,
            metadata,
            _registered_method=True)

    @staticmethod
    def SetWifiInfo(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(
            request,
            target,
            '/hal_pb.ServoControl/SetWifiInfo',
            hal__pb__pb2.WifiCredentials.SerializeToString,
            hal__pb__pb2.Empty.FromString,
            options,
            channel_credentials,
            insecure,
            call_credentials,
            compression,
            wait_for_ready,
            timeout,
            metadata,
            _registered_method=True)

    @staticmethod
    def GetServoInfo(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(
            request,
            target,
            '/hal_pb.ServoControl/GetServoInfo',
            hal__pb__pb2.ServoId.SerializeToString,
            hal__pb__pb2.ServoInfoResponse.FromString,
            options,
            channel_credentials,
            insecure,
            call_credentials,
            compression,
            wait_for_ready,
            timeout,
            metadata,
            _registered_method=True)

    @staticmethod
    def Scan(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(
            request,
            target,
            '/hal_pb.ServoControl/Scan',
            hal__pb__pb2.Empty.SerializeToString,
            hal__pb__pb2.ServoIds.FromString,
            options,
            channel_credentials,
            insecure,
            call_credentials,
            compression,
            wait_for_ready,
            timeout,
            metadata,
            _registered_method=True)

    @staticmethod
    def ChangeId(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(
            request,
            target,
            '/hal_pb.ServoControl/ChangeId',
            hal__pb__pb2.IdChange.SerializeToString,
            hal__pb__pb2.ChangeIdResponse.FromString,
            options,
            channel_credentials,
            insecure,
            call_credentials,
            compression,
            wait_for_ready,
            timeout,
            metadata,
            _registered_method=True)
