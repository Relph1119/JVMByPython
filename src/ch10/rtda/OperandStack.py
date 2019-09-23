#!/usr/bin/env python
# encoding: utf-8
"""
@author: HuRuiFeng
@file: OperandStack.py
@time: 2019/9/15 16:29
@desc: 操作数栈，用于python的列表能存储任何数据类型，所以将基本数据类型和引用类型都用一个Slot表示。
"""
import struct

from rtda.Slot import Slot


class OperandStack:
    def __init__(self, max_stack):
        self.slots = []
        self.size = 0
        if max_stack > 0:
            self.slots = [Slot() for _ in range(max_stack)]

    def push_numeric(self, val):
        self.slots[self.size].num = val
        self.size += 1

    def pop_numeric(self):
        self.size -= 1
        return self.slots[self.size].num

    def push_double(self, val):
        val = struct.unpack('>q', struct.pack('>d', val))[0]
        self.push_numeric(val)

    def pop_double(self):
        val = self.pop_numeric()
        return struct.unpack('>d', struct.pack('>q', val))[0]

    def push_float(self, val):
        val = struct.unpack('>l', struct.pack('>f', val))[0]
        self.push_numeric(val)

    def pop_float(self):
        val = self.pop_numeric()
        return struct.unpack('>f', struct.pack('>l', val))[0]

    def push_boolean(self, val):
        if val:
            self.push_numeric(1)
        else:
            self.push_numeric(0)

    def pop_boolean(self):
        return self.pop_numeric() == 1

    def push_ref(self, ref):
        if ref == 0:
            ref = None
        self.slots[self.size].ref = ref
        self.size += 1

    def pop_ref(self):
        self.size -= 1
        ref = self.slots[self.size].ref
        self.slots[self.size].ref = None
        return ref

    def push_slot(self, slot: Slot):
        self.slots[self.size] = slot
        self.size += 1

    def pop_slot(self):
        self.size -= 1
        return self.slots[self.size]

    # 返回距离操作数栈顶n个单元格的引用变量
    def get_ref_from_top(self, n):
        return self.slots[self.size - 1 - n].ref

    # 清空虚拟机栈
    def clear(self):
        self.size = 0
        for i, _ in enumerate(self.slots):
            self.slots[i].ref = None

    def __str__(self):
        return "size:{0} slots:{1}".format(self.size, [str(t) for t in self.slots])
