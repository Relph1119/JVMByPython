#!/usr/bin/env python
# encoding: utf-8
"""
@author: HuRuiFeng
@file: AttrLocalVariableTypeTable.py
@time: 2019/9/15 10:01
@desc: LocalVariableTypeTable属性类型表中存放方法的局部变量类型信息
"""

from .AttributeInfo import AttributeInfo


class LocalVariableTypeTableAttribute(AttributeInfo):
    def __init__(self):
        self.localVariableTable = []

    def read_info(self, class_reader):
        local_variable_table_length = int.from_bytes(class_reader.read_unit16(), byteorder="big")
        self.localVariableTable = [None for _ in range(local_variable_table_length)]
        for i in range(local_variable_table_length):
            local_variable_type_table_entry = LocalVariableTypeTableEntry()
            local_variable_type_table_entry.start_pc = int.from_bytes(class_reader.read_unit16(), byteorder="big")
            local_variable_type_table_entry.length = int.from_bytes(class_reader.read_unit16(), byteorder="big")
            local_variable_type_table_entry.name_index = int.from_bytes(class_reader.read_unit16(), byteorder="big")
            local_variable_type_table_entry.signature_index = int.from_bytes(class_reader.read_unit16(),
                                                                             byteorder="big")
            local_variable_type_table_entry.index = int.from_bytes(class_reader.read_unit16(), byteorder="big")
            self.localVariableTable[i] = local_variable_type_table_entry


class LocalVariableTypeTableEntry:
    def __init__(self):
        self.start_pc = 0
        self.length = 0
        self.name_index = 0
        self.signature_index = 0
        self.index = 0
