#!/usr/bin/env python
# encoding: utf-8
"""
@author: HuRuiFeng
@file: Frame.py
@time: 2019/9/15 16:19
@desc: 帧
"""
from ch04.rtda.LocalVars import LocalVars
from ch04.rtda.OperandStack import OperandStack


class Frame:
    def __init__(self, max_locals, max_stack):
        # 用来实现链表数据结构
        self.lower = None
        # 保存局部变量表指针
        self.local_vars = LocalVars(max_locals)
        # 保存操作数栈指针
        self.operand_stack = OperandStack(max_stack)
