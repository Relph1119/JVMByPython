#!/usr/bin/env python
# encoding: utf-8
"""
@author: HuRuiFeng
@file: Instruction.py
@time: 2019/9/15 16:58
@desc: 指令的接口类
"""
import ctypes
from abc import ABCMeta, abstractmethod

from ch07.instructions.base import BytecodeReader
from ch07.rtda import Frame


class Instruction(metaclass=ABCMeta):

    # 从字节码中提取操作数
    @abstractmethod
    def fetch_operands(self, reader: BytecodeReader):
        pass

    # 执行指令逻辑
    @abstractmethod
    def execute(self, frame: Frame):
        pass


# 表示没有操作数的指令
class NoOperandsInstruction(Instruction):
    def fetch_operands(self, reader):
        pass

    def execute(self, frame):
        pass


# 表示跳转指令
class BranchInstruction(Instruction):
    def __init__(self):
        # 跳转偏移量
        self.offset = 0

    def fetch_operands(self, reader):
        self.offset = ctypes.c_int(reader.read_int16()).value

    def execute(self, frame):
        pass


# 存储和加载类指令需要根据索引存取局部变量表，索引由单字节操作数给出。
class Index8Instruction(Instruction):
    def __init__(self):
        # 表示局部变量表索引
        self.index = 0

    # 从字节码中读取一个int8整数
    def fetch_operands(self, reader):
        self.index = ctypes.c_uint(reader.read_uint8()).value

    def execute(self, frame):
        pass


# 有一些指令需要访问运行时常量池，常量池索引由两字节操作数给出。
class Index16Instruction(Instruction):
    def __init__(self):
        self.index = 0

    # 从字节码中读取一个uint16整数
    def fetch_operands(self, reader):
        self.index = ctypes.c_uint(reader.read_uint16()).value

    def execute(self, frame):
        pass
