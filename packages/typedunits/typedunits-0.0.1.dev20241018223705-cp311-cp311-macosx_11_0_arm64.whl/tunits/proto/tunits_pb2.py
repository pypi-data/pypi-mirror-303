# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: tunits/proto/tunits.proto
"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import symbol_database as _symbol_database
from google.protobuf.internal import builder as _builder
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()




DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n\x19tunits/proto/tunits.proto\x12\x06tunits\"2\n\x08\x46raction\x12\x11\n\tnumerator\x18\x01 \x01(\x03\x12\x13\n\x0b\x64\x65nominator\x18\x02 \x01(\x03\"h\n\x04Unit\x12\x1e\n\x04unit\x18\x01 \x01(\x0e\x32\x10.tunits.UnitEnum\x12\x1c\n\x05scale\x18\x02 \x01(\x0e\x32\r.tunits.Scale\x12\"\n\x08\x65xponent\x18\x03 \x01(\x0b\x32\x10.tunits.Fraction\"*\n\x07\x43omplex\x12\x0c\n\x04real\x18\x01 \x01(\x01\x12\x11\n\timaginary\x18\x02 \x01(\x01\"m\n\x05Value\x12\x1b\n\x05units\x18\x01 \x03(\x0b\x32\x0c.tunits.Unit\x12\x14\n\nreal_value\x18\x02 \x01(\x01H\x00\x12(\n\rcomplex_value\x18\x03 \x01(\x0b\x32\x0f.tunits.ComplexH\x00\x42\x07\n\x05value\"\x1d\n\x0b\x44oubleArray\x12\x0e\n\x06values\x18\x01 \x03(\x01\"/\n\x0c\x43omplexArray\x12\x1f\n\x06values\x18\x01 \x03(\x0b\x32\x0f.tunits.Complex\"\x93\x01\n\nValueArray\x12\x1b\n\x05units\x18\x01 \x03(\x0b\x32\x0c.tunits.Unit\x12$\n\x05reals\x18\x02 \x01(\x0b\x32\x13.tunits.DoubleArrayH\x00\x12)\n\tcomplexes\x18\x03 \x01(\x0b\x32\x14.tunits.ComplexArrayH\x00\x12\r\n\x05shape\x18\x04 \x03(\rB\x08\n\x06values*]\n\x08UnitEnum\x12\x0b\n\x07\x44\x45\x43IBEL\x10\x01\x12\x16\n\x12\x44\x45\x43IBEL_MILLIWATTS\x10\x02\x12\x0b\n\x07RADIANS\x10\x03\x12\t\n\x05HERTZ\x10\x04\x12\x08\n\x04VOLT\x10\x05\x12\n\n\x06SECOND\x10\x06*\xbd\x02\n\x05Scale\x12\t\n\x05YOTTA\x10\x18\x12\t\n\x05ZETTA\x10\x15\x12\x07\n\x03\x45XA\x10\x12\x12\x08\n\x04PETA\x10\x0f\x12\x08\n\x04TERA\x10\x0c\x12\x08\n\x04GIGA\x10\t\x12\x08\n\x04MEGA\x10\x06\x12\x08\n\x04KILO\x10\x03\x12\t\n\x05HECTO\x10\x02\x12\t\n\x05\x44\x45\x43\x41\x44\x10\x01\x12\t\n\x05UNITY\x10\x00\x12\x11\n\x04\x44\x45\x43I\x10\xff\xff\xff\xff\xff\xff\xff\xff\xff\x01\x12\x12\n\x05\x43\x45NTI\x10\xfe\xff\xff\xff\xff\xff\xff\xff\xff\x01\x12\x12\n\x05MILLI\x10\xfd\xff\xff\xff\xff\xff\xff\xff\xff\x01\x12\x12\n\x05MICRO\x10\xfa\xff\xff\xff\xff\xff\xff\xff\xff\x01\x12\x11\n\x04NANO\x10\xf7\xff\xff\xff\xff\xff\xff\xff\xff\x01\x12\x11\n\x04PICO\x10\xf4\xff\xff\xff\xff\xff\xff\xff\xff\x01\x12\x12\n\x05\x46\x45MTO\x10\xf1\xff\xff\xff\xff\xff\xff\xff\xff\x01\x12\x11\n\x04\x41TTO\x10\xee\xff\xff\xff\xff\xff\xff\xff\xff\x01\x12\x12\n\x05ZEPTO\x10\xeb\xff\xff\xff\xff\xff\xff\xff\xff\x01\x12\x12\n\x05YOCTO\x10\xe8\xff\xff\xff\xff\xff\xff\xff\xff\x01\x42\x02P\x01')

_globals = globals()
_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, _globals)
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'tunits.proto.tunits_pb2', _globals)
if _descriptor._USE_C_DESCRIPTORS == False:
  DESCRIPTOR._options = None
  DESCRIPTOR._serialized_options = b'P\001'
  _globals['_UNITENUM']._serialized_start=580
  _globals['_UNITENUM']._serialized_end=673
  _globals['_SCALE']._serialized_start=676
  _globals['_SCALE']._serialized_end=993
  _globals['_FRACTION']._serialized_start=37
  _globals['_FRACTION']._serialized_end=87
  _globals['_UNIT']._serialized_start=89
  _globals['_UNIT']._serialized_end=193
  _globals['_COMPLEX']._serialized_start=195
  _globals['_COMPLEX']._serialized_end=237
  _globals['_VALUE']._serialized_start=239
  _globals['_VALUE']._serialized_end=348
  _globals['_DOUBLEARRAY']._serialized_start=350
  _globals['_DOUBLEARRAY']._serialized_end=379
  _globals['_COMPLEXARRAY']._serialized_start=381
  _globals['_COMPLEXARRAY']._serialized_end=428
  _globals['_VALUEARRAY']._serialized_start=431
  _globals['_VALUEARRAY']._serialized_end=578
# @@protoc_insertion_point(module_scope)
