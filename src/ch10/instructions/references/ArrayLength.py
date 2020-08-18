#!/usr/bin/env python
# encoding: utf-8
"""
@author: HuRuiFeng
@file: ArrayLength.py
@time: 2019/9/17 21:31
@desc: arraylength指令用于获取数组长度，只需要一个操作数，即从操作数栈顶弹出的数组引用。
"""
from ch10.instructions.base.Instruction import NoOperandsInstruction
from ch10.rtda.Frame import Frame


class ARRAY_LENGTH(NoOperandsInstruction):
    def execute(self, frame: Frame):
        stack = frame.operand_stack
        arr_ref = stack.pop_ref()
        # 如果数组引用是null，则抛出NullPointerException异常
        if arr_ref is None:
            raise RuntimeError("java.lang.NullPointerException")

        # 否则获得数组长度，推入操作数栈
        arr_len = arr_ref.array_length()
        stack.push_numeric(arr_len)
