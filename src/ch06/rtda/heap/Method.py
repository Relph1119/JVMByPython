#!/usr/bin/env python
# encoding: utf-8
"""
@author: HuRuiFeng
@file: Method.py
@time: 2019/9/16 16:55
@desc: 方法信息
"""
from classfile.MemberInfo import MemberInfo
from rtda.heap.ClassMember import ClassMember


class Method(ClassMember):
    def __init__(self):
        super(Method, self).__init__()
        # 操作数栈
        self.max_stack = 0
        # 局部变量表大小
        self.max_locals = 0
        # 存放方法字节码
        self.code = []

    # 根据class文件中的方法信息创建Method表
    @staticmethod
    def new_methods(clazz, cfMethods):
        methods = []
        for cfMethod in cfMethods:
            method = Method()
            method.set_class(clazz)
            method.copy_member_info(cfMethod)
            method.copy_attributes(cfMethod)
            methods.append(method)
        return methods

    # 从method_info结构中提取max_stack、max_locals、code信息
    def copy_attributes(self, cfMethod: MemberInfo):
        code_attr = cfMethod.code_attribute
        if code_attr:
            self.max_stack = code_attr.max_stack
            self.max_locals = code_attr.max_locals
            self.code = code_attr.code
