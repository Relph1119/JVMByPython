#!/usr/bin/env python
# encoding: utf-8
"""
@author: HuRuiFeng
@file: Rem.py
@time: 2019/9/15 20:04
@desc: 求余(rem)指令
"""

import math

from instructions.base.Instruction import NoOperandsInstruction


# double remainder
class DREM(NoOperandsInstruction):
    def execute(self, frame):
        stack = frame.operand_stack
        v2 = stack.pop_double()
        v1 = stack.pop_double()
        if v2 == 0.0:
            result = math.nan
        else:
            result = math.fmod(v1, v2)
        stack.push_double(result)


# float remainder
class FREM(NoOperandsInstruction):
    def execute(self, frame):
        stack = frame.operand_stack
        v2 = stack.pop_float()
        v1 = stack.pop_float()
        if v2 == 0.0:
            result = math.nan
        else:
            result = math.fmod(v1, v2)
        stack.push_float(result)


# int remainder
class IREM(NoOperandsInstruction):
    def execute(self, frame):
        stack = frame.operand_stack
        v2 = stack.pop_numeric()
        v1 = stack.pop_numeric()
        if v2 == 0:
            raise RuntimeError("java.lang.ArithmeticException: / by zero")
        result = v1 % v2
        stack.push_numeric(result)


# long remainder
class LREM(NoOperandsInstruction):
    def execute(self, frame):
        stack = frame.operand_stack
        v2 = stack.pop_numeric()
        v1 = stack.pop_numeric()
        if v2 == 0:
            raise RuntimeError("java.lang.ArithmeticException: / by zero")
        result = v1 % v2
        stack.push_numeric(result)
