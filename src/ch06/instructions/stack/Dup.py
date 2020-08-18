#!/usr/bin/env python
# encoding: utf-8
"""
@author: HuRuiFeng
@file: Dup.py
@time: 2019/9/15 19:30
@desc: dup系列指令
"""

from ch06.instructions.base.Instruction import NoOperandsInstruction
from ch06.rtda.Slot import Slot


# slot拷贝，不能使用深拷贝copy.deepcopy函数，由于ref复制的是引用，需要将num和ref都进行拷贝。
def copy_slot(slot):
    new_slot = Slot()
    new_slot.num = slot.num
    new_slot.ref = slot.ref
    return new_slot


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
        stack = frame.operand_stack
        slot = stack.pop_slot()
        stack.push_slot(slot)
        # 采用自定义的对象深拷贝，复制slot
        stack.push_slot(copy_slot(slot))


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
        stack = frame.operand_stack
        slot1 = stack.pop_slot()
        slot2 = stack.pop_slot()
        stack.push_slot(copy_slot(slot1))
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
        stack = frame.operand_stack
        slot1 = stack.pop_slot()
        slot2 = stack.pop_slot()
        slot3 = stack.pop_slot()
        stack.push_slot(copy_slot(slot1))
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
        stack = frame.operand_stack
        slot1 = stack.pop_slot()
        slot2 = stack.pop_slot()
        stack.push_slot(slot2)
        stack.push_slot(slot1)
        stack.push_slot(copy_slot(slot2))
        stack.push_slot(copy_slot(slot1))


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
        stack = frame.operand_stack
        slot1 = stack.pop_slot()
        slot2 = stack.pop_slot()
        slot3 = stack.pop_slot()
        stack.push_slot(copy_slot(slot2))
        stack.push_slot(copy_slot(slot1))
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
        stack = frame.operand_stack
        slot1 = stack.pop_slot()
        slot2 = stack.pop_slot()
        slot3 = stack.pop_slot()
        slot4 = stack.pop_slot()
        stack.push_slot(copy_slot(slot2))
        stack.push_slot(copy_slot(slot1))
        stack.push_slot(slot4)
        stack.push_slot(slot3)
        stack.push_slot(slot2)
        stack.push_slot(slot1)
