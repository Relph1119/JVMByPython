#!/usr/bin/env python
# encoding: utf-8
"""
@author: HuRuiFeng
@file: AttrLineNumberTable.py
@time: 2019/9/15 09:55
@desc: LineNumberTable属性表存放方法的行号信息
"""

from .AttributeInfo import AttributeInfo


class LineNumberTableAttribute(AttributeInfo):
    def __init__(self):
        self.lineNumberTable = []

    def read_info(self, class_reader):
        line_number_table_length = int.from_bytes(class_reader.read_unit16(), byteorder="big")
        self.lineNumberTable = [None for _ in range(line_number_table_length)]
        for i in range(line_number_table_length):
            line_number_table_entry = LineNumberTableEntry()
            line_number_table_entry.start_pc = int.from_bytes(class_reader.read_unit16(), byteorder="big")
            line_number_table_entry.line_number = int.from_bytes(class_reader.read_unit16(), byteorder="big")
            self.lineNumberTable[i] = line_number_table_entry

    def get_line_number(self, pc):
        for i in range(len(self.lineNumberTable) - 1, -1, -1):
            entry = self.lineNumberTable[i]
            if pc >= int(entry.start_pc):
                return int(entry.line_number)

        return -1


class LineNumberTableEntry():
    def __init__(self):
        self.start_pc = 0
        self.line_number = 0
