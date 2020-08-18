#!/usr/bin/env python
# encoding: utf-8
"""
@author: HuRuiFeng
@file: Swap.py
@time: 2019/9/15 19:49
@desc: swap指令
"""
from ch07.instructions.base.Instruction import NoOperandsInstruction


class SWAP(NoOperandsInstruction):
    """
    bottom -> top
    [...][c][b][a]
              \/
              /\
             V  V
    [...][c][a][b]
    """

    def execute(self, frame):
        stack = frame.operand_stack
        slot1 = stack.pop_slot()
        slot2 = stack.pop_slot()
        stack.push_slot(slot1)
        stack.push_slot(slot2)
