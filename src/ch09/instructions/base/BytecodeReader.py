#!/usr/bin/env python
# encoding: utf-8
"""
@author: HuRuiFeng
@file: BytecodeReader.py
@time: 2019/9/15 17:10
@desc: 字节码读取类
"""

import ctypes


class BytecodeReader:
    def __init__(self):
        # 存放字节码
        self.code = []
        # 记录读取到了哪个字节
        self.pc = 0

    # 为了避免每次解码指令都要新创建一个BytecodeReader实例，定义一个reset()方法
    def reset(self, code, pc):
        self.code = code
        self.pc = pc

    def read_uint8(self):
        i = self.code[self.pc]
        self.pc += 1
        return ctypes.c_uint8(i).value

    # 读取到的值转成int8返回
    def read_int8(self):
        i = self.code[self.pc]
        self.pc += 1
        return ctypes.c_int8(i).value

    # 连续读取两字节
    def read_uint16(self):
        byte1 = self.read_uint8()
        byte2 = self.read_uint8()
        return (byte1 << 8) | byte2

    # 调用read_uint16()，把读取到的值转成int16返回
    def read_int16(self):
        return ctypes.c_int16(self.read_uint16()).value

    # 连续读取4字节
    def read_int32(self):
        byte1 = self.read_uint8()
        byte2 = self.read_uint8()
        byte3 = self.read_uint8()
        byte4 = self.read_uint8()
        return ctypes.c_int32((byte1 << 24) | (byte2 << 16) | (byte3 << 8) | byte4).value

    def skip_padding(self):
        while self.pc % 4 != 0:
            self.read_uint8()

    def read_int32s(self, n):
        ints = []
        for i in range(n):
            ints.append(self.read_int32())
        return ints
