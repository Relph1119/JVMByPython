#!/usr/bin/env python
# encoding: utf-8
"""
@author: HuRuiFeng
@file: D2x.py
@time: 2019/9/15 20:36
@desc: double类型转换指令
"""

import ctypes

from instructions.base.Instruction import NoOperandsInstruction


# Convert double to float
class D2F(NoOperandsInstruction):
    def execute(self, frame):
        stack = frame.operand_stack
        d = stack.pop_double()
        f = ctypes.c_float(d).value
        stack.push_float(f)


# Convert double to int
class D2I(NoOperandsInstruction):
    def execute(self, frame):
        stack = frame.operand_stack
        d = stack.pop_double()
        i = int(d)
        stack.push_numeric(i)


# Convert double to long
class D2L(NoOperandsInstruction):
    def execute(self, frame):
        stack = frame.operand_stack
        d = stack.pop_double()
        l = int(d)
        stack.push_numeric(l)
