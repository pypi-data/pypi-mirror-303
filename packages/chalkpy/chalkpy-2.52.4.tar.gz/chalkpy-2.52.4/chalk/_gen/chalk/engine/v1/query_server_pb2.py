# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: chalk/engine/v1/query_server.proto
# Protobuf Python Version: 4.25.3
"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import symbol_database as _symbol_database
from google.protobuf.internal import builder as _builder
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


from chalk._gen.chalk.aggregate.v1 import service_pb2 as chalk_dot_aggregate_dot_v1_dot_service__pb2
from chalk._gen.chalk.auth.v1 import permissions_pb2 as chalk_dot_auth_dot_v1_dot_permissions__pb2
from chalk._gen.chalk.common.v1 import online_query_pb2 as chalk_dot_common_dot_v1_dot_online__query__pb2


DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(
    b'\n"chalk/engine/v1/query_server.proto\x12\x0f\x63halk.engine.v1\x1a chalk/aggregate/v1/service.proto\x1a\x1f\x63halk/auth/v1/permissions.proto\x1a"chalk/common/v1/online_query.proto"\x1f\n\x0bPingRequest\x12\x10\n\x03num\x18\x01 \x01(\x05R\x03num" \n\x0cPingResponse\x12\x10\n\x03num\x18\x01 \x01(\x05R\x03num2\xfc\x05\n\x0cQueryService\x12K\n\x04Ping\x12\x1c.chalk.engine.v1.PingRequest\x1a\x1d.chalk.engine.v1.PingResponse"\x06\x90\x02\x01\x80}\x01\x12]\n\x0bOnlineQuery\x12#.chalk.common.v1.OnlineQueryRequest\x1a$.chalk.common.v1.OnlineQueryResponse"\x03\x80}\x03\x12i\n\x0fOnlineQueryBulk\x12\'.chalk.common.v1.OnlineQueryBulkRequest\x1a(.chalk.common.v1.OnlineQueryBulkResponse"\x03\x80}\x03\x12l\n\x10OnlineQueryMulti\x12(.chalk.common.v1.OnlineQueryMultiRequest\x1a).chalk.common.v1.OnlineQueryMultiResponse"\x03\x80}\x03\x12r\n\x12UploadFeaturesBulk\x12*.chalk.common.v1.UploadFeaturesBulkRequest\x1a+.chalk.common.v1.UploadFeaturesBulkResponse"\x03\x80}\x03\x12\x84\x01\n\x15PlanAggregateBackfill\x12\x30.chalk.aggregate.v1.PlanAggregateBackfillRequest\x1a\x31.chalk.aggregate.v1.PlanAggregateBackfillResponse"\x06\x90\x02\x01\x80}\x0c\x12l\n\rGetAggregates\x12(.chalk.aggregate.v1.GetAggregatesRequest\x1a).chalk.aggregate.v1.GetAggregatesResponse"\x06\x90\x02\x01\x80}\x0b\x42\x85\x01\n\x13\x63om.chalk.engine.v1B\x10QueryServerProtoP\x01\xa2\x02\x03\x43\x45X\xaa\x02\x0f\x43halk.Engine.V1\xca\x02\x0f\x43halk\\Engine\\V1\xe2\x02\x1b\x43halk\\Engine\\V1\\GPBMetadata\xea\x02\x11\x43halk::Engine::V1b\x06proto3'
)

_globals = globals()
_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, _globals)
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, "chalk.engine.v1.query_server_pb2", _globals)
if _descriptor._USE_C_DESCRIPTORS == False:
    _globals["DESCRIPTOR"]._options = None
    _globals[
        "DESCRIPTOR"
    ]._serialized_options = b"\n\023com.chalk.engine.v1B\020QueryServerProtoP\001\242\002\003CEX\252\002\017Chalk.Engine.V1\312\002\017Chalk\\Engine\\V1\342\002\033Chalk\\Engine\\V1\\GPBMetadata\352\002\021Chalk::Engine::V1"
    _globals["_QUERYSERVICE"].methods_by_name["Ping"]._options = None
    _globals["_QUERYSERVICE"].methods_by_name["Ping"]._serialized_options = b"\220\002\001\200}\001"
    _globals["_QUERYSERVICE"].methods_by_name["OnlineQuery"]._options = None
    _globals["_QUERYSERVICE"].methods_by_name["OnlineQuery"]._serialized_options = b"\200}\003"
    _globals["_QUERYSERVICE"].methods_by_name["OnlineQueryBulk"]._options = None
    _globals["_QUERYSERVICE"].methods_by_name["OnlineQueryBulk"]._serialized_options = b"\200}\003"
    _globals["_QUERYSERVICE"].methods_by_name["OnlineQueryMulti"]._options = None
    _globals["_QUERYSERVICE"].methods_by_name["OnlineQueryMulti"]._serialized_options = b"\200}\003"
    _globals["_QUERYSERVICE"].methods_by_name["UploadFeaturesBulk"]._options = None
    _globals["_QUERYSERVICE"].methods_by_name["UploadFeaturesBulk"]._serialized_options = b"\200}\003"
    _globals["_QUERYSERVICE"].methods_by_name["PlanAggregateBackfill"]._options = None
    _globals["_QUERYSERVICE"].methods_by_name["PlanAggregateBackfill"]._serialized_options = b"\220\002\001\200}\014"
    _globals["_QUERYSERVICE"].methods_by_name["GetAggregates"]._options = None
    _globals["_QUERYSERVICE"].methods_by_name["GetAggregates"]._serialized_options = b"\220\002\001\200}\013"
    _globals["_PINGREQUEST"]._serialized_start = 158
    _globals["_PINGREQUEST"]._serialized_end = 189
    _globals["_PINGRESPONSE"]._serialized_start = 191
    _globals["_PINGRESPONSE"]._serialized_end = 223
    _globals["_QUERYSERVICE"]._serialized_start = 226
    _globals["_QUERYSERVICE"]._serialized_end = 990
# @@protoc_insertion_point(module_scope)
