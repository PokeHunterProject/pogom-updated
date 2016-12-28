# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: POGOProtos/Networking/Requests/Messages/GetAssetDigestMessage.proto

import sys
_b=sys.version_info[0]<3 and (lambda x:x) or (lambda x:x.encode('latin1'))
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
from google.protobuf import descriptor_pb2
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


from POGOProtos.Enums import Platform_pb2 as POGOProtos_dot_Enums_dot_Platform__pb2


DESCRIPTOR = _descriptor.FileDescriptor(
  name='POGOProtos/Networking/Requests/Messages/GetAssetDigestMessage.proto',
  package='POGOProtos.Networking.Requests.Messages',
  syntax='proto3',
  serialized_pb=_b('\nCPOGOProtos/Networking/Requests/Messages/GetAssetDigestMessage.proto\x12\'POGOProtos.Networking.Requests.Messages\x1a\x1fPOGOProtos/Enums/Platform.proto\"\x9d\x01\n\x15GetAssetDigestMessage\x12,\n\x08platform\x18\x01 \x01(\x0e\x32\x1a.POGOProtos.Enums.Platform\x12\x1b\n\x13\x64\x65vice_manufacturer\x18\x02 \x01(\t\x12\x14\n\x0c\x64\x65vice_model\x18\x03 \x01(\t\x12\x0e\n\x06locale\x18\x04 \x01(\t\x12\x13\n\x0b\x61pp_version\x18\x05 \x01(\rb\x06proto3')
  ,
  dependencies=[POGOProtos_dot_Enums_dot_Platform__pb2.DESCRIPTOR,])
_sym_db.RegisterFileDescriptor(DESCRIPTOR)




_GETASSETDIGESTMESSAGE = _descriptor.Descriptor(
  name='GetAssetDigestMessage',
  full_name='POGOProtos.Networking.Requests.Messages.GetAssetDigestMessage',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='platform', full_name='POGOProtos.Networking.Requests.Messages.GetAssetDigestMessage.platform', index=0,
      number=1, type=14, cpp_type=8, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='device_manufacturer', full_name='POGOProtos.Networking.Requests.Messages.GetAssetDigestMessage.device_manufacturer', index=1,
      number=2, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='device_model', full_name='POGOProtos.Networking.Requests.Messages.GetAssetDigestMessage.device_model', index=2,
      number=3, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='locale', full_name='POGOProtos.Networking.Requests.Messages.GetAssetDigestMessage.locale', index=3,
      number=4, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='app_version', full_name='POGOProtos.Networking.Requests.Messages.GetAssetDigestMessage.app_version', index=4,
      number=5, type=13, cpp_type=3, label=1,
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
  serialized_start=146,
  serialized_end=303,
)

_GETASSETDIGESTMESSAGE.fields_by_name['platform'].enum_type = POGOProtos_dot_Enums_dot_Platform__pb2._PLATFORM
DESCRIPTOR.message_types_by_name['GetAssetDigestMessage'] = _GETASSETDIGESTMESSAGE

GetAssetDigestMessage = _reflection.GeneratedProtocolMessageType('GetAssetDigestMessage', (_message.Message,), dict(
  DESCRIPTOR = _GETASSETDIGESTMESSAGE,
  __module__ = 'POGOProtos.Networking.Requests.Messages.GetAssetDigestMessage_pb2'
  # @@protoc_insertion_point(class_scope:POGOProtos.Networking.Requests.Messages.GetAssetDigestMessage)
  ))
_sym_db.RegisterMessage(GetAssetDigestMessage)


# @@protoc_insertion_point(module_scope)
