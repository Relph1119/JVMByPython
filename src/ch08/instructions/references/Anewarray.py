#!/usr/bin/env python
# encoding: utf-8
"""
@author: HuRuiFeng
@file: Anewarray.py
@time: 2019/9/17 21:18
@desc: anewarray指令用来创建引用类型数组，需要两个操作数。
第一个操作数是uint16索引，来自字节码。通过这个索引可以从当前类的运行时常量池中找到一个类符号引用，解析这个符号引用就可以得到数组元素的类。
第二个操作数是数组长度，从操作数栈中弹出。
"""
from ch08.instructions.base.Instruction import Index16Instruction


class ANEW_ARRAY(Index16Instruction):
    def execute(self, frame):
        import ctypes

        cp = frame.method.get_class().constant_pool
        class_ref = cp.get_constant(self.index)
        component_class = class_ref.resolved_class()

        stack = frame.operand_stack
        count = stack.pop_numeric()
        if count < 0:
            raise RuntimeError("java.lang.NegativeArraySizeException")

        arr_class = component_class.array_class()
        arr = arr_class.new_array(ctypes.c_uint(count).value)
        stack.push_ref(arr)
