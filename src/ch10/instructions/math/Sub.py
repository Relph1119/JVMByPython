#!/usr/bin/env python
# encoding: utf-8
"""
@author: HuRuiFeng
@file: Sub.py
@time: 2019/9/15 19:59
@desc: 减法(sub)指令
"""
from ch10.instructions.base.Instruction import NoOperandsInstruction


def _sub(frame):
    stack = frame.operand_stack
    v2 = stack.pop_numeric()
    v1 = stack.pop_numeric()
    result = v1 - v2
    stack.push_numeric(result)


# double sub
class DSUB(NoOperandsInstruction):
    def execute(self, frame):
        stack = frame.operand_stack
        v2 = stack.pop_double()
        v1 = stack.pop_double()
        result = v1 - v2
        stack.push_double(result)


# float sub
class FSUB(NoOperandsInstruction):
    def execute(self, frame):
        stack = frame.operand_stack
        v2 = stack.pop_float()
        v1 = stack.pop_float()
        result = v1 - v2
        stack.push_float(result)


# int sub
class ISUB(NoOperandsInstruction):
    def execute(self, frame):
        _sub(frame)


# long sub
class LSUB(NoOperandsInstruction):
    def execute(self, frame):
        _sub(frame)
