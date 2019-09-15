#!/usr/bin/env python
# encoding: utf-8
"""
@author: HuRuiFeng
@file: Add.py
@time: 2019/9/15 19:51
@desc: 加法(add)指令
"""
from instructions.base.Instruction import NoOperandsInstruction
from rtda import Frame


def _add(frame: Frame):
    stack = frame.operandStack
    v1 = stack.pop_numeric()
    v2 = stack.pop_numeric()
    result = v1 + v2
    stack.push_numeric(result)


# double add
class DADD(NoOperandsInstruction):
    def execute(self, frame):
        _add(frame)


# float add
class FADD(NoOperandsInstruction):
    def execute(self, frame):
        _add(frame)


# int add
class IADD(NoOperandsInstruction):
    def execute(self, frame):
        _add(frame)


# long add
class LADD(NoOperandsInstruction):
    def execute(self, frame):
        _add(frame)
