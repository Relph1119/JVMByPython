#!/usr/bin/env python
# encoding: utf-8
"""
@author: HuRuiFeng
@file: Invokeinterface.py
@time: 2019/9/17 10:20
@desc: 接口调用指令
"""

import ctypes

from ch07.instructions.base import MethodInvokeLogic
from ch07.instructions.base.Instruction import Instruction
from ch07.rtda.heap import MethodLookup


class INVOKE_INTERFACE(Instruction):
    def __init__(self):
        self.index = 0

    def fetch_operands(self, reader):
        self.index = ctypes.c_uint(reader.read_uint16()).value
        reader.read_uint8()
        reader.read_uint8()

    def execute(self, frame):
        # 从运行时常量池中获得并解析接口方法符号引用
        cp = frame.method.get_class().constant_pool
        method_ref = cp.get_constant(self.index)
        resolve_method = method_ref.resolved_interface_method()
        # 如果解析后的方法是静态方法或私有方法，则抛出IncompatibleClassChangeError异常
        if resolve_method.is_static() or resolve_method.is_private():
            raise RuntimeError("java.lang.IncompatibleClassChangeError")

        # 从操作数中弹出this引用，如果引用是null，则抛出NullPointerException异常。
        # 如果引用所指对象的类没有实现解析出来的接口，则抛出IncompatibleClassChangeError异常。
        ref = frame.operand_stack.get_ref_from_top(resolve_method.arg_slot_count - 1)
        if ref is None:
            raise RuntimeError("java.lang.NullPointerException")

        if not ref.get_class().is_implements(method_ref.resolved_class()):
            raise RuntimeError("java.lang.IncompatibleClassChangeError")

        # 查找最终要调用的方法，如果找不到，或者找到的方法是抽象的，则抛出abstractMethodError异常。
        # 如果找到的方法不是public，则抛出IllegalAccessError异常。
        method_to_be_invoked = MethodLookup.lookup_method_in_class(
            ref.get_class(), method_ref.name, method_ref.descriptor)
        if not method_to_be_invoked or method_to_be_invoked.is_abstract():
            raise RuntimeError("java.lang.abstractMethodError")
        if not method_to_be_invoked.is_public():
            raise RuntimeError("java.lang.IllegalAccessError")

        MethodInvokeLogic.invoke_method(frame, method_to_be_invoked)
