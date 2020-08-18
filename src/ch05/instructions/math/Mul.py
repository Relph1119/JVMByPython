#!/usr/bin/env python
# encoding: utf-8
"""
@author: HuRuiFeng
@file: Mul.py
@time: 2019/9/15 20:00
@desc: 乘法(mul)指令
"""
from ch05.instructions.base.Instruction import NoOperandsInstruction


def _mul(frame):
    stack = frame.operand_stack
    v2 = stack.pop_numeric()
    v1 = stack.pop_numeric()
    result = v1 * v2
    stack.push_numeric(result)


# double mul
class DMUL(NoOperandsInstruction):
    def execute(self, frame):
        _mul(frame)


# float mul
class FMUL(NoOperandsInstruction):
    def execute(self, frame):
        _mul(frame)


# int mul
class IMUL(NoOperandsInstruction):
    def execute(self, frame):
        _mul(frame)


# long mul
class LMUL(NoOperandsInstruction):
    def execute(self, frame):
        _mul(frame)
