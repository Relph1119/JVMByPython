#!/usr/bin/env python
# encoding: utf-8
"""
@author: HuRuiFeng
@file: Gotow.py
@time: 2019/9/15 21:57
@desc: goto_w指令和goto指令的唯一区别就是索引从2字节变成了4字节
"""

import ctypes

from ch06.instructions.base.BranchLogic import branch
from ch06.instructions.base.Instruction import NoOperandsInstruction


class GOTO_W(NoOperandsInstruction):
    def __init__(self):
        self.offset = 0

    def fetch_operands(self, reader):
        self.offset = ctypes.c_int(reader.read_int32()).value

    def execute(self, frame):
        branch(frame, self.offset)
