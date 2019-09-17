#!/usr/bin/env python
# encoding: utf-8
"""
@author: HuRuiFeng
@file: Ipush.py
@time: 2019/9/15 23:20
@desc:
"""

from instructions.base.Instruction import Instruction


# 从操作数中获取一个byte类型整数，扩展成int型，然后推入栈顶
class BIPUSH(Instruction):
    def __init__(self):
        self.val = 0

    def fetch_operands(self, reader):
        self.val = reader.read_int8()

    def execute(self, frame):
        i = self.val
        frame.operand_stack.push_numeric(i)


# 从操作数中获取一个short类型整数，扩展成int型，然后推入栈顶
class SIPUSH(Instruction):
    def __init__(self):
        self.val = 0

    def fetch_operands(self, reader):
        self.val = reader.read_int16()

    def execute(self, frame):
        i = self.val
        frame.operand_stack.push_numeric(i)
