#!/usr/bin/env python
# encoding: utf-8
"""
@author: HuRuiFeng
@file: ClassReader.py
@time: 2019/9/12 14:41
@desc: 读取class文件中的字节
"""


class ClassReader:
    def __init__(self, class_data):
        self.data = class_data

    # 读取u1类型数据
    def read_unit8(self):
        val = self.data[:1]
        self.data = self.data[1:]
        return val

    # 读取u2类型数据
    def read_unit16(self):
        val = self.data[:2]
        self.data = self.data[2:]
        return val

    # 读取u4类型数据
    def read_unit32(self):
        val = self.data[:4]
        self.data = self.data[4:]
        return val

    # 读取u8类型数据
    def read_unit64(self):
        val = self.data[:8]
        self.data = self.data[8:]
        return val

    # 读取uint16表
    def read_unit16s(self):
        # 表的大小由开头的uint16数据指出
        n = int.from_bytes(self.read_unit16(), byteorder='big')
        s = []
        for i in range(n):
            s.append(int.from_bytes(self.read_unit16(), byteorder='big'))
        return s

    # 读取指定数量的字节
    def read_bytes(self, n):
        bytes_data = self.data[:n]
        self.data = self.data[n:]
        return bytearray(bytes_data)
