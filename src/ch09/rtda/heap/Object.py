#!/usr/bin/env python
# encoding: utf-8
"""
@author: HuRuiFeng
@file: Object.py
@time: 2019/9/15 16:04
@desc: 表示对象
"""

from ch09.rtda.Slot import Slots, copy_slot
from ch09.rtda.heap.Class import Class


class Object:
    def __init__(self, clazz: Class, data=None, extra=None):
        # 存放对象的class
        self._class = clazz
        # 存放实例变量
        if data is None:
            self.data = []
        else:
            self.data = data
        # 用来记录Object结构体实例的额外信息
        if extra is None:
            self.extra = []
        else:
            self.extra = extra

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
        if type(self.data).__getitem__ is not None:
            return len(self.data)
        else:
            raise RuntimeError("Not array!")

    # 直接给对象的引用类型实例变量赋值
    def set_ref_var(self, name, descriptor, ref):
        field = self._class.get_field(name, descriptor, False)
        slots = self.data
        slots.set_ref(field.slot_id, ref)

    def get_ref_var(self, name, descriptor):
        field = self._class.get_field(name, descriptor, False)
        slots = self.data
        return slots.get_ref(field.slot_id)

    # 数组拷贝
    @staticmethod
    def array_copy(src, dest, src_pos, dest_pos, length):
        if type(src.data).__getitem__ is not None:
            dest.data[dest_pos: dest_pos + length] = list(src.data[src_pos: src_pos + length])
        else:
            raise RuntimeError("Not array!")

    def clone(self):
        return Object(self._class, self.clone_data())

    def clone_data(self):
        if not isinstance(self.data, Slots):
            new_data = list(self.data)
            return new_data
        else:
            new_data = Slots(len(self.data))
            for i, slot in enumerate(self.data):
                new_data[i] = copy_slot(slot)
            return new_data
