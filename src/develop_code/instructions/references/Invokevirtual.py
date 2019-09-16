#!/usr/bin/env python
# encoding: utf-8
"""
@author: HuRuiFeng
@file: Invokevirtual.py
@time: 2019/9/16 20:57
@desc: invokevirtual用于打印计算结果
"""

from instructions.base.Instruction import Index16Instruction
from rtda.Frame import Frame


class INVOKE_VIRTURL(Index16Instruction):
    def execute(self, frame: Frame):
        cp = frame.method.get_class().constant_pool
        method_ref = cp.get_constant(self.index)
        if method_ref.name == "println":
            stack = frame.operand_stack
            descriptor = method_ref.descriptor
            if descriptor == "(Z)V":
                print("{0}".format(stack.pop_numeric() != 0))
            elif descriptor in {"(C)V", "(B)V", "(S)V", "(I)V", "(J)V", "(F)V", "(D)V"}:
                print("{0}".format(stack.pop_numeric()))
            else:
                raise RuntimeError("println: " + method_ref.descriptor)
            stack.pop_ref()
