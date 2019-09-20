#!/usr/bin/env python
# encoding: utf-8
"""
@author: HuRuiFeng
@file: CpFieldRef.py
@time: 2019/9/16 18:00
@desc: 字段符号引用
"""
from classfile.ConstantMemberRefInfo import ConstantFieldRefInfo
from rtda.heap.Class import Class
from rtda.heap.ConstantPool import ConstantPool
from rtda.heap.CpMemberRef import MemberRef


class FieldRef(MemberRef):
    def __init__(self, constant_pool: ConstantPool, ref_info: ConstantFieldRefInfo):
        super(FieldRef, self).__init__()
        self.field = None
        self.cp = constant_pool
        self.copy_member_ref_info(ref_info)

    # 字段解析
    def resolve_field(self):
        if self.field is None:
            self.resolve_field_ref()
        return self.field

    # 字段符号引用解析
    def resolve_field_ref(self):
        """
        如果类D想通过字段符号引用访问类C的某个字段，首先要解析符号引用得到类C，然后根据字段名和描述符查找字段。
        如果字段查找失败，则虚拟机排除NoSuchFieldError异常。
        如果查找成功，但D没有足够的权限访问该字段，则虚拟机抛出IllegalAccessError异常。
        :return:
        """
        d = self.cp.get_class()
        c = self.resolved_class()
        field = self.lookup_field(c, self.name, self.descriptor)

        if field is None:
            raise RuntimeError("java.lang.NoSuchFieldError")

        if not field.is_accessible_to(d):
            raise RuntimeError("java.lang.IllegalAccessError")

        self.field = field

    # 字段查找
    @staticmethod
    def lookup_field(c: Class, name, descriptor):
        """
        首先在C的字段中查找，如果找不到，在C的直接接口递归应用这个查找过程。
        如果还是找不到，在C的超类中递归应用这个查找过程。
        如果仍然找不到，则查找失败。
        :param c:
        :param name:
        :param descriptor:
        :return:
        """
        for field in c.fields:
            if field.name == name and field.descriptor == descriptor:
                return field

        for interface in c.interfaces:
            field = FieldRef.lookup_field(interface, name, descriptor)
            if field is not None:
                return field

        if c.super_class is not None:
            return FieldRef.lookup_field(c.super_class, name, descriptor)

        return None
