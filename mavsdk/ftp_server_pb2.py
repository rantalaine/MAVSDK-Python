# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# NO CHECKED-IN PROTOBUF GENCODE
# source: ftp_server/ftp_server.proto
# Protobuf Python Version: 5.29.0
"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import runtime_version as _runtime_version
from google.protobuf import symbol_database as _symbol_database
from google.protobuf.internal import builder as _builder
_runtime_version.ValidateProtobufRuntimeVersion(
    _runtime_version.Domain.PUBLIC,
    5,
    29,
    0,
    '',
    'ftp_server/ftp_server.proto'
)
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


from . import mavsdk_options_pb2 as mavsdk__options__pb2


DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n\x1b\x66tp_server/ftp_server.proto\x12\x15mavsdk.rpc.ftp_server\x1a\x14mavsdk_options.proto\"!\n\x11SetRootDirRequest\x12\x0c\n\x04path\x18\x01 \x01(\t\"W\n\x12SetRootDirResponse\x12\x41\n\x11\x66tp_server_result\x18\x01 \x01(\x0b\x32&.mavsdk.rpc.ftp_server.FtpServerResult\"\xc2\x01\n\x0f\x46tpServerResult\x12=\n\x06result\x18\x01 \x01(\x0e\x32-.mavsdk.rpc.ftp_server.FtpServerResult.Result\x12\x12\n\nresult_str\x18\x02 \x01(\t\"\\\n\x06Result\x12\x12\n\x0eRESULT_UNKNOWN\x10\x00\x12\x12\n\x0eRESULT_SUCCESS\x10\x01\x12\x19\n\x15RESULT_DOES_NOT_EXIST\x10\x02\x12\x0f\n\x0bRESULT_BUSY\x10\x03\x32{\n\x10\x46tpServerService\x12g\n\nSetRootDir\x12(.mavsdk.rpc.ftp_server.SetRootDirRequest\x1a).mavsdk.rpc.ftp_server.SetRootDirResponse\"\x04\x80\xb5\x18\x01\x42&\n\x14io.mavsdk.ftp_serverB\x0e\x46tpServerProtob\x06proto3')

_globals = globals()
_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, _globals)
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'ftp_server.ftp_server_pb2', _globals)
if not _descriptor._USE_C_DESCRIPTORS:
  _globals['DESCRIPTOR']._loaded_options = None
  _globals['DESCRIPTOR']._serialized_options = b'\n\024io.mavsdk.ftp_serverB\016FtpServerProto'
  _globals['_FTPSERVERSERVICE'].methods_by_name['SetRootDir']._loaded_options = None
  _globals['_FTPSERVERSERVICE'].methods_by_name['SetRootDir']._serialized_options = b'\200\265\030\001'
  _globals['_SETROOTDIRREQUEST']._serialized_start=76
  _globals['_SETROOTDIRREQUEST']._serialized_end=109
  _globals['_SETROOTDIRRESPONSE']._serialized_start=111
  _globals['_SETROOTDIRRESPONSE']._serialized_end=198
  _globals['_FTPSERVERRESULT']._serialized_start=201
  _globals['_FTPSERVERRESULT']._serialized_end=395
  _globals['_FTPSERVERRESULT_RESULT']._serialized_start=303
  _globals['_FTPSERVERRESULT_RESULT']._serialized_end=395
  _globals['_FTPSERVERSERVICE']._serialized_start=397
  _globals['_FTPSERVERSERVICE']._serialized_end=520
# @@protoc_insertion_point(module_scope)
