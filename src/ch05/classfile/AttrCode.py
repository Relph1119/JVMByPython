#!/usr/bin/env python
# encoding: utf-8
"""
@author: HuRuiFeng
@file: AttrCode.py
@time: 2019/9/15 09:49
@desc: Code属性存放字节码等方法相关信息
"""

from ch05.classfile.AttributeInfo import AttributeInfo


class CodeAttribute(AttributeInfo):
    def __init__(self, constant_pool):
        self.cp = constant_pool
        # 操作数栈的最大深度
        self.max_stack = 0
        # 局部变量表大小
        self.max_locals = 0
        # 字节码，存在u1表中
        self.code = None
        # 异常处理表
        self.exception_table = []
        # 属性表
        self.attributes = []

    def read_info(self, class_reader):
        self.max_stack = int.from_bytes(class_reader.read_unit16(), byteorder="big")
        self.max_locals = int.from_bytes(class_reader.read_unit16(), byteorder="big")
        code_length = int.from_bytes(class_reader.read_unit32(), byteorder="big")
        self.code = class_reader.read_bytes(code_length)
        self.exception_table = self.read_exception_table(class_reader)
        self.attributes = AttributeInfo.read_attributes(class_reader, self.cp)

    @staticmethod
    def read_exception_table(class_reader):
        exception_table_length = int.from_bytes(class_reader.read_unit16(), byteorder="big")
        exception_table = []
        for _ in range(exception_table_length):
            exception_table_entry = ExceptionTableEntry()
            exception_table_entry.start_pc = int.from_bytes(class_reader.read_unit16(), byteorder="big")
            exception_table_entry.end_pc = int.from_bytes(class_reader.read_unit16(), byteorder="big")
            exception_table_entry.handler_pc = int.from_bytes(class_reader.read_unit16(), byteorder="big")
            exception_table_entry.catch_type = int.from_bytes(class_reader.read_unit16(), byteorder="big")
            exception_table.append(exception_table_entry)
        return exception_table


# 异常处理表实体类
class ExceptionTableEntry:
    def __init__(self):
        self.start_pc = 0
        self.end_pc = 0
        self.handler_pc = 0
        self.catch_type = 0
