#!/usr/bin/env python
# encoding: utf-8
"""
@author: HuRuiFeng
@file: Xaload.py
@time: 2019/9/17 21:35
@desc: <t>aload系列指令按索引获取数组元素值，然后推入操作数栈。
"""
from ch08.instructions.base.Instruction import NoOperandsInstruction
from ch08.rtda.Frame import Frame
from ch08.rtda.heap.Object import Object


def check_not_none(ref: Object):
    if ref is None:
        raise RuntimeError("java.lang.NullPointerException")


def check_index(arr_len, index):
    import ctypes

    # 如果数组索引小于0，或者大于等于数组长度，则抛出ArrayIndexOutOfBoundsException异常
    if index < 0 or index >= ctypes.c_int32(arr_len).value:
        raise RuntimeError("ArrayIndexOutOfBoundsException")


class AALOAD(NoOperandsInstruction):
    def execute(self, frame: Frame):
        stack = frame.operand_stack
        index = stack.pop_numeric()
        arr_ref = stack.pop_ref()

        # 检查第二个操作数：数组引用
        check_not_none(arr_ref)
        ref_array = arr_ref.refs()
        # 检查数组索引
        check_index(len(ref_array), index)
        stack.push_ref(ref_array[index])


class BALOAD(NoOperandsInstruction):
    def execute(self, frame: Frame):
        stack = frame.operand_stack
        index = stack.pop_numeric()
        arr_ref = stack.pop_ref()

        check_not_none(arr_ref)
        bytes_array = arr_ref.bytes()
        check_index(len(bytes_array), index)
        stack.push_numeric(bytes_array[index])


class CALOAD(NoOperandsInstruction):
    def execute(self, frame: Frame):
        stack = frame.operand_stack
        index = stack.pop_numeric()
        arr_ref = stack.pop_ref()

        check_not_none(arr_ref)
        char_array = arr_ref.chars()
        check_index(len(char_array), index)
        stack.push_numeric(char_array[index])


class DALOAD(NoOperandsInstruction):
    def execute(self, frame: Frame):
        stack = frame.operand_stack
        index = stack.pop_numeric()
        arr_ref = stack.pop_ref()

        check_not_none(arr_ref)
        double_array = arr_ref.doubles()
        check_index(len(double_array), index)
        stack.push_numeric(double_array[index])


class FALOAD(NoOperandsInstruction):
    def execute(self, frame: Frame):
        stack = frame.operand_stack
        index = stack.pop_numeric()
        arr_ref = stack.pop_ref()

        check_not_none(arr_ref)
        float_array = arr_ref.floats()
        check_index(len(float_array), index)
        stack.push_numeric(float_array[index])


class IALOAD(NoOperandsInstruction):
    def execute(self, frame: Frame):
        stack = frame.operand_stack
        index = stack.pop_numeric()
        arr_ref = stack.pop_ref()

        check_not_none(arr_ref)
        int_array = arr_ref.ints()
        check_index(len(int_array), index)
        stack.push_numeric(int_array[index])


class LALOAD(NoOperandsInstruction):
    def execute(self, frame: Frame):
        stack = frame.operand_stack
        index = stack.pop_numeric()
        arr_ref = stack.pop_ref()

        check_not_none(arr_ref)
        long_array = arr_ref.longs()
        check_index(len(long_array), index)
        stack.push_numeric(long_array[index])


class SALOAD(NoOperandsInstruction):
    def execute(self, frame: Frame):
        stack = frame.operand_stack
        index = stack.pop_numeric()
        arr_ref = stack.pop_ref()

        check_not_none(arr_ref)
        short_array = arr_ref.shorts()
        check_index(len(short_array), index)
        stack.push_numeric(short_array[index])
