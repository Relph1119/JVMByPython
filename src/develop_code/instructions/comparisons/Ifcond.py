#!/usr/bin/env python
# encoding: utf-8
"""
@author: HuRuiFeng
@file: Ifcond.py
@time: 2019/9/15 20:58
@desc: if<cond>指令把操作数栈顶的int变量弹出，然后跟0进行比较，满足条件则跳转
"""
from instructions.base.BranchLogic import branch
from instructions.base.Instruction import BranchInstruction


# ifeq: x == 0
class IFEQ(BranchInstruction):
    def execute(self, frame):
        val = frame.operandStack.pop_numeric()
        if val == 0:
            branch(frame, self.offset)


# ifne: x != 0
class IFNE(BranchInstruction):
    def execute(self, frame):
        val = frame.operandStack.pop_numeric()
        if val != 0:
            branch(frame, self.offset)


# iflt: x < 0
class IFLT(BranchInstruction):
    def execute(self, frame):
        val = frame.operandStack.pop_numeric()
        if val < 0:
            branch(frame, self.offset)


# ifle: x <= 0
class IFLE(BranchInstruction):
    def execute(self, frame):
        val = frame.operandStack.pop_numeric()
        if val <= 0:
            branch(frame, self.offset)


# ifgt: x > 0
class IFGT(BranchInstruction):
    def execute(self, frame):
        val = frame.operandStack.pop_numeric()
        if val > 0:
            branch(frame, self.offset)


# ifge: x >= 0
class IFGE(BranchInstruction):
    def execute(self, frame):
        val = frame.operandStack.pop_numeric()
        if val >= 0:
            branch(frame, self.offset)
