#!/usr/bin/env python
# encoding: utf-8
"""
@author: HuRuiFeng
@file: OperandStack.py
@time: 2019/9/15 16:29
@desc: 操作数栈，用于python的列表能存储任何数据类型，所以将基本数据类型和引用类型都用一个Slot表示。
"""

from ch04.rtda.Slot import Slot


class OperandStack:
    def __init__(self, max_stack):
        self.slots = []
        if max_stack > 0:
            self.slots = [Slot() for _ in range(max_stack)]
        self.size = 0

    def push_numeric(self, val):
        self.slots[self.size].num = val
        self.size += 1

    def pop_numeric(self):
        self.size -= 1
        return self.slots[self.size].num

    def push_ref(self, ref):
        self.slots[self.size].ref = ref
        self.size += 1

    def pop_ref(self):
        self.size -= 1
        ref = self.slots[self.size].ref
        self.slots[self.size].ref = None
        return ref
