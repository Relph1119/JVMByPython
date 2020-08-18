#!/usr/bin/env python
# encoding: utf-8
"""
@author: HuRuiFeng
@file: AttrExceptions.py
@time: 2019/9/15 09:49
@desc: 记录方法抛出的异常表
"""

from ch06.classfile.AttributeInfo import AttributeInfo


class ExceptionsAttribute(AttributeInfo):
    def __init__(self):
        self.exception_index_table = []

    def read_info(self, class_reader):
        self.exception_index_table = class_reader.read_unit16s()
