# Генерация кода сгенерирована сервером плагинов gRPC Python.
"""Client and server classes corresponding to protobuf-defined services."""
import grpc

from . import glossary_pb2 as glossary__pb2


class GlossaryServiceStub(object):
    """Missing associated documentation comment in .proto file."""

    def __init__(self, channel):
        """Constructor.

        Args:
            channel: A grpc.Channel.
        """
        self.GetAllTerms = channel.unary_unary(
                '/glossary.GlossaryService/GetAllTerms',
                request_serializer=glossary__pb2.GetAllTermsRequest.SerializeToString,
                response_deserializer=glossary__pb2.GetAllTermsResponse.FromString,
                )
        self.GetTermById = channel.unary_unary(
                '/glossary.GlossaryService/GetTermById',
                request_serializer=glossary__pb2.GetTermByIdRequest.SerializeToString,
                response_deserializer=glossary__pb2.TermResponse.FromString,
                )
        self.GetTermByName = channel.unary_unary(
                '/glossary.GlossaryService/GetTermByName',
                request_serializer=glossary__pb2.GetTermByNameRequest.SerializeToString,
                response_deserializer=glossary__pb2.TermResponse.FromString,
                )
        self.SearchTerms = channel.unary_unary(
                '/glossary.GlossaryService/SearchTerms',
                request_serializer=glossary__pb2.SearchTermsRequest.SerializeToString,
                response_deserializer=glossary__pb2.SearchTermsResponse.FromString,
                )
        self.CreateTerm = channel.unary_unary(
                '/glossary.GlossaryService/CreateTerm',
                request_serializer=glossary__pb2.CreateTermRequest.SerializeToString,
                response_deserializer=glossary__pb2.TermResponse.FromString,
                )
        self.UpdateTerm = channel.unary_unary(
                '/glossary.GlossaryService/UpdateTerm',
                request_serializer=glossary__pb2.UpdateTermRequest.SerializeToString,
                response_deserializer=glossary__pb2.TermResponse.FromString,
                )
        self.DeleteTerm = channel.unary_unary(
                '/glossary.GlossaryService/DeleteTerm',
                request_serializer=glossary__pb2.DeleteTermRequest.SerializeToString,
                response_deserializer=glossary__pb2.DeleteResponse.FromString,
                )
        self.GetStats = channel.unary_unary(
                '/glossary.GlossaryService/GetStats',
                request_serializer=glossary__pb2.Empty.SerializeToString,
                response_deserializer=glossary__pb2.StatsResponse.FromString,
                )
        self.GetCategories = channel.unary_unary(
                '/glossary.GlossaryService/GetCategories',
                request_serializer=glossary__pb2.Empty.SerializeToString,
                response_deserializer=glossary__pb2.CategoriesResponse.FromString,
                )
        self.GetRelatedTerms = channel.unary_unary(
                '/glossary.GlossaryService/GetRelatedTerms',
                request_serializer=glossary__pb2.GetRelatedTermsRequest.SerializeToString,
                response_deserializer=glossary__pb2.RelatedTermsResponse.FromString,
                )


class GlossaryServiceServicer(object):
    """Missing associated documentation comment in .proto file."""

    def GetAllTerms(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def GetTermById(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def GetTermByName(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def SearchTerms(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def CreateTerm(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def UpdateTerm(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def DeleteTerm(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def GetStats(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def GetCategories(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def GetRelatedTerms(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')


def add_GlossaryServiceServicer_to_server(servicer, server):
    rpc_method_handlers = {
            'GetAllTerms': grpc.unary_unary_rpc_method_handler(
                    servicer.GetAllTerms,
                    request_deserializer=glossary__pb2.GetAllTermsRequest.FromString,
                    response_serializer=glossary__pb2.GetAllTermsResponse.SerializeToString,
            ),
            'GetTermById': grpc.unary_unary_rpc_method_handler(
                    servicer.GetTermById,
                    request_deserializer=glossary__pb2.GetTermByIdRequest.FromString,
                    response_serializer=glossary__pb2.TermResponse.SerializeToString,
            ),
            'GetTermByName': grpc.unary_unary_rpc_method_handler(
                    servicer.GetTermByName,
                    request_deserializer=glossary__pb2.GetTermByNameRequest.FromString,
                    response_serializer=glossary__pb2.TermResponse.SerializeToString,
            ),
            'SearchTerms': grpc.unary_unary_rpc_method_handler(
                    servicer.SearchTerms,
                    request_deserializer=glossary__pb2.SearchTermsRequest.FromString,
                    response_serializer=glossary__pb2.SearchTermsResponse.SerializeToString,
            ),
            'CreateTerm': grpc.unary_unary_rpc_method_handler(
                    servicer.CreateTerm,
                    request_deserializer=glossary__pb2.CreateTermRequest.FromString,
                    response_serializer=glossary__pb2.TermResponse.SerializeToString,
            ),
            'UpdateTerm': grpc.unary_unary_rpc_method_handler(
                    servicer.UpdateTerm,
                    request_deserializer=glossary__pb2.UpdateTermRequest.FromString,
                    response_serializer=glossary__pb2.TermResponse.SerializeToString,
            ),
            'DeleteTerm': grpc.unary_unary_rpc_method_handler(
                    servicer.DeleteTerm,
                    request_deserializer=glossary__pb2.DeleteTermRequest.FromString,
                    response_serializer=glossary__pb2.DeleteResponse.SerializeToString,
            ),
            'GetStats': grpc.unary_unary_rpc_method_handler(
                    servicer.GetStats,
                    request_deserializer=glossary__pb2.Empty.FromString,
                    response_serializer=glossary__pb2.StatsResponse.SerializeToString,
            ),
            'GetCategories': grpc.unary_unary_rpc_method_handler(
                    servicer.GetCategories,
                    request_deserializer=glossary__pb2.Empty.FromString,
                    response_serializer=glossary__pb2.CategoriesResponse.SerializeToString,
            ),
            'GetRelatedTerms': grpc.unary_unary_rpc_method_handler(
                    servicer.GetRelatedTerms,
                    request_deserializer=glossary__pb2.GetRelatedTermsRequest.FromString,
                    response_serializer=glossary__pb2.RelatedTermsResponse.SerializeToString,
            ),
    }
    generic_handler = grpc.method_handlers_generic_handler(
            'glossary.GlossaryService', rpc_method_handlers)
    server.add_generic_rpc_handlers((generic_handler,))