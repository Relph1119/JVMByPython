#!/usr/bin/env python
# encoding: utf-8
"""
@author: HuRuiFeng
@file: Object.py
@time: 2019/9/15 16:04
@desc: 表示对象
"""
from rtda.Slot import Slots
from rtda.heap.Class import Class


class Object:
    def __init__(self, clazz: Class, data=None):
        # 存放对象的class
        self._class = clazz
        # 存放实例变量
        if data is None:
            self.data = []
        else:
            self.data = data

    @staticmethod
    def new_object(clazz: Class):
        return Object(clazz, Slots(clazz.instance_slot_count))

    def get_class(self):
        return self._class

    def is_instance_of(self, clazz: Class) -> bool:
        return clazz.is_assignable_from(self._class)

    def fields(self):
        return self.data

    def bytes(self):
        return self.data

    def shorts(self):
        return self.data

    def ints(self):
        return self.data

    def longs(self):
        return self.data

    def chars(self):
        return self.data

    def floats(self):
        return self.data

    def doubles(self):
        return self.data

    # 引用类型数组
    def refs(self):
        return self.data

    # 数组长度
    # 上述方法主要是供<t>aload、<t>astore和arraylength指令使用；
    # <t>aload和<t>astore系列指令各有8条，针对每种类型都提供一个方法，返回相应的数组数据（由于python的数组中可以存放各种类型，故不区分数组类型）
    # arraylength指令只有一条，只需要一个方法。
    def array_length(self):
        return len(self.data)

    def set_ref_var(self, name, descriptor, ref):
        field = self._class.get_field(name, descriptor, False)
        slots = self.data
        slots.set_ref(field.slotId, ref)

    def get_ref_var(self, name, descriptor):
        field = self._class.get_field(name, descriptor, False)
        slots = self.data
        return slots.get_ref(field.slotId)
