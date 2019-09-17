#!/usr/bin/env python
# encoding: utf-8
"""
@author: HuRuiFeng
@file: Or.py
@time: 2019/9/15 20:30
@desc: 按位或(or)指令
"""
from instructions.base.Instruction import NoOperandsInstruction
from rtda import Frame


def _or(frame: Frame):
    stack = frame.operand_stack
    v2 = stack.pop_numeric()
    v1 = stack.pop_numeric()
    result = v1 | v2
    stack.push_numeric(result)


# int or
class IOR(NoOperandsInstruction):
    def execute(self, frame):
        _or(frame)


# long or
class LOR(NoOperandsInstruction):
    def execute(self, frame):
        _or(frame)
