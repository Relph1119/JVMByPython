#!/usr/bin/env python
# encoding: utf-8
"""
@author: HuRuiFeng
@file: CpInterfaceMethodRef.py
@time: 2019/9/16 18:13
@desc: 接口方法符号引用
"""
from ch09.classfile.ConstantMemberRefInfo import ConstantInterfaceMethodRefInfo
from ch09.rtda.heap import MethodLookup
from ch09.rtda.heap.ConstantPool import ConstantPool
from ch09.rtda.heap.CpMemberRef import MemberRef


class InterfaceMethodRef(MemberRef):
    def __init__(self, constant_pool: ConstantPool, ref_info: ConstantInterfaceMethodRefInfo):
        super().__init__()
        self.method = None
        self.cp = constant_pool
        self.copy_member_ref_info(ref_info)

    # 解析接口方法
    def resolved_interface_method(self):
        if self.method is None:
            self.resolve_interface_method_ref()
        return self.method

    # 解析接口方法符号引用
    def resolve_interface_method_ref(self):
        d = self.cp.get_class
        c = self.resolved_class()
        if not c.is_interface():
            raise RuntimeError("java.lang.IncompatibleClassChangeError")

        method = self.lookup_interface_method(c, self.name, self.descriptor)
        if method is None:
            raise RuntimeError("java.lang.NoSuchMethodError")
        if not method.is_accessible_to(d):
            raise RuntimeError("java.lang.IllegalAccessError")

        self.method = method

    # 根据方法名和描述符查找接口方法
    @staticmethod
    def lookup_interface_method(iface, name, descriptor):
        for method in iface.methods:
            if method.name == name and method.descriptor == descriptor:
                return method

        return MethodLookup.lookup_method_in_interfaces(iface.interfaces, name, descriptor)
