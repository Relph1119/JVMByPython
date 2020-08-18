#!/usr/bin/env python
# encoding: utf-8
"""
@author: HuRuiFeng
@file: Checkcast.py
@time: 2019/9/16 20:22
@desc: checkcast指令和instanceof指令很像，区别在于：instanceof指令会改变操作数栈（弹出对象引用，推入判断结果）；
checkcast指令则不会改变操作数栈（如果判断失败，直接抛出ClassCastException异常）
"""
from ch06.instructions.base.Instruction import Index16Instruction
from ch06.rtda.Frame import Frame


class CHECK_CAST(Index16Instruction):
    def execute(self, frame:Frame):
        stack = frame.operand_stack
        ref = stack.pop_ref()
        stack.push_ref(ref)
        if ref is None:
            return

        cp = frame.method.get_class().constant_pool
        class_ref = cp.get_constant(self.index)
        clazz = class_ref.resolved_class()
        if not ref.is_instance_of(clazz):
            raise RuntimeError("java.lang.ClassCastException")
