#!/usr/bin/env python
# encoding: utf-8
"""
@author: HuRuiFeng
@file: Sh.py
@time: 2019/9/15 20:04
@desc: 位移指令
"""

import ctypes

from instructions.base.Instruction import NoOperandsInstruction


# int左位移
class ISHL(NoOperandsInstruction):
    def execute(self, frame):
        stack = frame.operand_stack
        v2 = stack.pop_numeric()
        v1 = stack.pop_numeric()
        s = v2 & 0x1f
        result = v1 << s
        stack.push_numeric(result)


# int算术右位移
class ISHR(NoOperandsInstruction):
    def execute(self, frame):
        stack = frame.operand_stack
        v2 = stack.pop_numeric()
        v1 = stack.pop_numeric()
        s = v2 & 0x1f
        result = v1 >> s
        stack.push_numeric(result)


# int逻辑右位移
class IUSHR(NoOperandsInstruction):
    def execute(self, frame):
        stack = frame.operand_stack
        v2 = stack.pop_numeric()
        v1 = stack.pop_numeric()
        s = v2 & 0x1f
        result = ctypes.c_int32(ctypes.c_uint32(v1).value >> s).value
        stack.push_numeric(result)


# long左位移
class LSHL(NoOperandsInstruction):
    def execute(self, frame):
        stack = frame.operand_stack
        v2 = stack.pop_numeric()
        v1 = stack.pop_numeric()
        s = v2 & 0x3f
        result = v1 << s
        stack.push_numeric(result)


# long算术右位移
class LSHR(NoOperandsInstruction):
    def execute(self, frame):
        stack = frame.operand_stack
        v2 = stack.pop_numeric()
        v1 = stack.pop_numeric()
        s = v2 & 0x3f
        result = v1 >> s
        stack.push_numeric(result)


# long逻辑右位移
class LUSHR(NoOperandsInstruction):
    def execute(self, frame):
        stack = frame.operand_stack
        v2 = stack.pop_numeric()
        v1 = stack.pop_numeric()
        s = v2 & 0x3f
        result = ctypes.c_int32(ctypes.c_uint32(v1).value >> s).value
        stack.push_numeric(result)
