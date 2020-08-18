#!/usr/bin/env python
# encoding: utf-8
"""
@author: HuRuiFeng
@file: L2x.py
@time: 2019/9/15 20:46
@desc: long类型转换指令
"""

import ctypes

from ch07.instructions.base.Instruction import NoOperandsInstruction


# Convert long to double
class L2D(NoOperandsInstruction):
    def execute(self, frame):
        stack = frame.operand_stack
        l = stack.pop_numeric()
        d = ctypes.c_float(l).value
        stack.push_numeric(d)


# Convert long to float
class L2F(NoOperandsInstruction):
    def execute(self, frame):
        stack = frame.operand_stack
        l = stack.pop_numeric()
        f = ctypes.c_float(l).value
        stack.push_numeric(f)


# Convert long to int
class L2I(NoOperandsInstruction):
    def execute(self, frame):
        stack = frame.operand_stack
        l = stack.pop_numeric()
        i = ctypes.c_int32(l).value
        stack.push_numeric(i)
