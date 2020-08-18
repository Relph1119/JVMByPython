#!/usr/bin/env python
# encoding: utf-8
"""
@author: HuRuiFeng
@file: CpMethodRef.py
@time: 2019/9/16 18:11
@desc: 方法符号引用
"""
from ch09.classfile.ConstantMemberRefInfo import ConstantMethodRefInfo
from ch09.rtda.heap import MethodLookup
from ch09.rtda.heap.ConstantPool import ConstantPool
from ch09.rtda.heap.CpMemberRef import MemberRef


class MethodRef(MemberRef):
    def __init__(self, constant_pool: ConstantPool, ref_info: ConstantMethodRefInfo):
        super(MethodRef, self).__init__()
        self.method = None
        self.cp = constant_pool
        self.copy_member_ref_info(ref_info)

    # 解析非接口方法
    def resolved_method(self):
        if self.method is None:
            self.resolve_method_ref()
        return self.method

    # 解析非接口方法符号引用
    def resolve_method_ref(self):
        """
        如果类D想通过方法符号引用访问类C的某个方法，先要解析符号引用得到类C。
        如果C是接口，则抛出IncompatibleClassChangeError异常，否则根据方法名和描述符查找方法。
        如果找不到对应方法，则抛出NoSuchMethodError异常，否则检查类D是否有权限访问该方法。
        如果没有，则抛出IllegalAccessError异常。
        :return:
        """
        d = self.cp.get_class()
        c = self.resolved_class()
        if c.is_interface():
            raise RuntimeError("java.lang.IncompatibleClassChangeError")

        method = self.lookup_method(c, self.name, self.descriptor)
        if method is None:
            raise RuntimeError("java.lang.NoSuchMethodError")
        if not method.is_accessible_to(d):
            raise RuntimeError("java.lang.IllegalAccessError")

        self.method = method

    # 根据方法名和描述符查找方法
    @staticmethod
    def lookup_method(clazz, name, descriptor):
        """
        先从C的继承层次中找，如果找不到，就去C的接口中找。
        :param clazz:
        :param name:
        :param descriptor:
        :return:
        """
        method = MethodLookup.lookup_method_in_class(clazz, name, descriptor)
        if method is None:
            method = MethodLookup.lookup_method_in_interfaces(clazz.interfaces, name, descriptor)
        return method
