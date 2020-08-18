#!/usr/bin/env python
# encoding: utf-8
"""
@author: HuRuiFeng
@file: And.py
@time: 2019/9/15 19:53
@desc: 按位与(and)指令
"""
from ch08.instructions.base.Instruction import NoOperandsInstruction


def _and(frame):
    stack = frame.operand_stack
    v2 = stack.pop_numeric()
    v1 = stack.pop_numeric()
    result = v1 & v2
    stack.push_numeric(result)


# int and
class IAND(NoOperandsInstruction):
    def execute(self, frame):
        _and(frame)


# long and
class LAND(NoOperandsInstruction):
    def execute(self, frame):
        _and(frame)
