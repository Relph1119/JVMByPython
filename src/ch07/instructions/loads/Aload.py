#!/usr/bin/env python
# encoding: utf-8
"""
@author: HuRuiFeng
@file: Aload.py
@time: 2019/9/15 19:16
@desc: 引用类型变量加载指令
"""
from ch07.instructions.base.Instruction import Index8Instruction, NoOperandsInstruction
from ch07.rtda import Frame


def _aload(frame: Frame, index):
    ref = frame.local_vars.get_ref(index)
    frame.operand_stack.push_ref(ref)


class ALOAD(Index8Instruction):
    def execute(self, frame):
        _aload(frame, self.index)


class ALOAD_0(NoOperandsInstruction):
    def execute(self, frame):
        _aload(frame, 0)


class ALOAD_1(NoOperandsInstruction):
    def execute(self, frame):
        _aload(frame, 1)


class ALOAD_2(NoOperandsInstruction):
    def execute(self, frame):
        _aload(frame, 2)


class ALOAD_3(NoOperandsInstruction):
    def execute(self, frame):
        _aload(frame, 3)
