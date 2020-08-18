#!/usr/bin/env python
# encoding: utf-8
"""
@author: HuRuiFeng
@file: Const.py
@time: 2019/9/15 18:34
@desc: Const系列指令
"""
from ch06.instructions.base.Instruction import NoOperandsInstruction


# aconst_null指令把null引用推入操作数栈顶
class ACONST_NULL(NoOperandsInstruction):
    def execute(self, frame):
        frame.operand_stack.push_ref(None)


# 把double类型0推入操作数栈顶
class DCONST_0(NoOperandsInstruction):
    def execute(self, frame):
        frame.operand_stack.push_numeric(0.0)


# 把double类型1推入操作数栈顶
class DCONST_1(NoOperandsInstruction):
    def execute(self, frame):
        frame.operand_stack.push_numeric(1.0)


# 把float类型0推入操作数栈顶
class FCONST_0(NoOperandsInstruction):
    def execute(self, frame):
        frame.operand_stack.push_numeric(0.0)


# 把float类型1推入操作数栈顶
class FCONST_1(NoOperandsInstruction):
    def execute(self, frame):
        frame.operand_stack.push_numeric(1.0)


# 把float类型2推入操作数栈顶
class FCONST_2(NoOperandsInstruction):
    def execute(self, frame):
        frame.operand_stack.push_numeric(2.0)


# 把int类型-1推入操作数栈顶
class ICONST_M1(NoOperandsInstruction):
    def execute(self, frame):
        frame.operand_stack.push_numeric(-1)


# 把int类型0推入操作数栈顶
class ICONST_0(NoOperandsInstruction):
    def execute(self, frame):
        frame.operand_stack.push_numeric(0)


# 把int类型1推入操作数栈顶
class ICONST_1(NoOperandsInstruction):
    def execute(self, frame):
        frame.operand_stack.push_numeric(1)


# 把int类型2推入操作数栈顶
class ICONST_2(NoOperandsInstruction):
    def execute(self, frame):
        frame.operand_stack.push_numeric(2)


# 把int类型3推入操作数栈顶
class ICONST_3(NoOperandsInstruction):
    def execute(self, frame):
        frame.operand_stack.push_numeric(3)


# 把int类型4推入操作数栈顶
class ICONST_4(NoOperandsInstruction):
    def execute(self, frame):
        frame.operand_stack.push_numeric(4)


# 把int类型5推入操作数栈顶
class ICONST_5(NoOperandsInstruction):
    def execute(self, frame):
        frame.operand_stack.push_numeric(5)


# 把long类型0推入操作数栈顶
class LCONST_0(NoOperandsInstruction):
    def execute(self, frame):
        frame.operand_stack.push_numeric(0)


# 把long类型1推入操作数栈顶
class LCONST_1(NoOperandsInstruction):
    def execute(self, frame):
        frame.operand_stack.push_numeric(1)
