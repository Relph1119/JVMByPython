#!/usr/bin/env python
# encoding: utf-8
"""
@author: HuRuiFeng
@file: MethodDescriptorParser.py
@time: 2019/9/16 09:27
@desc: 方法描述符解析器
"""

from rtda.heap.MethodDescriptor import MethodDescriptor


class MethodDescriptorParser:
    def __init__(self):
        self.raw = ""
        self.offset = 0
        self.parsed = None

    @staticmethod
    def parse_method_descriptor(descriptor):
        parser = MethodDescriptorParser()
        return parser.parse(descriptor)

    def parse(self, descriptor):
        self.raw = descriptor
        self.parsed = MethodDescriptor()
        self.start_params()
        self.parse_param_types()
        self.end_params()
        self.parse_return_type()
        self.finish()
        return self.parsed

    def start_params(self):
        if self.read_uint8() != '(':
            self.cause_panic()

    def end_params(self):
        if self.read_uint8() != ')':
            self.cause_panic()

    def finish(self):
        if self.offset != len(self.raw):
            self.cause_panic()

    def cause_panic(self):
        raise RuntimeError("BAD descriptor: {0}".format(self.raw))

    def read_uint8(self):
        b = self.raw[self.offset]
        self.offset += 1
        return b

    def unread_uint8(self):
        self.offset -= 1

    def parse_param_types(self):
        while True:
            t = self.parse_field_type()
            if t != "":
                self.parsed.add_parameter_type(t)
            else:
                break

    def parse_return_type(self):
        if self.read_uint8() == 'V':
            self.parsed.return_type = "V"
            return

        self.unread_uint8()
        t = self.parse_field_type()
        if t != "":
            self.parsed.return_type = t
            return

        self.cause_panic()

    def parse_field_type(self):
        field_type = self.read_uint8()
        if field_type == 'B':
            return 'B'
        elif field_type == 'C':
            return 'C'
        elif field_type == 'D':
            return 'D'
        elif field_type == 'F':
            return 'F'
        elif field_type == 'I':
            return 'I'
        elif field_type == 'J':
            return 'J'
        elif field_type == 'S':
            return 'S'
        elif field_type == 'Z':
            return 'Z'
        elif field_type == 'L':
            return self.parse_object_type()
        elif field_type == '[':
            return self.parse_array_type()
        else:
            self.unread_uint8()
            return ""

    def parse_object_type(self):
        unread = self.raw[self.offset:]
        semicolon_index = unread.find(";")
        if semicolon_index == -1:
            self.cause_panic()
            return ""
        else:
            obj_start = self.offset - 1
            obj_end = self.offset + semicolon_index + 1
            self.offset = obj_end
            # todo:
            # descriptor = copy.deepcopy(self.raw[obj_start:obj_end])
            descriptor = self.raw[obj_start:obj_end]
            return descriptor

    def parse_array_type(self):
        arr_start = self.offset - 1
        self.parse_field_type()
        arr_end = self.offset
        # todo:
        # descriptor = copy.deepcopy(self.raw[arr_start:arr_end])
        descriptor = self.raw[arr_start:arr_end]
        return descriptor
