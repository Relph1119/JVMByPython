#!/usr/bin/env python
# encoding: utf-8
"""
@author: HuRuiFeng
@file: Lookupswitch.py
@time: 2019/9/15 21:40
@desc: switch-case语句：如果case值不可以编码成一个索引表，则实现成lookupswitch指令
"""

import ctypes

from instructions.base.BranchLogic import branch
from instructions.base.Instruction import NoOperandsInstruction


class LOOKUP_SWITCH(NoOperandsInstruction):
    def __init__(self):
        self.default_offset = 0
        self.n_pairs = 0
        # 有点像Map，它的key是case值，value是跳转偏移量
        self.match_offsets = []

    def fetch_operands(self, reader):
        reader.skip_padding()
        self.default_offset = reader.read_int32()
        self.n_pairs = reader.read_int32()
        self.match_offsets = reader.read_int32s(self.n_pairs * 2)

    def execute(self, frame):
        # 先从操作数栈中弹出一个int变量
        key = frame.operandStack.pop_numeric()
        # 然后用它查找match_offsets，看能否找到匹配的key
        for i in range(0, self.n_pairs * 2, 2):
            if self.match_offsets[i] == key:
                # 如果能，则按照value给出的偏移量跳转
                offset = self.match_offsets[i + 1]
                branch(frame, ctypes.c_int(offset).value)
                return
        # 否则按照default_offset跳转
        branch(frame, ctypes.c_int(self.default_offset).value)
