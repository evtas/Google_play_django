# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: game.proto
"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()




DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n\ngame.proto\x12\x02pb\"\x19\n\x0bGameRequest\x12\n\n\x02id\x18\x01 \x01(\x05\"\xb3\x01\n\x0cGameResponse\x12\n\n\x02id\x18\x01 \x01(\x05\x12\x0c\n\x04name\x18\x02 \x01(\t\x12\x0e\n\x06\x61uthor\x18\x03 \x01(\t\x12\x12\n\nstarRating\x18\x04 \x01(\t\x12\x15\n\rdownloadTimes\x18\x05 \x01(\t\x12\x15\n\rcontentRating\x18\x06 \x01(\t\x12\x14\n\x0cintroduction\x18\x07 \x01(\t\x12\x12\n\nupdateTime\x18\x08 \x01(\t\x12\r\n\x05image\x18\t \x01(\t2=\n\x05Gamer\x12\x34\n\rGetGameDetail\x12\x0f.pb.GameRequest\x1a\x10.pb.GameResponse\"\x00\x42\x06Z\x04.;pbb\x06proto3')



_GAMEREQUEST = DESCRIPTOR.message_types_by_name['GameRequest']
_GAMERESPONSE = DESCRIPTOR.message_types_by_name['GameResponse']
GameRequest = _reflection.GeneratedProtocolMessageType('GameRequest', (_message.Message,), {
  'DESCRIPTOR' : _GAMEREQUEST,
  '__module__' : 'game_pb2'
  # @@protoc_insertion_point(class_scope:pb.GameRequest)
  })
_sym_db.RegisterMessage(GameRequest)

GameResponse = _reflection.GeneratedProtocolMessageType('GameResponse', (_message.Message,), {
  'DESCRIPTOR' : _GAMERESPONSE,
  '__module__' : 'game_pb2'
  # @@protoc_insertion_point(class_scope:pb.GameResponse)
  })
_sym_db.RegisterMessage(GameResponse)

_GAMER = DESCRIPTOR.services_by_name['Gamer']
if _descriptor._USE_C_DESCRIPTORS == False:

  DESCRIPTOR._options = None
  DESCRIPTOR._serialized_options = b'Z\004.;pb'
  _GAMEREQUEST._serialized_start=18
  _GAMEREQUEST._serialized_end=43
  _GAMERESPONSE._serialized_start=46
  _GAMERESPONSE._serialized_end=225
  _GAMER._serialized_start=227
  _GAMER._serialized_end=288
# @@protoc_insertion_point(module_scope)
