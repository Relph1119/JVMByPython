#!/usr/bin/env python
# encoding: utf-8
"""
@author: HuRuiFeng
@file: Ifacmp.py
@time: 2019/9/15 21:10
@desc: if_acmp<cond>指令把栈顶的两个引用弹出，根据引用是否相同进行跳转
"""
from ch06.instructions.base.BranchLogic import branch
from ch06.instructions.base.Instruction import BranchInstruction


def _acmpPop(frame):
    stack = frame.operand_stack
    val2 = stack.pop_ref()
    val1 = stack.pop_ref()
    return val1, val2


class IF_ACMPEQ(BranchInstruction):
    def execute(self, frame):
        val1, val2 = _acmpPop(frame)
        if val1 is val2:
            branch(frame, self.offset)


class IF_ACMPNE(BranchInstruction):
    def execute(self, frame):
        val1, val2 = _acmpPop(frame)
        if val1 is not val2:
            branch(frame, self.offset)
