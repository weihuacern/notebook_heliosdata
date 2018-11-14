# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: tags.proto

import sys
_b=sys.version_info[0]<3 and (lambda x:x) or (lambda x:x.encode('latin1'))
from google.protobuf.internal import enum_type_wrapper
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()




DESCRIPTOR = _descriptor.FileDescriptor(
  name='tags.proto',
  package='data',
  syntax='proto3',
  serialized_options=None,
  serialized_pb=_b('\n\ntags.proto\x12\x04\x64\x61ta*_\n\x0bStorageType\x12\x13\n\x0f\x44\x42_TYPE_DEFAULT\x10\x00\x12\x0c\n\x08MSSQL_DB\x10\x01\x12\x0c\n\x08MYSQL_DB\x10\x02\x12\t\n\x05SAMBA\x10\x03\x12\x07\n\x03NFS\x10\x04\x12\x0b\n\x07MONGODB\x10\x05*V\n\x0b\x46ileLogType\x12\x19\n\x15\x46ILE_LOG_TYPE_DEFAULT\x10\x00\x12\x0e\n\nPII_IE_LOG\x10\x01\x12\r\n\tFUZZY_LOG\x10\x02\x12\r\n\tFILES_LOG\x10\x03*\xcd\x03\n\x0cPiiFieldName\x12\x16\n\x12\x46IELD_NAME_DEFAULT\x10\x00\x12\x0e\n\nFIRST_NAME\x10\x01\x12\r\n\tLAST_NAME\x10\x02\x12\x0f\n\x0bMIDDLE_NAME\x10\x03\x12\r\n\tFULL_NAME\x10\x04\x12\n\n\x06GENDER\x10\x05\x12\x07\n\x03\x41GE\x10\x06\x12\x11\n\rDATE_OF_BIRTH\x10\x07\x12\x1a\n\x16SOCIAL_SECURITY_NUMBER\x10\x08\x12\x19\n\x15IDENTIFICATION_NUMBER\x10\t\x12\x13\n\x0fPASSPORT_NUMBER\x10\n\x12\x1a\n\x16STREET_NUMBER_AND_NAME\x10\x0b\x12\n\n\x06PO_BOX\x10\x0c\x12\x08\n\x04\x43ITY\x10\r\x12\t\n\x05STATE\x10\x0e\x12\x0c\n\x08ZIP_CODE\x10\x0f\x12\x0b\n\x07\x43OUNTRY\x10\x10\x12\x0b\n\x07\x41\x44\x44RESS\x10\x11\x12\x10\n\x0cMOBILE_PHONE\x10\x12\x12\r\n\tFIX_PHONE\x10\x13\x12\t\n\x05PHONE\x10\x14\x12\t\n\x05\x45MAIL\x10\x15\x12\r\n\tEDUCATION\x10\x16\x12\x0c\n\x08INDUSTRY\x10\x17\x12\x0b\n\x07\x43OMPANY\x10\x18\x12\x12\n\x0eMARITAL_STATUS\x10\x19\x12\x08\n\x04RACE\x10\x1a\x12\x0e\n\nOCCUPATION\x10\x1b*<\n\nFeatureTag\x12\x0b\n\x07\x44\x45\x46\x41ULT\x10\x00\x12\r\n\tUNDER_AGE\x10\x01\x12\x12\n\x0eRESIDE_COUNTRY\x10\x02*C\n\x10\x45ntityElementTag\x12\x13\n\x0f\x45LEMENT_DEFAULT\x10\x00\x12\x0c\n\x08LOCATION\x10\x01\x12\x0c\n\x08\x42\x45HAVIOR\x10\x02*F\n\x08Language\x12\x10\n\x0cLANG_DEFAULT\x10\x00\x12\x0b\n\x07\x45NGLISH\x10\x01\x12\x0b\n\x07\x43HINESE\x10\x02\x12\x0e\n\nINDONESIAN\x10\x03*\xa1\x01\n\x06\x42roLog\x12\x13\n\x0f\x42RO_LOG_DEFAULT\x10\x00\x12\x08\n\x04\x43ONN\x10\x01\x12\x07\n\x03\x44NS\x10\x02\x12\x08\n\x04HTTP\x10\x03\x12\x07\n\x03TDS\x10\x04\x12\x10\n\x0cTDS_SQLBATCH\x10\x05\x12\x11\n\rTDS_TDS7LOGIN\x10\x06\x12\x07\n\x03SSL\x10\x07\x12\t\n\x05\x46ILES\x10\x08\x12\t\n\x05MYSQL\x10\t\x12\t\n\x05\x46UZZY\x10\n\x12\r\n\tSMB_FILES\x10\x0b*I\n\x0b\x46\x65\x61tureType\x12\x18\n\x14\x46\x45\x41TURE_TYPE_DEFAULT\x10\x00\x12\x0b\n\x07\x42OOLEAN\x10\x01\x12\x07\n\x03NUM\x10\x02\x12\n\n\x06STRING\x10\x03*B\n\x0bKvStoreType\x12\x18\n\x14KVSTORE_TYPE_DEFAULT\x10\x00\x12\n\n\x06\x43ONSUL\x10\x01\x12\r\n\tCASSANDRA\x10\x02\x62\x06proto3')
)

_STORAGETYPE = _descriptor.EnumDescriptor(
  name='StorageType',
  full_name='data.StorageType',
  filename=None,
  file=DESCRIPTOR,
  values=[
    _descriptor.EnumValueDescriptor(
      name='DB_TYPE_DEFAULT', index=0, number=0,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='MSSQL_DB', index=1, number=1,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='MYSQL_DB', index=2, number=2,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='SAMBA', index=3, number=3,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='NFS', index=4, number=4,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='MONGODB', index=5, number=5,
      serialized_options=None,
      type=None),
  ],
  containing_type=None,
  serialized_options=None,
  serialized_start=20,
  serialized_end=115,
)
_sym_db.RegisterEnumDescriptor(_STORAGETYPE)

StorageType = enum_type_wrapper.EnumTypeWrapper(_STORAGETYPE)
_FILELOGTYPE = _descriptor.EnumDescriptor(
  name='FileLogType',
  full_name='data.FileLogType',
  filename=None,
  file=DESCRIPTOR,
  values=[
    _descriptor.EnumValueDescriptor(
      name='FILE_LOG_TYPE_DEFAULT', index=0, number=0,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='PII_IE_LOG', index=1, number=1,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='FUZZY_LOG', index=2, number=2,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='FILES_LOG', index=3, number=3,
      serialized_options=None,
      type=None),
  ],
  containing_type=None,
  serialized_options=None,
  serialized_start=117,
  serialized_end=203,
)
_sym_db.RegisterEnumDescriptor(_FILELOGTYPE)

FileLogType = enum_type_wrapper.EnumTypeWrapper(_FILELOGTYPE)
_PIIFIELDNAME = _descriptor.EnumDescriptor(
  name='PiiFieldName',
  full_name='data.PiiFieldName',
  filename=None,
  file=DESCRIPTOR,
  values=[
    _descriptor.EnumValueDescriptor(
      name='FIELD_NAME_DEFAULT', index=0, number=0,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='FIRST_NAME', index=1, number=1,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='LAST_NAME', index=2, number=2,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='MIDDLE_NAME', index=3, number=3,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='FULL_NAME', index=4, number=4,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='GENDER', index=5, number=5,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='AGE', index=6, number=6,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='DATE_OF_BIRTH', index=7, number=7,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='SOCIAL_SECURITY_NUMBER', index=8, number=8,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='IDENTIFICATION_NUMBER', index=9, number=9,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='PASSPORT_NUMBER', index=10, number=10,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='STREET_NUMBER_AND_NAME', index=11, number=11,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='PO_BOX', index=12, number=12,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='CITY', index=13, number=13,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='STATE', index=14, number=14,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='ZIP_CODE', index=15, number=15,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='COUNTRY', index=16, number=16,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='ADDRESS', index=17, number=17,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='MOBILE_PHONE', index=18, number=18,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='FIX_PHONE', index=19, number=19,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='PHONE', index=20, number=20,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='EMAIL', index=21, number=21,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='EDUCATION', index=22, number=22,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='INDUSTRY', index=23, number=23,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='COMPANY', index=24, number=24,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='MARITAL_STATUS', index=25, number=25,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='RACE', index=26, number=26,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='OCCUPATION', index=27, number=27,
      serialized_options=None,
      type=None),
  ],
  containing_type=None,
  serialized_options=None,
  serialized_start=206,
  serialized_end=667,
)
_sym_db.RegisterEnumDescriptor(_PIIFIELDNAME)

PiiFieldName = enum_type_wrapper.EnumTypeWrapper(_PIIFIELDNAME)
_FEATURETAG = _descriptor.EnumDescriptor(
  name='FeatureTag',
  full_name='data.FeatureTag',
  filename=None,
  file=DESCRIPTOR,
  values=[
    _descriptor.EnumValueDescriptor(
      name='DEFAULT', index=0, number=0,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='UNDER_AGE', index=1, number=1,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='RESIDE_COUNTRY', index=2, number=2,
      serialized_options=None,
      type=None),
  ],
  containing_type=None,
  serialized_options=None,
  serialized_start=669,
  serialized_end=729,
)
_sym_db.RegisterEnumDescriptor(_FEATURETAG)

FeatureTag = enum_type_wrapper.EnumTypeWrapper(_FEATURETAG)
_ENTITYELEMENTTAG = _descriptor.EnumDescriptor(
  name='EntityElementTag',
  full_name='data.EntityElementTag',
  filename=None,
  file=DESCRIPTOR,
  values=[
    _descriptor.EnumValueDescriptor(
      name='ELEMENT_DEFAULT', index=0, number=0,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='LOCATION', index=1, number=1,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='BEHAVIOR', index=2, number=2,
      serialized_options=None,
      type=None),
  ],
  containing_type=None,
  serialized_options=None,
  serialized_start=731,
  serialized_end=798,
)
_sym_db.RegisterEnumDescriptor(_ENTITYELEMENTTAG)

EntityElementTag = enum_type_wrapper.EnumTypeWrapper(_ENTITYELEMENTTAG)
_LANGUAGE = _descriptor.EnumDescriptor(
  name='Language',
  full_name='data.Language',
  filename=None,
  file=DESCRIPTOR,
  values=[
    _descriptor.EnumValueDescriptor(
      name='LANG_DEFAULT', index=0, number=0,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='ENGLISH', index=1, number=1,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='CHINESE', index=2, number=2,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='INDONESIAN', index=3, number=3,
      serialized_options=None,
      type=None),
  ],
  containing_type=None,
  serialized_options=None,
  serialized_start=800,
  serialized_end=870,
)
_sym_db.RegisterEnumDescriptor(_LANGUAGE)

Language = enum_type_wrapper.EnumTypeWrapper(_LANGUAGE)
_BROLOG = _descriptor.EnumDescriptor(
  name='BroLog',
  full_name='data.BroLog',
  filename=None,
  file=DESCRIPTOR,
  values=[
    _descriptor.EnumValueDescriptor(
      name='BRO_LOG_DEFAULT', index=0, number=0,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='CONN', index=1, number=1,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='DNS', index=2, number=2,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='HTTP', index=3, number=3,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='TDS', index=4, number=4,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='TDS_SQLBATCH', index=5, number=5,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='TDS_TDS7LOGIN', index=6, number=6,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='SSL', index=7, number=7,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='FILES', index=8, number=8,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='MYSQL', index=9, number=9,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='FUZZY', index=10, number=10,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='SMB_FILES', index=11, number=11,
      serialized_options=None,
      type=None),
  ],
  containing_type=None,
  serialized_options=None,
  serialized_start=873,
  serialized_end=1034,
)
_sym_db.RegisterEnumDescriptor(_BROLOG)

BroLog = enum_type_wrapper.EnumTypeWrapper(_BROLOG)
_FEATURETYPE = _descriptor.EnumDescriptor(
  name='FeatureType',
  full_name='data.FeatureType',
  filename=None,
  file=DESCRIPTOR,
  values=[
    _descriptor.EnumValueDescriptor(
      name='FEATURE_TYPE_DEFAULT', index=0, number=0,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='BOOLEAN', index=1, number=1,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='NUM', index=2, number=2,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='STRING', index=3, number=3,
      serialized_options=None,
      type=None),
  ],
  containing_type=None,
  serialized_options=None,
  serialized_start=1036,
  serialized_end=1109,
)
_sym_db.RegisterEnumDescriptor(_FEATURETYPE)

FeatureType = enum_type_wrapper.EnumTypeWrapper(_FEATURETYPE)
_KVSTORETYPE = _descriptor.EnumDescriptor(
  name='KvStoreType',
  full_name='data.KvStoreType',
  filename=None,
  file=DESCRIPTOR,
  values=[
    _descriptor.EnumValueDescriptor(
      name='KVSTORE_TYPE_DEFAULT', index=0, number=0,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='CONSUL', index=1, number=1,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='CASSANDRA', index=2, number=2,
      serialized_options=None,
      type=None),
  ],
  containing_type=None,
  serialized_options=None,
  serialized_start=1111,
  serialized_end=1177,
)
_sym_db.RegisterEnumDescriptor(_KVSTORETYPE)

KvStoreType = enum_type_wrapper.EnumTypeWrapper(_KVSTORETYPE)
DB_TYPE_DEFAULT = 0
MSSQL_DB = 1
MYSQL_DB = 2
SAMBA = 3
NFS = 4
MONGODB = 5
FILE_LOG_TYPE_DEFAULT = 0
PII_IE_LOG = 1
FUZZY_LOG = 2
FILES_LOG = 3
FIELD_NAME_DEFAULT = 0
FIRST_NAME = 1
LAST_NAME = 2
MIDDLE_NAME = 3
FULL_NAME = 4
GENDER = 5
AGE = 6
DATE_OF_BIRTH = 7
SOCIAL_SECURITY_NUMBER = 8
IDENTIFICATION_NUMBER = 9
PASSPORT_NUMBER = 10
STREET_NUMBER_AND_NAME = 11
PO_BOX = 12
CITY = 13
STATE = 14
ZIP_CODE = 15
COUNTRY = 16
ADDRESS = 17
MOBILE_PHONE = 18
FIX_PHONE = 19
PHONE = 20
EMAIL = 21
EDUCATION = 22
INDUSTRY = 23
COMPANY = 24
MARITAL_STATUS = 25
RACE = 26
OCCUPATION = 27
DEFAULT = 0
UNDER_AGE = 1
RESIDE_COUNTRY = 2
ELEMENT_DEFAULT = 0
LOCATION = 1
BEHAVIOR = 2
LANG_DEFAULT = 0
ENGLISH = 1
CHINESE = 2
INDONESIAN = 3
BRO_LOG_DEFAULT = 0
CONN = 1
DNS = 2
HTTP = 3
TDS = 4
TDS_SQLBATCH = 5
TDS_TDS7LOGIN = 6
SSL = 7
FILES = 8
MYSQL = 9
FUZZY = 10
SMB_FILES = 11
FEATURE_TYPE_DEFAULT = 0
BOOLEAN = 1
NUM = 2
STRING = 3
KVSTORE_TYPE_DEFAULT = 0
CONSUL = 1
CASSANDRA = 2


DESCRIPTOR.enum_types_by_name['StorageType'] = _STORAGETYPE
DESCRIPTOR.enum_types_by_name['FileLogType'] = _FILELOGTYPE
DESCRIPTOR.enum_types_by_name['PiiFieldName'] = _PIIFIELDNAME
DESCRIPTOR.enum_types_by_name['FeatureTag'] = _FEATURETAG
DESCRIPTOR.enum_types_by_name['EntityElementTag'] = _ENTITYELEMENTTAG
DESCRIPTOR.enum_types_by_name['Language'] = _LANGUAGE
DESCRIPTOR.enum_types_by_name['BroLog'] = _BROLOG
DESCRIPTOR.enum_types_by_name['FeatureType'] = _FEATURETYPE
DESCRIPTOR.enum_types_by_name['KvStoreType'] = _KVSTORETYPE
_sym_db.RegisterFileDescriptor(DESCRIPTOR)


# @@protoc_insertion_point(module_scope)
