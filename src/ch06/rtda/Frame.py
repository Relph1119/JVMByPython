#!/usr/bin/env python
# encoding: utf-8
"""
@author: HuRuiFeng
@file: Frame.py
@time: 2019/9/15 16:19
@desc: 帧
"""
from ch06.rtda.LocalVars import LocalVars
from ch06.rtda.OperandStack import OperandStack
from ch06.rtda.Thread import Thread
from ch06.rtda.heap.Method import Method


class Frame:
    def __init__(self, thread: Thread, method: Method):
        # 用来实现链表数据结构
        self.lower = None
        self.thread = thread
        self.method = method
        # 保存局部变量表指针
        self.local_vars = LocalVars(method.max_locals)
        # 保存操作数栈指针
        self.operand_stack = OperandStack(method.max_stack)
        self.next_pc = 0
