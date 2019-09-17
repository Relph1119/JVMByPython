#!/usr/bin/env python
# encoding: utf-8
"""
@author: HuRuiFeng
@file: Class.py
@time: 2019/9/16 16:07
@desc: 类信息
"""
from classfile.ClassFile import ClassFile
from rtda.Slot import Slots
from rtda.heap import AccessFlags
from rtda.heap.ConstantPool import ConstantPool
from rtda.heap.Field import Field
from rtda.heap.Method import Method


class Class:
    def __init__(self):
        # 访问标志
        self.access_flags = 0
        # 类名（完全限定名），具有java/lang/Object的形式
        self.name = ""
        # 超类名（完全限定名）
        self.super_class_name = ""
        # 接口名（完全限定名）
        self.interface_names = []
        # 运行时常量池指针
        self.constant_pool = None
        # 字段表
        self.fields = []
        # 方法表
        self.methods = []
        # 加载器
        self.loader = None
        # 超类
        self.super_class = None
        # 接口
        self.interfaces = []
        # 实例变量所占空间
        self.instance_slot_count = 0
        # 类变量所占空间
        self.static_slot_count = 1
        # 静态变量
        self.static_vars = Slots()
        # 表示类的<clinit>方法是否已经开始执行
        self.init_started = False

    # 用来把classFile类转换成Class类
    @staticmethod
    def new_class(classFile: ClassFile):
        clazz = Class()
        clazz.access_flags = classFile.access_flags
        clazz.name = classFile.class_name
        clazz.super_class_name = classFile.super_class_name
        clazz.interface_names = classFile.interface_names
        clazz.constant_pool = ConstantPool.new_constant_pool(clazz, classFile.constant_pool)
        clazz.fields = Field.new_fields(clazz, classFile.fields)
        clazz.methods = Method.new_method(clazz, classFile.methods)
        return clazz

    # 用于判断public访问标志是否被设置
    def is_public(self):
        return 0 != self.access_flags & AccessFlags.ACC_PUBLIC

    # 用于判断final访问标志是否被设置
    def is_final(self):
        return 0 != self.access_flags & AccessFlags.ACC_FINAL

    # 用于判断super访问标志是否被设置
    def is_super(self):
        return 0 != self.access_flags & AccessFlags.ACC_SUPER

    # 用于判断interface访问标志是否被设置
    def is_interface(self):
        return 0 != self.access_flags & AccessFlags.ACC_INTERFACE

    # 用于判断abstract访问标志是否被设置
    def is_abstract(self):
        return 0 != self.access_flags & AccessFlags.ACC_ABSTRACT

    # 用于判断synthetic访问标志是否被设置
    def is_synthetic(self):
        return 0 != self.access_flags & AccessFlags.ACC_SYNTHETIC

    # 用于判断annotation访问标志是否被设置
    def is_annotation(self):
        return 0 != self.access_flags & AccessFlags.ACC_ANNOTATION

    # 用于判断enum访问标志是否被设置
    def is_enum(self):
        return 0 != self.access_flags & AccessFlags.ACC_ENUM

    # 类的访问控制权限
    def is_accessible_to(self, otherClass):
        """
        如果类D想访问类C，需要满足两个条件之一：C是pubilc，或者C和D在同一个运行时包内。
        :param otherClass:
        :return:
        """
        return self.is_public() or self.get_package_name() == otherClass.get_package_name()

    # 获取类所在的包名
    def get_package_name(self):
        i = self.name.rfind("/")
        if i >= 0:
            return self.name[:i]
        return ""

    def is_assignable_from(self, otherClass) -> bool:
        """
        在三种情况下，S类型的引用值可以赋值给T类型：S和T是同一类型；T是类且S是T的子类；或者T是接口且S实现了T接口
        :param otherClass:
        :return:
        """
        s, t = otherClass, self
        if s == t:
            return True

        if not t.is_interface():
            return s.is_sub_class_of(t)
        else:
            return s.is_implements(t)

    # 判断S是否是T的子类，也就是判断T是否是S的（直接或间接）超类
    def is_sub_class_of(self, otherClass):
        c = self.super_class
        while c:
            if c == otherClass:
                return True
            c = c.super_class

        return False

    # 判断S是否实现了T接口
    def is_implements(self, iface):
        c = self
        while c:
            for interface in c.interfaces:
                if interface == iface or interface.is_sub_interface_of(iface):
                    return True

        return False

    # 判断S是否实现了T的子接口
    def is_sub_interface_of(self, iface):
        for super_interface in self.interfaces:
            if super_interface == iface or super_interface.is_sub_interface_of(iface):
                return True

        return False

    # 判断S是否是T的超类
    def is_super_class_of(self, otherClass):
        return otherClass.is_sub_class_of(self)

    def get_main_method(self):
        return self.get_static_method("main", "([Ljava/lang/String;)V")

    def get_static_method(self, name, descriptor):
        for method in self.methods:
            if method.is_static() and method.name == name and method.descriptor == descriptor:
                return method
        return None

    def new_object(self):
        from rtda.heap.Object import Object
        return Object(self)

    def start_init(self):
        self.init_started = True

    def get_clinit_method(self):
        return self.get_static_method("<clinit>", "()V")
