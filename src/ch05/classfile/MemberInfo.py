#!/usr/bin/env python
# encoding: utf-8
"""
@author: HuRuiFeng
@file: MemberInfo.py
@time: 2019/9/14 22:49
@desc: 统一的类表示字段和方法
"""
from classfile.AttrCode import CodeAttribute


class MemberInfo():
    def __init__(self, constant_pool):
        self.cp = constant_pool
        self.access_flags = ""
        self.name_index = ""
        self.descriptor_index = ""
        self.attributes = []

    # 读取字段表或方法表
    def read_members(self, class_reader, constant_pool):
        member_count = int.from_bytes(class_reader.read_unit16(), byteorder='big')
        members = []
        for i in range(member_count):
            members.append(self.read_member(class_reader, constant_pool))
        return members

    # 读取字段或方法数据
    @staticmethod
    def read_member(class_reader, constant_pool):
        from .AttributeInfo import AttributeInfo

        # 初始化MemberInfo对象
        member = MemberInfo(constant_pool)
        member.access_flags = class_reader.read_unit16()
        member.name_index = int.from_bytes(class_reader.read_unit16(), byteorder="big")
        member.descriptor_index = int.from_bytes(class_reader.read_unit16(), byteorder="big")
        member.attributes = AttributeInfo.read_attributes(class_reader, constant_pool)
        return member

    # 从常量池查找字段或方法名
    @property
    def name(self):
        return self.cp.get_utf8(self.name_index)

    # 从常量池查找字段或方法描述符
    @property
    def descriptor(self):
        return self.cp.get_utf8(self.descriptor_index)

    # 得到MemberInfo的Code属性
    @property
    def code_attribute(self):
        for attrInfo in self.attributes:

            if isinstance(attrInfo, CodeAttribute):
                return attrInfo

        return None
