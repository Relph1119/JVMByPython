#!/usr/bin/env python
# encoding: utf-8
"""
@author: HuRuiFeng
@file: Tableswitch.py
@time: 2019/9/15 21:21
@desc: switch-case语句：如果case值可以编码成一个索引表，则实现成tableswith指令
"""
from instructions.base.BranchLogic import branch
from instructions.base.Instruction import NoOperandsInstruction


class TABLE_SWITCH(NoOperandsInstruction):
    def __init__(self):
        # 默认情况下执行跳转所需的字节码偏移量
        self.default_offset = 0
        # low和high记录case的取值范围
        self.low = 0
        self.high = 0
        # 一个索引表，存放high-low+1个int值，对应各种case情况下，执行跳转所需的字节码偏移量
        self.jump_offsets = []

    def fetch_operands(self, reader):
        # tableswitch指令操作码后面有0~3字节的padding，以保证default_offset在字节码中的地址是4的倍数
        reader.skip_padding()
        self.default_offset = reader.read_int32()
        self.low = reader.read_int32()
        self.high = reader.read_int32()
        jump_offsets_count = self.high - self.low + 1
        self.jump_offsets = reader.read_int32s(jump_offsets_count)

    def execute(self, frame):
        # 先从操作数栈中弹出一个int变量
        index = frame.operand_stack.pop_numeric()
        # 然后看它是否在low和high给定的范围内
        if self.low <= index <= self.high:
            # 如果在，则从jump_offset表中查出偏移量进行跳转
            offset = self.jump_offsets[index - self.low]
        else:
            # 否则按照default_offset跳转
            offset = self.default_offset
        branch(frame, offset)
