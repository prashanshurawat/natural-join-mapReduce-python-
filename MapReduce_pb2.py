# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: MapReduce.proto
"""Generated protocol buffer code."""
from google.protobuf.internal import builder as _builder
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database

# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()

DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(
    b'\n\x0fMapReduce.proto\x12\nmaster_map\"\x8d\x01\n\tinput_map\x12\x36\n\tindex_map\x18\x01 \x03(\x0b\x32#.master_map.input_map.IndexMapEntry\x1aH\n\rIndexMapEntry\x12\x0b\n\x03key\x18\x01 \x01(\t\x12&\n\x05value\x18\x02 \x01(\x0b\x32\x17.master_map.input_split:\x02\x38\x01\"\x1c\n\x0binput_split\x12\r\n\x05input\x18\x01 \x03(\t\"\"\n\x0einput_response\x12\x10\n\x08response\x18\x01 \x01(\t2\x92\x01\n\x03map\x12\x42\n\x0binputSplits\x12\x15.master_map.input_map\x1a\x1a.master_map.input_response\"\x00\x12G\n\x0ereducer_inputs\x12\x17.master_map.input_split\x1a\x1a.master_map.input_response\"\x00\x62\x06proto3')

_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, globals())
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'MapReduce_pb2', globals())
_MAP = DESCRIPTOR.services_by_name['map']

_INPUT_SPLIT = DESCRIPTOR.message_types_by_name['input_split']
input_split = _reflection.GeneratedProtocolMessageType('input_split', (_message.Message,), {
    'DESCRIPTOR': _INPUT_SPLIT,
    '__module__': 'MapReduce_pb2'
})
_sym_db.RegisterMessage(input_split)

_INPUT_MAP = DESCRIPTOR.message_types_by_name['input_map']
input_map = _reflection.GeneratedProtocolMessageType('input_map', (_message.Message,), {
    'DESCRIPTOR': _INPUT_MAP,
    '__module__': 'MapReduce_pb2'
})
_sym_db.RegisterMessage(input_map)

_INPUT_RESPONSE = DESCRIPTOR.message_types_by_name['input_response']
input_response = _reflection.GeneratedProtocolMessageType('input_response', (_message.Message,), {
    'DESCRIPTOR': _INPUT_RESPONSE,
    '__module__': 'MapReduce_pb2'
})
_sym_db.RegisterMessage(input_response)

if _descriptor._USE_C_DESCRIPTORS == False:
    DESCRIPTOR._options = None
    _INPUT_MAP_INDEXMAPENTRY._options = None
    _INPUT_MAP_INDEXMAPENTRY._serialized_options = b'8\001'
    _INPUT_MAP._serialized_start = 32
    _INPUT_MAP._serialized_end = 173
    _INPUT_MAP_INDEXMAPENTRY._serialized_start = 101
    _INPUT_MAP_INDEXMAPENTRY._serialized_end = 173
    _INPUT_SPLIT._serialized_start = 175
    _INPUT_SPLIT._serialized_end = 203
    _INPUT_RESPONSE._serialized_start = 205
    _INPUT_RESPONSE._serialized_end = 239
    _MAP._serialized_start = 242
    _MAP._serialized_end = 388
# @@protoc_insertion_point(module_scope)