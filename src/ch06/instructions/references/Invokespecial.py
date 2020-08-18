#!/usr/bin/env python
# encoding: utf-8
"""
@author: HuRuiFeng
@file: Invokespecial.py
@time: 2019/9/16 20:55
@desc: invokespecial指令用于调用构造函数初始化对象
"""

from ch06.instructions.base.Instruction import Index16Instruction
from ch06.rtda.Frame import Frame


class INVOKE_SPECIAL(Index16Instruction):
    def execute(self, frame: Frame):
        frame.operand_stack.pop_ref()
