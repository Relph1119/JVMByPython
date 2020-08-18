#!/usr/bin/env python
# encoding: utf-8
"""
@author: HuRuiFeng
@file: AttrConstantValue.py
@time: 2019/9/15 09:49
@desc: 用于表示常量表达式的值
"""

from classfile.AttributeInfo import AttributeInfo


class ConstantValueAttribute(AttributeInfo):
    def __init__(self):
        self.constant_value_index = 0

    def read_info(self, class_reader):
        self.constant_value_index = int.from_bytes(class_reader.read_unit16(), byteorder="big")
