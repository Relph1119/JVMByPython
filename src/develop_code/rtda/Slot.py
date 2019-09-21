#!/usr/bin/env python
# encoding: utf-8
"""
@author: HuRuiFeng
@file: Slot.py
@time: 2019/9/15 16:22
@desc: Slot类，可以容纳一个int值和一个引用值
"""


class Slot:
    def __init__(self):
        # 存放整数
        self.num = 0
        # 存放引用
        self.ref = None

    def __str__(self):
        return "num:{0} ref:{1}".format(self.num, self.ref)


# Slot数组类
class Slots(list):
    def __init__(self, slot_count=1):
        if slot_count > 0:
            super().__init__([Slot() for _ in range(slot_count)])
        else:
            super().__init__()

    def set_numeric(self, index, val):
        self[index].num = val

    def get_numeric(self, index):
        return self[index].num

    def set_ref(self, index, ref):
        self[index].ref = ref

    def get_ref(self, index):
        return self[index].ref


# slot拷贝，不能使用深拷贝copy.deepcopy函数，由于ref复制的是引用，需要将num和ref都进行拷贝。
def copy_slot(slot):
    new_slot = Slot()
    new_slot.num = slot.num
    new_slot.ref = slot.ref
    return new_slot
