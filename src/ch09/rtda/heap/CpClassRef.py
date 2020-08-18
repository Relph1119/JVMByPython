#!/usr/bin/env python
# encoding: utf-8
"""
@author: HuRuiFeng
@file: CpClassRef.py
@time: 2019/9/16 17:57
@desc: 类符号引用
"""
from ch09.classfile.ConstantClassInfo import ConstantClassInfo
from ch09.rtda.heap.CpSymRef import SymRef


class ClassRef(SymRef):

    def __init__(self, constant_pool, class_info: ConstantClassInfo):
        super().__init__()
        self.cp = constant_pool
        self.class_name = class_info.name
