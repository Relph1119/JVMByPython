#!/usr/bin/env python
# encoding: utf-8
"""
@author: HuRuiFeng
@file: Iinc.py
@time: 2019/9/15 20:32
@desc: int变量增加常量值指令
"""

import ctypes

from ch05.instructions.base.Instruction import NoOperandsInstruction


class IINC(NoOperandsInstruction):
    def __init__(self):
        self.index = 0
        self.const = 0

    # 从字节码里读取操作数
    def fetch_operands(self, reader):
        self.index = ctypes.c_uint(reader.read_uint8()).value
        self.const = ctypes.c_int32(reader.read_int8()).value

    # 从局部变量表中读取变量，给它加上常量值，再把结果写回局部变量表
    def execute(self, frame):
        local_vars = frame.local_vars
        val = local_vars.get_numeric(self.index)
        val += self.const
        local_vars.set_numeric(self.index, val)
