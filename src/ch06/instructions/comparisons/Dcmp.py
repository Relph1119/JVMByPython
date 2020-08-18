#!/usr/bin/env python
# encoding: utf-8
"""
@author: HuRuiFeng
@file: Dcmp.py
@time: 2019/9/15 20:50
@desc: 比较double变量指令，当两个double变量中至少有一个是NaN时，用dcmpg指令比较的结果是1，用dcmpl指令比较的结果是-1
"""
from ch06.instructions.base.Instruction import NoOperandsInstruction


def _dcmp(frame, gFlag):
    stack = frame.operand_stack
    v2 = stack.pop_numeric()
    v1 = stack.pop_numeric()
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


class DCMPG(NoOperandsInstruction):
    def execute(self, frame):
        _dcmp(frame, True)


class DCMPL(NoOperandsInstruction):
    def execute(self, frame):
        _dcmp(frame, False)
