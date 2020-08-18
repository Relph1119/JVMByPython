#!/usr/bin/env python
# encoding: utf-8
"""
@author: HuRuiFeng
@file: UnparsedAttribute.py
@time: 2019/9/15 09:37
@desc: 未解析的属性
"""

from classfile.AttributeInfo import AttributeInfo


class UnparsedAttribute(AttributeInfo):
    def __init__(self, attr_name, attr_len):
        self.name = attr_name
        self.length = attr_len
        self.info = []

    def read_info(self, class_reader):
        self.info = class_reader.read_bytes(self.length)
