#!/usr/bin/env python
# encoding: utf-8
"""
@author: HuRuiFeng
@file: Goto.py
@time: 2019/9/15 21:20
@desc: goto指令，进行无条件跳转
"""
from ch05.instructions.base.BranchLogic import branch
from ch05.instructions.base.Instruction import BranchInstruction


class GOTO(BranchInstruction):
    def execute(self, frame):
        branch(frame, self.offset)
