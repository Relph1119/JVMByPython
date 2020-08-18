#!/usr/bin/env python
# encoding: utf-8
"""
@author: HuRuiFeng
@file: ConstantMemberRefInfo.py
@time: 2019/9/15 00:18
@desc: 对象引用类
"""

from ch08.classfile.ConstantInfo import ConstantInfo


class ConstantMemberRefInfo(ConstantInfo):
    def __init__(self, constant_pool):
        from ch08.classfile.ConstantPool import ConstantPool
        self.cp = ConstantPool(constant_pool)
        self.class_index = 0
        self.name_and_type_index = 0

    def read_info(self, class_reader):
        self.class_index = int.from_bytes(class_reader.read_unit16(), byteorder="big")
        self.name_and_type_index = int.from_bytes(class_reader.read_unit16(), byteorder="big")

    @property
    def class_name(self):
        return self.cp.get_class_name(self.class_index)

    @property
    def name_and_descriptor(self):
        return self.cp.get_name_and_type(self.name_and_type_index)


# 字段符号引用类
class ConstantFieldRefInfo(ConstantMemberRefInfo):
    def __init__(self, constant_pool):
        super(ConstantFieldRefInfo, self).__init__(constant_pool)


# 普通（非接口）方法符号引用类
class ConstantMethodRefInfo(ConstantMemberRefInfo):
    def __init__(self, constant_pool):
        super(ConstantMethodRefInfo, self).__init__(constant_pool)


# 接口方法符号引用类
class ConstantInterfaceMethodRefInfo(ConstantMemberRefInfo):
    def __init__(self, constant_pool):
        super(ConstantInterfaceMethodRefInfo, self).__init__(constant_pool)
