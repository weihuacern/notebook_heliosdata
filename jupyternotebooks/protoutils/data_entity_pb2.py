# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: data_entity.proto

import sys
_b=sys.version_info[0]<3 and (lambda x:x) or (lambda x:x.encode('latin1'))
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


import tags_pb2 as tags__pb2
import scannerdata_locationinfo_pb2 as scannerdata__locationinfo__pb2


DESCRIPTOR = _descriptor.FileDescriptor(
  name='data_entity.proto',
  package='data',
  syntax='proto3',
  serialized_options=None,
  serialized_pb=_b('\n\x11\x64\x61ta_entity.proto\x12\x04\x64\x61ta\x1a\ntags.proto\x1a\x1escannerdata_locationinfo.proto\"\xa7\x01\n\x08\x42\x65havior\x12\x11\n\ttimestmap\x18\x01 \x01(\x01\x12\n\n\x02ip\x18\x02 \x01(\t\x12\x0c\n\x04port\x18\x03 \x01(\t\x12\x0b\n\x03loc\x18\x04 \x01(\t\x12\x17\n\x0f\x61\x63\x63\x65ss_log_json\x18\x05 \x01(\t\x12\x10\n\x08\x63onn_uid\x18\x06 \x01(\t\x12\r\n\x05\x62ytes\x18\x07 \x01(\x01\x12\'\n\x0cstorage_type\x18\x08 \x01(\x0e\x32\x11.data.StorageType\"\x8a\x01\n\nRawPiiItem\x12&\n\nfield_name\x18\x01 \x01(\x0e\x32\x12.data.PiiFieldName\x12\'\n\x0c\x66\x65\x61ture_type\x18\x02 \x01(\x0e\x32\x11.data.FeatureType\x12\x1c\n\x04lang\x18\x03 \x01(\x0e\x32\x0e.data.Language\x12\r\n\x05value\x18\x04 \x01(\t\"\x90\x01\n\x0b\x46\x65\x61tureItem\x12&\n\x0c\x66\x65\x61ture_name\x18\x01 \x01(\x0e\x32\x10.data.FeatureTag\x12\x1f\n\x04type\x18\x02 \x01(\x0e\x32\x11.data.FeatureType\x12\x12\n\nbool_value\x18\x03 \x01(\x08\x12\x11\n\tnum_value\x18\x04 \x01(\x01\x12\x11\n\tstr_value\x18\x05 \x01(\t\"\x99\x02\n\x11\x44\x61taEntityElement\x12\x11\n\tentity_id\x18\x01 \x01(\t\x12\x0f\n\x07id_cols\x18\x02 \x03(\t\x12%\n\tlocations\x18\x03 \x01(\x0b\x32\x12.data.LocationInfo\x12#\n\x08\x66\x65\x61tures\x18\x04 \x01(\x0b\x32\x11.data.FeatureItem\x12!\n\tbehaviors\x18\x05 \x01(\x0b\x32\x0e.data.Behavior\x12\x15\n\rinfotimestamp\x18\x06 \x01(\x01\x12#\n\tpii_items\x18\x07 \x03(\x0b\x32\x10.data.RawPiiItem\x12(\n\x08\x65le_type\x18\x08 \x01(\x0e\x32\x16.data.EntityElementTag\x12\x0b\n\x03loc\x18\t \x01(\t\"\x8f\x01\n\nDataEntity\x12\x11\n\tentity_id\x18\x01 \x01(\t\x12\x0f\n\x07id_cols\x18\x02 \x03(\t\x12\x17\n\x0f\x66irst_seen_time\x18\x03 \x01(\x01\x12\x16\n\x0elast_seen_time\x18\x04 \x01(\x01\x12,\n\x0binfo_sorted\x18\x05 \x03(\x0b\x32\x17.data.DataEntityElementb\x06proto3')
  ,
  dependencies=[tags__pb2.DESCRIPTOR,scannerdata__locationinfo__pb2.DESCRIPTOR,])




_BEHAVIOR = _descriptor.Descriptor(
  name='Behavior',
  full_name='data.Behavior',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='timestmap', full_name='data.Behavior.timestmap', index=0,
      number=1, type=1, cpp_type=5, label=1,
      has_default_value=False, default_value=float(0),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='ip', full_name='data.Behavior.ip', index=1,
      number=2, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='port', full_name='data.Behavior.port', index=2,
      number=3, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='loc', full_name='data.Behavior.loc', index=3,
      number=4, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='access_log_json', full_name='data.Behavior.access_log_json', index=4,
      number=5, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='conn_uid', full_name='data.Behavior.conn_uid', index=5,
      number=6, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='bytes', full_name='data.Behavior.bytes', index=6,
      number=7, type=1, cpp_type=5, label=1,
      has_default_value=False, default_value=float(0),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='storage_type', full_name='data.Behavior.storage_type', index=7,
      number=8, type=14, cpp_type=8, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=72,
  serialized_end=239,
)


_RAWPIIITEM = _descriptor.Descriptor(
  name='RawPiiItem',
  full_name='data.RawPiiItem',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='field_name', full_name='data.RawPiiItem.field_name', index=0,
      number=1, type=14, cpp_type=8, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='feature_type', full_name='data.RawPiiItem.feature_type', index=1,
      number=2, type=14, cpp_type=8, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='lang', full_name='data.RawPiiItem.lang', index=2,
      number=3, type=14, cpp_type=8, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='value', full_name='data.RawPiiItem.value', index=3,
      number=4, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=242,
  serialized_end=380,
)


_FEATUREITEM = _descriptor.Descriptor(
  name='FeatureItem',
  full_name='data.FeatureItem',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='feature_name', full_name='data.FeatureItem.feature_name', index=0,
      number=1, type=14, cpp_type=8, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='type', full_name='data.FeatureItem.type', index=1,
      number=2, type=14, cpp_type=8, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='bool_value', full_name='data.FeatureItem.bool_value', index=2,
      number=3, type=8, cpp_type=7, label=1,
      has_default_value=False, default_value=False,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='num_value', full_name='data.FeatureItem.num_value', index=3,
      number=4, type=1, cpp_type=5, label=1,
      has_default_value=False, default_value=float(0),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='str_value', full_name='data.FeatureItem.str_value', index=4,
      number=5, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=383,
  serialized_end=527,
)


_DATAENTITYELEMENT = _descriptor.Descriptor(
  name='DataEntityElement',
  full_name='data.DataEntityElement',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='entity_id', full_name='data.DataEntityElement.entity_id', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='id_cols', full_name='data.DataEntityElement.id_cols', index=1,
      number=2, type=9, cpp_type=9, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='locations', full_name='data.DataEntityElement.locations', index=2,
      number=3, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='features', full_name='data.DataEntityElement.features', index=3,
      number=4, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='behaviors', full_name='data.DataEntityElement.behaviors', index=4,
      number=5, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='infotimestamp', full_name='data.DataEntityElement.infotimestamp', index=5,
      number=6, type=1, cpp_type=5, label=1,
      has_default_value=False, default_value=float(0),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='pii_items', full_name='data.DataEntityElement.pii_items', index=6,
      number=7, type=11, cpp_type=10, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='ele_type', full_name='data.DataEntityElement.ele_type', index=7,
      number=8, type=14, cpp_type=8, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='loc', full_name='data.DataEntityElement.loc', index=8,
      number=9, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=530,
  serialized_end=811,
)


_DATAENTITY = _descriptor.Descriptor(
  name='DataEntity',
  full_name='data.DataEntity',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='entity_id', full_name='data.DataEntity.entity_id', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='id_cols', full_name='data.DataEntity.id_cols', index=1,
      number=2, type=9, cpp_type=9, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='first_seen_time', full_name='data.DataEntity.first_seen_time', index=2,
      number=3, type=1, cpp_type=5, label=1,
      has_default_value=False, default_value=float(0),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='last_seen_time', full_name='data.DataEntity.last_seen_time', index=3,
      number=4, type=1, cpp_type=5, label=1,
      has_default_value=False, default_value=float(0),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='info_sorted', full_name='data.DataEntity.info_sorted', index=4,
      number=5, type=11, cpp_type=10, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=814,
  serialized_end=957,
)

_BEHAVIOR.fields_by_name['storage_type'].enum_type = tags__pb2._STORAGETYPE
_RAWPIIITEM.fields_by_name['field_name'].enum_type = tags__pb2._PIIFIELDNAME
_RAWPIIITEM.fields_by_name['feature_type'].enum_type = tags__pb2._FEATURETYPE
_RAWPIIITEM.fields_by_name['lang'].enum_type = tags__pb2._LANGUAGE
_FEATUREITEM.fields_by_name['feature_name'].enum_type = tags__pb2._FEATURETAG
_FEATUREITEM.fields_by_name['type'].enum_type = tags__pb2._FEATURETYPE
_DATAENTITYELEMENT.fields_by_name['locations'].message_type = scannerdata__locationinfo__pb2._LOCATIONINFO
_DATAENTITYELEMENT.fields_by_name['features'].message_type = _FEATUREITEM
_DATAENTITYELEMENT.fields_by_name['behaviors'].message_type = _BEHAVIOR
_DATAENTITYELEMENT.fields_by_name['pii_items'].message_type = _RAWPIIITEM
_DATAENTITYELEMENT.fields_by_name['ele_type'].enum_type = tags__pb2._ENTITYELEMENTTAG
_DATAENTITY.fields_by_name['info_sorted'].message_type = _DATAENTITYELEMENT
DESCRIPTOR.message_types_by_name['Behavior'] = _BEHAVIOR
DESCRIPTOR.message_types_by_name['RawPiiItem'] = _RAWPIIITEM
DESCRIPTOR.message_types_by_name['FeatureItem'] = _FEATUREITEM
DESCRIPTOR.message_types_by_name['DataEntityElement'] = _DATAENTITYELEMENT
DESCRIPTOR.message_types_by_name['DataEntity'] = _DATAENTITY
_sym_db.RegisterFileDescriptor(DESCRIPTOR)

Behavior = _reflection.GeneratedProtocolMessageType('Behavior', (_message.Message,), dict(
  DESCRIPTOR = _BEHAVIOR,
  __module__ = 'data_entity_pb2'
  # @@protoc_insertion_point(class_scope:data.Behavior)
  ))
_sym_db.RegisterMessage(Behavior)

RawPiiItem = _reflection.GeneratedProtocolMessageType('RawPiiItem', (_message.Message,), dict(
  DESCRIPTOR = _RAWPIIITEM,
  __module__ = 'data_entity_pb2'
  # @@protoc_insertion_point(class_scope:data.RawPiiItem)
  ))
_sym_db.RegisterMessage(RawPiiItem)

FeatureItem = _reflection.GeneratedProtocolMessageType('FeatureItem', (_message.Message,), dict(
  DESCRIPTOR = _FEATUREITEM,
  __module__ = 'data_entity_pb2'
  # @@protoc_insertion_point(class_scope:data.FeatureItem)
  ))
_sym_db.RegisterMessage(FeatureItem)

DataEntityElement = _reflection.GeneratedProtocolMessageType('DataEntityElement', (_message.Message,), dict(
  DESCRIPTOR = _DATAENTITYELEMENT,
  __module__ = 'data_entity_pb2'
  # @@protoc_insertion_point(class_scope:data.DataEntityElement)
  ))
_sym_db.RegisterMessage(DataEntityElement)

DataEntity = _reflection.GeneratedProtocolMessageType('DataEntity', (_message.Message,), dict(
  DESCRIPTOR = _DATAENTITY,
  __module__ = 'data_entity_pb2'
  # @@protoc_insertion_point(class_scope:data.DataEntity)
  ))
_sym_db.RegisterMessage(DataEntity)


# @@protoc_insertion_point(module_scope)
