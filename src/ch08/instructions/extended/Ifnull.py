#!/usr/bin/env python
# encoding: utf-8
"""
@author: HuRuiFeng
@file: Ifnull.py
@time: 2019/9/15 21:54
@desc: 根据引用是否为null进行跳转
"""
from ch08.instructions.base.BranchLogic import branch
from ch08.instructions.base.Instruction import BranchInstruction


class IFNULL(BranchInstruction):
    def execute(self, frame):
        ref = frame.operand_stack.pop_ref()
        if ref is None:
            branch(frame, self.offset)


class IFNONNULL(BranchInstruction):
    def execute(self, frame):
        ref = frame.operand_stack.pop_ref()
        if ref is not None:
            branch(frame, self.offset)
