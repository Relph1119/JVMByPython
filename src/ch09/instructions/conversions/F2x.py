#!/usr/bin/env python
# encoding: utf-8
"""
@author: HuRuiFeng
@file: F2x.py
@time: 2019/9/15 20:38
@desc: float类型转换指令
"""

import ctypes

from ch09.instructions.base.Instruction import NoOperandsInstruction


# Convert float to double
class F2D(NoOperandsInstruction):
    def execute(self, frame):
        stack = frame.operand_stack
        f = stack.pop_float()
        d = float(f)
        stack.push_double(d)


# Convert float to int
class F2I(NoOperandsInstruction):
    def execute(self, frame):
        stack = frame.operand_stack
        f = stack.pop_float()
        i = int(f)
        stack.push_numeric(i)


# Convert float to long
class F2L(NoOperandsInstruction):
    def execute(self, frame):
        stack = frame.operand_stack
        f = stack.pop_float()
        l = int(f)
        stack.push_numeric(l)
