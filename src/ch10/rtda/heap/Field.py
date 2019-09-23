#!/usr/bin/env python
# encoding: utf-8
"""
@author: HuRuiFeng
@file: Field.py
@time: 2019/9/16 16:49
@desc: 字段信息
"""
from classfile.MemberInfo import MemberInfo
from rtda.heap import AccessFlags
from rtda.heap.ClassMember import ClassMember


class Field(ClassMember):
    def __init__(self):
        super(Field, self).__init__()
        self.const_value_index = 0
        self.slot_id = 0

    # 根据class文件的字段信息创建字段表
    @staticmethod
    def new_fields(clazz, cfFields):
        fields = []
        for cfField in cfFields:
            field = Field()
            field.set_class(clazz)
            field.copy_member_info(cfField)
            field.copy_attributes(cfField)
            fields.append(field)
        return fields

    # 用于判断volatile访问标志是否被设置
    def is_volatile(self):
        return 0 != self.access_flags & AccessFlags.ACC_VOLATILE

    # 用于判断transient访问标志是否被设置
    def is_transient(self):
        return 0 != self.access_flags & AccessFlags.ACC_TRANSIENT

    # 用于判断enum访问标志是否被设置
    def is_enum(self):
        return 0 != self.access_flags & AccessFlags.ACC_ENUM

    # 从method_info结构中提取constant_value_index信息
    def copy_attributes(self, cfField: MemberInfo):
        val_attr = cfField.constant_value_attribute
        if val_attr:
            self.const_value_index = val_attr.constant_value_index
