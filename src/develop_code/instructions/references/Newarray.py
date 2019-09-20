#!/usr/bin/env python
# encoding: utf-8
"""
@author: HuRuiFeng
@file: Newarray.py
@time: 2019/9/17 21:07
@desc: newarray指令用来创建基本类型数组，包括boolean[]、byte[]、char[]、short[]、int[]、long[]、float[]和double[] 8种。
需要两个操作数：第一个操作数是一个uint8整数，在字节码中紧跟在指令操作码后面，表示要创建哪种类型的数组。
第二个操作数是count，从操作数栈中弹出，表示数组长度。
"""
from instructions.base.Instruction import Instruction
from rtda.Frame import Frame


class NEW_ARRAY(Instruction):
    AT_BOOLEAN = 4
    AT_CHAR = 5
    AT_FLOAT = 6
    AT_DOUBLE = 7
    AT_BYTE = 8
    AT_SHORT = 9
    AT_INT = 10
    AT_LONG = 11

    def __init__(self):
        self.atype = 0

    def fetch_operands(self, reader):
        self.atype = reader.read_uint8()

    def execute(self, frame: Frame):
        import ctypes

        stack = frame.operand_stack
        count = stack.pop_numeric()
        # 如果count小于0，则抛出NegativeArraySizeException异常
        if count < 0:
            raise RuntimeError("java.lang.NegativeArraySizeException")

        # 根据atype值使用当前类的类加载器加载数组类，然后创建数组对象并推入操作数栈。
        class_loader = frame.method.get_class().loader
        arr_class = self.get_primitive_array_class(class_loader, self.atype)
        arr = arr_class.new_array(ctypes.c_uint(count).value)
        stack.push_ref(arr)

    @staticmethod
    def get_primitive_array_class(loader, atype):
        if atype == NEW_ARRAY.AT_BOOLEAN:
            return loader.load_class("[Z")
        elif atype == NEW_ARRAY.AT_BYTE:
            return loader.load_class("[B")
        elif atype == NEW_ARRAY.AT_CHAR:
            return loader.load_class("[C")
        elif atype == NEW_ARRAY.AT_SHORT:
            return loader.load_class("[S")
        elif atype == NEW_ARRAY.AT_INT:
            return loader.load_class("[I")
        elif atype == NEW_ARRAY.AT_LONG:
            return loader.load_class("[J")
        elif atype == NEW_ARRAY.AT_FLOAT:
            return loader.load_class("[F")
        elif atype == NEW_ARRAY.AT_DOUBLE:
            return loader.load_class("[D")
        else:
            raise RuntimeError("Invalid atype!")
