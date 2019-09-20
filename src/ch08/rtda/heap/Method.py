#!/usr/bin/env python
# encoding: utf-8
"""
@author: HuRuiFeng
@file: Method.py
@time: 2019/9/16 16:55
@desc: 方法信息
"""
from classfile.MemberInfo import MemberInfo
from rtda.heap import AccessFlags
from rtda.heap.ClassMember import ClassMember
from rtda.heap.MethodDescriptorParser import MethodDescriptorParser


class Method(ClassMember):
    def __init__(self):
        super(Method, self).__init__()
        # 操作数栈
        self.max_stack = 0
        # 局部变量表大小
        self.max_locals = 0
        # 存放方法字节码
        self.code = []
        self.arg_slot_count = 0

    # 根据class文件中的方法信息创建Method表
    @staticmethod
    def new_method(clazz, cfMethods):
        methods = []
        for cfMethod in cfMethods:
            method = Method()
            method.set_class(clazz)
            method.copy_member_info(cfMethod)
            method.copy_attributes(cfMethod)
            method.calc_arg_slot_count()
            methods.append(method)
        return methods

    # 从method_info结构中提取max_stack、max_locals、code信息
    def copy_attributes(self, cfMethod: MemberInfo):
        code_attr = cfMethod.code_attribute
        if code_attr:
            self.max_stack = code_attr.max_stack
            self.max_locals = code_attr.max_locals
            self.code = code_attr.code

    # 计算参数在局部变量表中占用多少位置
    def calc_arg_slot_count(self):
        parsed_descriptor = MethodDescriptorParser.parse_method_descriptor(self.descriptor)
        for _ in parsed_descriptor.parameter_types:
            self.arg_slot_count += 1

        if not self.is_static():
            self.arg_slot_count += 1

    def is_synchronized(self):
        return 0 != self.access_flags & AccessFlags.ACC_SYNCHRONIZED

    def is_bridge(self):
        return 0 != self.access_flags & AccessFlags.ACC_BRIDGE

    def is_varargs(self):
        return 0 != self.access_flags & AccessFlags.ACC_VARARGS

    def is_native(self):
        return 0 != self.access_flags & AccessFlags.ACC_NATIVE

    def is_abstract(self):
        return 0 != self.access_flags & AccessFlags.ACC_ABSTRACT

    def is_strict(self):
        return 0 != self.access_flags & AccessFlags.ACC_STRICT
