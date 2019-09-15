#!/usr/bin/env python
# encoding: utf-8
"""
@author: HuRuiFeng
@file: Frame.py
@time: 2019/9/15 16:19
@desc: 帧
"""
from rtda import Thread
from rtda.LocalVars import LocalVars
from rtda.OperandStack import OperandStack


class Frame:
    def __init__(self, thread:Thread, max_locals, max_stack):
        # 用来实现链表数据结构
        self.lower = None
        self.thread = thread
        # 保存局部变量表指针
        self.localVars = LocalVars(max_locals)
        # 保存操作数栈指针
        self.operandStack = OperandStack(max_stack)
        self.next_pc = 0
