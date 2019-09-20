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
    def __init__(self, clazz: Class):
        # 存放对象的class
        self._class = clazz
        # 存放实例变量
        self.fields = Slots(clazz.instance_slot_count)

    def get_class(self):
        return self._class

    def is_instance_of(self, clazz: Class) -> bool:
        return clazz.is_assignable_from(self._class)
