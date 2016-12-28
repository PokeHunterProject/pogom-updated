# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: POGOProtos/Data/Battle/BattleLog.proto

import sys
_b=sys.version_info[0]<3 and (lambda x:x) or (lambda x:x.encode('latin1'))
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
from google.protobuf import descriptor_pb2
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


from POGOProtos.Data.Battle import BattleAction_pb2 as POGOProtos_dot_Data_dot_Battle_dot_BattleAction__pb2
from POGOProtos.Data.Battle import BattleState_pb2 as POGOProtos_dot_Data_dot_Battle_dot_BattleState__pb2
from POGOProtos.Data.Battle import BattleType_pb2 as POGOProtos_dot_Data_dot_Battle_dot_BattleType__pb2


DESCRIPTOR = _descriptor.FileDescriptor(
  name='POGOProtos/Data/Battle/BattleLog.proto',
  package='POGOProtos.Data.Battle',
  syntax='proto3',
  serialized_pb=_b('\n&POGOProtos/Data/Battle/BattleLog.proto\x12\x16POGOProtos.Data.Battle\x1a)POGOProtos/Data/Battle/BattleAction.proto\x1a(POGOProtos/Data/Battle/BattleState.proto\x1a\'POGOProtos/Data/Battle/BattleType.proto\"\x8d\x02\n\tBattleLog\x12\x32\n\x05state\x18\x01 \x01(\x0e\x32#.POGOProtos.Data.Battle.BattleState\x12\x37\n\x0b\x62\x61ttle_type\x18\x02 \x01(\x0e\x32\".POGOProtos.Data.Battle.BattleType\x12\x11\n\tserver_ms\x18\x03 \x01(\x03\x12<\n\x0e\x62\x61ttle_actions\x18\x04 \x03(\x0b\x32$.POGOProtos.Data.Battle.BattleAction\x12!\n\x19\x62\x61ttle_start_timestamp_ms\x18\x05 \x01(\x03\x12\x1f\n\x17\x62\x61ttle_end_timestamp_ms\x18\x06 \x01(\x03\x62\x06proto3')
  ,
  dependencies=[POGOProtos_dot_Data_dot_Battle_dot_BattleAction__pb2.DESCRIPTOR,POGOProtos_dot_Data_dot_Battle_dot_BattleState__pb2.DESCRIPTOR,POGOProtos_dot_Data_dot_Battle_dot_BattleType__pb2.DESCRIPTOR,])
_sym_db.RegisterFileDescriptor(DESCRIPTOR)




_BATTLELOG = _descriptor.Descriptor(
  name='BattleLog',
  full_name='POGOProtos.Data.Battle.BattleLog',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='state', full_name='POGOProtos.Data.Battle.BattleLog.state', index=0,
      number=1, type=14, cpp_type=8, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='battle_type', full_name='POGOProtos.Data.Battle.BattleLog.battle_type', index=1,
      number=2, type=14, cpp_type=8, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='server_ms', full_name='POGOProtos.Data.Battle.BattleLog.server_ms', index=2,
      number=3, type=3, cpp_type=2, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='battle_actions', full_name='POGOProtos.Data.Battle.BattleLog.battle_actions', index=3,
      number=4, type=11, cpp_type=10, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='battle_start_timestamp_ms', full_name='POGOProtos.Data.Battle.BattleLog.battle_start_timestamp_ms', index=4,
      number=5, type=3, cpp_type=2, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='battle_end_timestamp_ms', full_name='POGOProtos.Data.Battle.BattleLog.battle_end_timestamp_ms', index=5,
      number=6, type=3, cpp_type=2, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=193,
  serialized_end=462,
)

_BATTLELOG.fields_by_name['state'].enum_type = POGOProtos_dot_Data_dot_Battle_dot_BattleState__pb2._BATTLESTATE
_BATTLELOG.fields_by_name['battle_type'].enum_type = POGOProtos_dot_Data_dot_Battle_dot_BattleType__pb2._BATTLETYPE
_BATTLELOG.fields_by_name['battle_actions'].message_type = POGOProtos_dot_Data_dot_Battle_dot_BattleAction__pb2._BATTLEACTION
DESCRIPTOR.message_types_by_name['BattleLog'] = _BATTLELOG

BattleLog = _reflection.GeneratedProtocolMessageType('BattleLog', (_message.Message,), dict(
  DESCRIPTOR = _BATTLELOG,
  __module__ = 'POGOProtos.Data.Battle.BattleLog_pb2'
  # @@protoc_insertion_point(class_scope:POGOProtos.Data.Battle.BattleLog)
  ))
_sym_db.RegisterMessage(BattleLog)


# @@protoc_insertion_point(module_scope)