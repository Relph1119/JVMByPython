#!/usr/bin/env python
# encoding: utf-8
"""
@author: HuRuiFeng
@file: Dup.py
@time: 2019/9/15 19:30
@desc: dup系列指令
"""

import copy

from instructions.base.Instruction import NoOperandsInstruction


class DUP(NoOperandsInstruction):
    """
    复制栈顶的单个变量
    bottom -> top
    [...][c][b][a]
                 \_
                   |
                   V
    [...][c][b][a][a]
    """

    def execute(self, frame):
        stack = frame.operandStack
        slot = stack.pop_slot()
        stack.push_slot(slot)
        # 采用deepcopy对象深拷贝，复制slot
        stack.push_slot(copy.deepcopy(slot))


class DUP_X1(NoOperandsInstruction):
    """
    bottom -> top
    [...][c][b][a]
              __/
             |
             V
    [...][c][a][b][a]
    """

    def execute(self, frame):
        stack = frame.operandStack
        slot1 = stack.pop_slot()
        slot2 = stack.pop_slot()
        stack.push_slot(copy.deepcopy(slot1))
        stack.push_slot(slot2)
        stack.push_slot(slot1)


class DUP_X2(NoOperandsInstruction):
    """
    bottom -> top
    [...][c][b][a]
           _____/
          |
          V
    [...][a][c][b][a]
    """

    def execute(self, frame):
        stack = frame.operandStack
        slot1 = stack.pop_slot()
        slot2 = stack.pop_slot()
        slot3 = stack.pop_slot()
        stack.push_slot(copy.deepcopy(slot1))
        stack.push_slot(slot3)
        stack.push_slot(slot2)
        stack.push_slot(slot1)


class DUP2(NoOperandsInstruction):
    """
    bottom -> top
    [...][c][b][a]____
              \____   |
                   |  |
                   V  V
    [...][c][b][a][b][a]
    """

    def execute(self, frame):
        stack = frame.operandStack()
        slot1 = stack.pop_slot()
        slot2 = stack.pop_slot()
        stack.push_slot(slot2)
        stack.push_slot(slot1)
        stack.push_slot(copy.deepcopy(slot2))
        stack.push_slot(copy.deepcopy(slot1))


class DUP2_X1(NoOperandsInstruction):
    """
    bottom -> top
    [...][c][b][a]
           _/ __/
          |  |
          V  V
    [...][b][a][c][b][a]
    """

    def execute(self, frame):
        stack = frame.operandStack()
        slot1 = stack.pop_slot()
        slot2 = stack.pop_slot()
        slot3 = stack.pop_slot()
        stack.push_slot(copy.deepcopy(slot2))
        stack.push_slot(copy.deepcopy(slot1))
        stack.push_slot(slot3)
        stack.push_slot(slot2)
        stack.push_slot(slot1)


class DUP2_X2(NoOperandsInstruction):
    """
    bottom -> top
    [...][d][c][b][a]
           ____/ __/
          |   __/
          V  V
    [...][b][a][d][c][b][a]
    """

    def execute(self, frame):
        stack = frame.operandStack()
        slot1 = stack.pop_slot()
        slot2 = stack.pop_slot()
        slot3 = stack.pop_slot()
        slot4 = stack.pop_slot()
        stack.push_slot(copy.deepcopy(slot2))
        stack.push_slot(copy.deepcopy(slot1))
        stack.push_slot(slot4)
        stack.push_slot(slot3)
        stack.push_slot(slot2)
        stack.push_slot(slot1)
