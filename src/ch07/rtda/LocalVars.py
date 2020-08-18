#!/usr/bin/env python
# encoding: utf-8
"""
@author: HuRuiFeng
@file: LocalVars.py
@time: 2019/9/15 16:22
@desc: 局部变量表，用于python的列表能存储任何数据类型，所以将基本数据类型和引用类型都用一个Slot表示。
"""

from ch07.rtda.Slot import Slot


class LocalVars(list):
    def __init__(self, max_locals):
        super().__init__([Slot() for _ in range(max_locals)])

    def set_numeric(self, index, val):
        self[index].num = val

    def get_numeric(self, index):
        return self[index].num

    def set_ref(self, index, ref):
        self[index].ref = ref

    def get_ref(self, index):
        return self[index].ref

    def set_slot(self, index, slot: Slot):
        self[index] = slot

    def __str__(self):
        return "slots:{0}".format([str(t) for t in self])
