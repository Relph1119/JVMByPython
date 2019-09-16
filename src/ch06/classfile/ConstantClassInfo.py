#!/usr/bin/env python
# encoding: utf-8
"""
@author: HuRuiFeng
@file: ConstantClassInfo.py
@time: 2019/9/15 00:22
@desc: 表示类或者接口的符号引用
"""

from .ConstantInfo import ConstantInfo


class ConstantClassInfo(ConstantInfo):
    def __init__(self, constant_pool):
        from classfile.ConstantPool import ConstantPool
        self.cp = ConstantPool(constant_pool)
        self.name_index = 0

    def read_info(self, class_reader):
        self.name_index = int.from_bytes(class_reader.read_unit16(), byteorder="big")

    @property
    def name(self):
        return self.cp.get_utf8(self.name_index)
