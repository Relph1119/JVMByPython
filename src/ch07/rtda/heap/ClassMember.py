#!/usr/bin/env python
# encoding: utf-8
"""
@author: HuRuiFeng
@file: ClassMember.py
@time: 2019/9/16 16:33
@desc: 类成员信息，由于字段和方法都属于类的成员，它们有一些相同的信息（访问标志、名字、描述符）。
"""
from ch07.rtda.heap import AccessFlags


class ClassMember:
    def __init__(self):
        # 访问标志
        self.access_flags = 0
        # 名字
        self.name = ""
        # 描述符
        self.descriptor = ""
        # 存放Class类指针
        self._class = None

    # 从class文件中复制数据
    def copy_member_info(self, member_info):
        self.access_flags = member_info.access_flags
        self.name = member_info.name
        self.descriptor = member_info.descriptor

    def set_class(self, clazz):
        self._class = clazz

    def get_class(self):
        return self._class

    # 用于判断public访问标志是否被设置
    def is_public(self):
        return 0 != self.access_flags & AccessFlags.ACC_PUBLIC

    # 用于判断private访问标志是否被设置
    def is_private(self):
        return 0 != self.access_flags & AccessFlags.ACC_PRIVATE

    # 用于判断protected访问标志是否被设置
    def is_protected(self):
        return 0 != self.access_flags & AccessFlags.ACC_PROTECTED

    # 用于判断static访问标志是否被设置
    def is_static(self):
        return 0 != self.access_flags & AccessFlags.ACC_STATIC

    # 用于判断final访问标志是否被设置
    def is_final(self):
        return 0 != self.access_flags & AccessFlags.ACC_FINAL

    # 用于判断synthetic访问标志是否被设置
    def is_synthetic(self):
        return 0 != self.access_flags & AccessFlags.ACC_SYNTHETIC

    # 类成员的访问控制规则
    def is_accessible_to(self, d):
        """
        如果字段是public，这任何类都可以访问。
        如果字段是protected，则只有子类和同一包下的类可以访问。
        如果字段有默认访问权限（非public，非protected，也非private），则只有同一个包下的类可以访问。
        否则，字段是private，只有声明这个字段的类才能访问
        :param d:
        :return:
        """
        if self.is_public():
            return True

        c = self._class
        if self.is_protected():
            return d == c or d.is_sub_class_of(c) or c.get_package_name() == d.get_package_name()

        if not self.is_private():
            return c.get_package_name() == d.get_package_name()

        return d == c
