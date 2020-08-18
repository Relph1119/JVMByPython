#!/usr/bin/env python
# encoding: utf-8
"""
@author: HuRuiFeng
@file: Nop.py
@time: 2019/9/15 18:33
@desc: nop指令，它什么也不做
"""
from ch05.instructions.base.Instruction import NoOperandsInstruction


class NOP(NoOperandsInstruction):
    def execute(self, frame):
        # 什么也不用做
        pass
