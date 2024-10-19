# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: mediapipe/calculators/tflite/ssd_anchors_calculator.proto
# Protobuf Python Version: 4.25.5
"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import symbol_database as _symbol_database
from google.protobuf.internal import builder as _builder
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


from mediapipe.framework import calculator_pb2 as mediapipe_dot_framework_dot_calculator__pb2
try:
  mediapipe_dot_framework_dot_calculator__options__pb2 = mediapipe_dot_framework_dot_calculator__pb2.mediapipe_dot_framework_dot_calculator__options__pb2
except AttributeError:
  mediapipe_dot_framework_dot_calculator__options__pb2 = mediapipe_dot_framework_dot_calculator__pb2.mediapipe.framework.calculator_options_pb2
from mediapipe.framework.formats.object_detection import anchor_pb2 as mediapipe_dot_framework_dot_formats_dot_object__detection_dot_anchor__pb2


DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n9mediapipe/calculators/tflite/ssd_anchors_calculator.proto\x12\tmediapipe\x1a$mediapipe/framework/calculator.proto\x1a\x39mediapipe/framework/formats/object_detection/anchor.proto\"\xd7\x05\n\x1bSsdAnchorsCalculatorOptions\x12\x18\n\x10input_size_width\x18\x01 \x01(\x05\x12\x19\n\x11input_size_height\x18\x02 \x01(\x05\x12\x11\n\tmin_scale\x18\x03 \x01(\x02\x12\x11\n\tmax_scale\x18\x04 \x01(\x02\x12\x1c\n\x0f\x61nchor_offset_x\x18\x05 \x01(\x02:\x03\x30.5\x12\x1c\n\x0f\x61nchor_offset_y\x18\x06 \x01(\x02:\x03\x30.5\x12\x12\n\nnum_layers\x18\x07 \x01(\x05\x12\x19\n\x11\x66\x65\x61ture_map_width\x18\x08 \x03(\x05\x12\x1a\n\x12\x66\x65\x61ture_map_height\x18\t \x03(\x05\x12\x0f\n\x07strides\x18\n \x03(\x05\x12\x15\n\raspect_ratios\x18\x0b \x03(\x02\x12+\n\x1creduce_boxes_in_lowest_layer\x18\x0c \x01(\x08:\x05\x66\x61lse\x12*\n\x1finterpolated_scale_aspect_ratio\x18\r \x01(\x02:\x01\x31\x12 \n\x11\x66ixed_anchor_size\x18\x0e \x01(\x08:\x05\x66\x61lse\x12+\n\x1cmultiscale_anchor_generation\x18\x0f \x01(\x08:\x05\x66\x61lse\x12\x14\n\tmin_level\x18\x10 \x01(\x05:\x01\x33\x12\x14\n\tmax_level\x18\x11 \x01(\x05:\x01\x37\x12\x17\n\x0c\x61nchor_scale\x18\x12 \x01(\x02:\x01\x34\x12\x1c\n\x11scales_per_octave\x18\x13 \x01(\x05:\x01\x32\x12#\n\x15normalize_coordinates\x18\x14 \x01(\x08:\x04true\x12(\n\rfixed_anchors\x18\x15 \x03(\x0b\x32\x11.mediapipe.Anchor2T\n\x03\x65xt\x12\x1c.mediapipe.CalculatorOptions\x18\xff\xb8\xf3u \x01(\x0b\x32&.mediapipe.SsdAnchorsCalculatorOptions')

_globals = globals()
_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, _globals)
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'mediapipe.calculators.tflite.ssd_anchors_calculator_pb2', _globals)
if _descriptor._USE_C_DESCRIPTORS == False:
  DESCRIPTOR._options = None
  _globals['_SSDANCHORSCALCULATOROPTIONS']._serialized_start=170
  _globals['_SSDANCHORSCALCULATOROPTIONS']._serialized_end=897
# @@protoc_insertion_point(module_scope)
