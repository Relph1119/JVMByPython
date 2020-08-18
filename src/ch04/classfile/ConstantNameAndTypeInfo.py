#!/usr/bin/env python
# encoding: utf-8
"""
@author: HuRuiFeng
@file: ConstantNameAndTypeInfo.py
@time: 2019/9/15 00:24
@desc: 表示字段或方法的名称和描述符
"""

from ch04.classfile.ConstantInfo import ConstantInfo


class ConstantNameAndTypeInfo(ConstantInfo):
    def __init__(self):
        self.name_index = 0
        self.descriptor_index = 0

    def read_info(self, class_reader):
        self.name_index = int.from_bytes(class_reader.read_unit16(), byteorder="big")
        self.descriptor_index = int.from_bytes(class_reader.read_unit16(), byteorder="big")
