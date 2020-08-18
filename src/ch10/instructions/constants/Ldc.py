#!/usr/bin/env python
# encoding: utf-8
"""
@author: HuRuiFeng
@file: Ldc.py
@time: 2019/9/16 20:33
@desc: ldc系列指令从运行时常量池中加载常量值，并把它推入操作数栈。
ldc和ldc_w指令用于加载int、float和字符串常量，java.lang.Class实例或者MethodType和MethodHandle实例。
ldc2_w指令用于加载long和double常量。
"""
from ch10.instructions.base.Instruction import Index8Instruction, Index16Instruction
from ch10.rtda.Frame import Frame
from ch10.rtda.heap.CpClassRef import ClassRef
from ch10.rtda.heap.StringPool import j_string


def _ldc(frame: Frame, index):
    stack = frame.operand_stack
    clazz = frame.method.get_class()
    c = clazz.constant_pool.get_constant(index)

    if isinstance(c, int):
        stack.push_numeric(c)
    elif isinstance(c, float):
        stack.push_float(c)
    elif isinstance(c, str):
        # 从运行时常量池中加载字符串常量，先通过常量拿到python字符串，然后把它转成Java字符串实例
        interned_str = j_string(clazz.loader, c)
        # 把引用推入操作数栈顶
        stack.push_ref(interned_str)
    elif isinstance(c, ClassRef):
        class_obj = c.resolved_class().j_class
        stack.push_ref(class_obj)
    else:
        raise RuntimeError("todo: ldc!")


class LDC(Index8Instruction):
    def execute(self, frame):
        _ldc(frame, self.index)


class LDC_W(Index16Instruction):
    def execute(self, frame):
        _ldc(frame, self.index)


class LDC2_W(Index16Instruction):
    def execute(self, frame: Frame):
        stack = frame.operand_stack
        cp = frame.method.get_class().constant_pool
        c = cp.get_constant(self.index)

        if isinstance(c, int):
            stack.push_numeric(c)
        elif isinstance(c, float):
            stack.push_double(c)
        else:
            raise RuntimeError("java.lang.ClassFormatError")
