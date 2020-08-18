#!/usr/bin/env python
# encoding: utf-8
"""
@author: HuRuiFeng
@file: Dcmp.py
@time: 2019/9/15 20:54
@desc: 比较float变量指令，当两个float变量中至少有一个是NaN时，用fcmpg指令比较的结果是1，用fcmpl指令比较的结果是-1
"""
from ch09.instructions.base.Instruction import NoOperandsInstruction


def _fcmp(frame, gFlag):
    stack = frame.operand_stack
    v2 = stack.pop_float()
    v1 = stack.pop_float()
    if v1 > v2:
        stack.push_numeric(1)
    elif v1 == v2:
        stack.push_numeric(0)
    elif v1 < v2:
        stack.push_numeric(-1)
    elif gFlag:
        stack.push_numeric(1)
    else:
        stack.push_numeric(-1)


class FCMPG(NoOperandsInstruction):
    def execute(self, frame):
        _fcmp(frame, True)


class FCMPL(NoOperandsInstruction):
    def execute(self, frame):
        _fcmp(frame, False)
