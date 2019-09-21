#!/usr/bin/env python
# encoding: utf-8
"""
@author: HuRuiFeng
@file: Invokespecial.py
@time: 2019/9/16 20:55
@desc: invokespecial指令用于调用构造函数初始化对象
"""
from instructions.base import MethodInvokeLogic
from instructions.base.Instruction import Index16Instruction
from rtda.Frame import Frame
from rtda.heap import MethodLookup


class INVOKE_SPECIAL(Index16Instruction):
    def execute(self, frame: Frame):
        # 获得当前类、当前常量池、方法符号引用
        current_class = frame.method.get_class()
        cp = current_class.constant_pool
        method_ref = cp.get_constant(self.index)
        # 解析符号引用，得到解析后的类和方法
        resolved_class = method_ref.resolved_class()
        resolved_method = method_ref.resolved_method()

        # 假设从方法符号引用中解析出来的类是C，方法是M。
        # 如果M是构造函数，则声明M的类必须是C，否则抛出NoSuchMethodError异常。
        # 如果M是静态方法，则抛出IncompatibleClassChangeError异常。
        if resolved_method.name == "<init>" and resolved_method.get_class() != resolved_class:
            raise RuntimeError("java.lang.NoSuchMethodError")
        if resolved_method.is_static():
            raise RuntimeError("java.lang.IncompatibleClassChangeError")

        # 从操作数栈中弹出this引用，如果该引用是null，抛出NullPointerException异常。
        ref = frame.operand_stack.get_ref_from_top(resolved_method.arg_slot_count - 1)
        if ref is None:
            raise RuntimeError("java.lang.NullPointerException")

        # 确保protected方法只能被声明该方法的类或子类调用，如果违反这一规定，则抛出IllegalAccessError异常。
        if resolved_method.is_protected() \
                and resolved_method.get_class().is_super_class_of(current_class) \
                and resolved_method.get_class().get_package_name() != current_class.get_package_name() \
                and ref.get_class() != current_class \
                and not ref.get_class().is_sub_class_of(current_class):
            raise RuntimeError("java.lang.IllegalAccessError")

        # 如果调用超类中函数，但不是构造函数，且当前类的ACC_SUPER标志被设置，需要一个额外的过程查找最终要调用的方法，
        # 否则签名从方法符号引用中解析出来的方法就是要调用的方法。
        method_to_be_invoked = resolved_method
        if current_class.is_super() \
                and resolved_class.is_super_class_of(current_class) \
                and resolved_method.name != "<init>":
            method_to_be_invoked = MethodLookup.lookup_method_in_class(
                current_class.super_class, method_ref.name, method_ref.descriptor)

        # 如果查找过程失败，或者找到的方法是抽象的，抛出abstractMethodError异常。
        if not method_to_be_invoked or method_to_be_invoked.is_abstract():
            raise RuntimeError("java.lang.AbstractMethodError")

        MethodInvokeLogic.invoke_method(frame, method_to_be_invoked)
