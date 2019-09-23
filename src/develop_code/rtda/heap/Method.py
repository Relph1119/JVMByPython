#!/usr/bin/env python
# encoding: utf-8
"""
@author: HuRuiFeng
@file: Method.py
@time: 2019/9/16 16:55
@desc: 方法信息
"""
from classfile.AttrLineNumberTable import LineNumberTableAttribute
from classfile.MemberInfo import MemberInfo
from rtda.heap import AccessFlags, ExceptionTable
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
        # 异常处理表
        self.exception_table = ExceptionTable.ExceptionTable()
        # 行号表
        self.line_number_table = LineNumberTableAttribute()
        self.arg_slot_count = 0

    # 根据class文件中的方法信息创建Method表
    @staticmethod
    def new_methods(clazz, cfMethods):
        methods = []
        for cfMethod in cfMethods:
            method = Method.new_method(clazz, cfMethod)
            methods.append(method)
        return methods

    @staticmethod
    def new_method(clazz, cfMethod):
        method = Method()
        method.set_class(clazz)
        method.copy_member_info(cfMethod)
        method.copy_attributes(cfMethod)
        md = MethodDescriptorParser.parse_method_descriptor(method.descriptor)
        # 先计算arg_slot_count字段
        method.calc_arg_slot_count(md.parameter_types)
        # 如果是本地方法，则注入字节码和其他信息。
        if method.is_native():
            method.inject_code_attribute(md.return_type)

        return method

    def inject_code_attribute(self, return_type):
        # 由于本地方法在class文件中没有Code属性，所以需要给max_stack和max_locals赋值。
        self.max_stack = 4
        self.max_locals = self.arg_slot_count
        # code字段是本地方法的字节码，第一条指令都是0xfe，第二条指令则根据函数的返回值选择相应的返回指令。
        if return_type[0] == 'V':
            # 对应指令return
            self.code = [0xfe, 0xb1]
        elif return_type[0] == 'D':
            # 对应指令dreturn
            self.code = [0xfe, 0xaf]
        elif return_type[0] == 'F':
            # 对应指令freturn
            self.code = [0xfe, 0xae]
        elif return_type[0] == 'J':
            # 对应指令lreturn
            self.code = [0xfe, 0xad]
        elif return_type[0] in {'L', '['}:
            # 对应指令areturn
            self.code = [0xfe, 0xb0]
        else:
            # 对应指令ireturn
            self.code = [0xfe, 0xac]

    # 从method_info结构中提取max_stack、max_locals、code信息
    def copy_attributes(self, cfMethod: MemberInfo):
        code_attr = cfMethod.code_attribute
        if code_attr:
            self.max_stack = code_attr.max_stack
            self.max_locals = code_attr.max_locals
            self.code = code_attr.code
            # 从class文件中提取行号表
            self.line_number_table = code_attr.line_number_table_attribute()
            # 复制异常处理表
            self.exception_table.exception_table = ExceptionTable.new_exception_table(code_attr.exception_table,
                                                                                      self.get_class().constant_pool)

    # 计算参数在局部变量表中占用多少位置
    def calc_arg_slot_count(self, param_types):
        for _, param_type in enumerate(param_types):
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

    def find_exception_handler(self, exClass, pc):
        """
        调用ExceptionTable.find_exception_handler()方法搜索异常处理表，
        如果能找到对应的异常处理项，则返回它的handler_pc字段，否则返回-1
        :param exClass:
        :param pc:
        :return:
        """
        handler = self.exception_table.find_exception_handler(exClass, pc)
        if handler is not None:
            return handler.handler_pc

        return -1

    def get_line_number(self, pc):
        """
        和源文件名一样，并不是每个方法都有行号表。
        如果方法没有行号表，查不到pc对应的行号，返回-1。
        本地方法没有字节码，返回-2。
        剩下情况调用LineNumberTableAttribute的get_line_number()方法查找行号。
        :param pc:
        :return:
        """
        if self.is_native():
            return -2

        if self.line_number_table is None:
            return -1

        return self.line_number_table.get_line_number(pc)
