#!/usr/bin/env python
# encoding: utf-8
"""
@author: HuRuiFeng
@file: ConstantPool.py
@time: 2019/9/14 22:56
@desc: 常量池类
"""


class ConstantPool:
    def __init__(self, cp=None):
        if cp is None:
            cp = []
        self.cp = cp

    def read_constant_pool(self, class_reader):
        from .CpNumeric import ConstantLongInfo, ConstantDoubleInfo
        from .ConstantInfo import ConstantInfo

        cp_count = int.from_bytes(class_reader.read_unit16(), byteorder="big")
        self.cp = [0 for i in range(cp_count)]

        # 索引从1开始
        i = 1
        while i < cp_count:
            self.cp[i] = ConstantInfo.read_constant_info(class_reader, self.cp)
            if isinstance(self.cp[i], ConstantLongInfo) or isinstance(self.cp[i], ConstantDoubleInfo):
                i += 1
            i += 1

    def get_constant_info(self, index):
        cp_info = self.cp[index]
        if cp_info:
            return cp_info
        else:
            raise RuntimeError("Invalid constant pool index!")

    def get_name_and_type(self, index):
        nt_info = self.get_constant_info(index)
        name = self.get_utf8(nt_info.name_index)
        _type = self.get_utf8(nt_info.descriptor_index)
        return name, _type

    def get_class_name(self, index):
        class_info = self.get_constant_info(index)
        return self.get_utf8(class_info.name_index)

    def get_utf8(self, index):
        utf8_info = self.get_constant_info(index)
        return utf8_info.str

    def __len__(self):
        return len(self.cp)