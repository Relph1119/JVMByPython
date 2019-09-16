#!/usr/bin/env python
# encoding: utf-8
"""
@author: HuRuiFeng
@file: I2x.py
@time: 2019/9/15 20:41
@desc: int类型转换指令
"""

import ctypes

from instructions.base.Instruction import NoOperandsInstruction


# Convert int to byte
class I2B(NoOperandsInstruction):
    def execute(self, frame):
        stack = frame.operand_stack
        i = stack.pop_numeric()
        b = ctypes.c_int32(ctypes.c_int8(i).value).value
        stack.push_numeric(b)


# Convert int to char
class I2C(NoOperandsInstruction):
    def execute(self, frame):
        stack = frame.operand_stack
        i = stack.pop_numeric()
        c = ctypes.c_int32(ctypes.c_uint16(i).value).value
        stack.push_numeric(c)


# Convert int to short
class I2S(NoOperandsInstruction):
    def execute(self, frame):
        stack = frame.operand_stack
        i = stack.pop_numeric()
        s = ctypes.c_int32(ctypes.c_int16(i).value).value
        stack.push_numeric(s)


# Convert int to double
class I2D(NoOperandsInstruction):
    def execute(self, frame):
        stack = frame.operand_stack
        i = stack.pop_numeric()
        d = ctypes.c_float(i).value
        stack.push_numeric(d)


# Convert int to float
class I2F(NoOperandsInstruction):
    def execute(self, frame):
        stack = frame.operand_stack
        i = stack.pop_numeric()
        f = ctypes.c_float(i).value
        stack.push_numeric(f)


# Convert int to long
class I2L(NoOperandsInstruction):
    def execute(self, frame):
        stack = frame.operand_stack
        i = stack.pop_numeric()
        l = ctypes.c_int64(i).value
        stack.push_numeric(l)
