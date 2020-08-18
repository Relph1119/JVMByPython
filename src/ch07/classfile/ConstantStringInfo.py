#!/usr/bin/env python
# encoding: utf-8
"""
@author: HuRuiFeng
@file: ConstantStringInfo.py
@time: 2019/9/15 00:18
@desc: 表示java.lang.String字面量
"""

from ch07.classfile.ConstantInfo import ConstantInfo


class ConstantStringInfo(ConstantInfo):
    def __init__(self, constant_pool):
        from ch07.classfile.ConstantPool import ConstantPool
        self.cp = ConstantPool(constant_pool)
        self.string_index = ""

    # 读取常量池索引
    def read_info(self, class_reader):
        self.string_index = int.from_bytes(class_reader.read_unit16(), byteorder="big")

    # 按索引从常量池中查找字符串
    def __str__(self):
        return self.cp.get_utf8(self.string_index)
