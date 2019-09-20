#!/usr/bin/env python
# encoding: utf-8
"""
@author: HuRuiFeng
@file: Multianewarray.py
@time: 2019/9/17 22:00
@desc: multianewarray指令用于创建多维数组。
第一个操作数是一个uint16索引，通过这个索引可以从运行时常量池中找到一个类符号引用，解析这个引用就可以得到多维数组类。
第二个操作数是一个uint8整数，表示数组维度。
还需要从操作数栈中弹出n个整数，分别白哦是每一个维度的数组长度。
"""

import copy
import ctypes

from instructions.base.Instruction import Instruction
from rtda.Frame import Frame


# 从操作数栈中弹出n个int值，并确保它们都大于等于0，如果其中任何一个小于0，则抛出NegativeArraySizeException异常。
def pop_and_check_counts(stack, dimensions):
    counts = [0 for i in range(dimensions)]
    for i in range(dimensions - 1, -1, -1):
        counts[i] = stack.pop_numeric()
        if counts[i] < 0:
            raise RuntimeError("java.lang.NegativeArraySizeException")

    return counts


# 创建多维数组
def new_multi_dimensional_array(counts, arr_class):
    count = ctypes.c_uint(counts[0]).value
    arr = arr_class.new_array(count)

    if len(counts) > 1:
        refs = arr.refs()
        for i in range(len(refs)):
            refs[i] = new_multi_dimensional_array(copy.deepcopy(counts[1:]), arr_class.component_class())

    return arr


class MULTI_ANEW_ARRAY(Instruction):
    def __init__(self):
        self.index = 0
        self.dimensions = 0

    def fetch_operands(self, reader):
        self.index = reader.read_uint16()
        self.dimensions = reader.read_uint8()

    def execute(self, frame: Frame):
        cp = frame.method.get_class().constant_pool
        class_ref = cp.get_constant(ctypes.c_uint(self.index).value)
        # 解析出来的直接就是数组类
        arr_class = class_ref.resolved_class()

        stack = frame.operand_stack
        counts = pop_and_check_counts(stack, ctypes.c_int(self.dimensions).value)
        arr = new_multi_dimensional_array(counts, arr_class)
        stack.push_ref(arr)
