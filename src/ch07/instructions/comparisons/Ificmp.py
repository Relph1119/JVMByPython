#!/usr/bin/env python
# encoding: utf-8
"""
@author: HuRuiFeng
@file: Ificmp.py
@time: 2019/9/15 21:06
@desc: if_icmp<cond>指令把栈顶的两个int变量弹出，然后进行比较，满足条件则跳转
"""
from ch07.instructions.base.BranchLogic import branch
from ch07.instructions.base.Instruction import BranchInstruction
from ch07.rtda import Frame


def _icmpPop(frame: Frame):
    stack = frame.operand_stack
    val2 = stack.pop_numeric()
    val1 = stack.pop_numeric()
    return val1, val2


# if_icmpeq: x1 == x2
class IF_ICMPEQ(BranchInstruction):
    def execute(self, frame):
        val1, val2 = _icmpPop(frame)
        if val1 == val2:
            branch(frame, self.offset)


# if_icmpne: x1 != x2
class IF_ICMPNE(BranchInstruction):
    def execute(self, frame):
        val1, val2 = _icmpPop(frame)
        if val1 != val2:
            branch(frame, self.offset)


# if_icmplt: x1 < x2
class IF_ICMPLT(BranchInstruction):
    def execute(self, frame):
        val1, val2 = _icmpPop(frame)
        if val1 < val2:
            branch(frame, self.offset)


# if_icmple: x1 <= x2
class IF_ICMPLE(BranchInstruction):
    def execute(self, frame):
        val1, val2 = _icmpPop(frame)
        if val1 <= val2:
            branch(frame, self.offset)


# if_icmpgt: x1 > x2
class IF_ICMPGT(BranchInstruction):
    def execute(self, frame):
        val1, val2 = _icmpPop(frame)
        if val1 > val2:
            branch(frame, self.offset)


# if_icmpge: x1 >= x2
class IF_ICMPGE(BranchInstruction):
    def execute(self, frame):
        val1, val2 = _icmpPop(frame)
        if val1 >= val2:
            branch(frame, self.offset)
