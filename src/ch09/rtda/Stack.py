#!/usr/bin/env python
# encoding: utf-8
"""
@author: HuRuiFeng
@file: Stack.py
@time: 2019/9/15 16:13
@desc: Java虚拟机栈
"""
from rtda.Frame import Frame


class Stack:
    def __init__(self, max_size):
        self.max_size = max_size
        self.size = 0
        self.__top = None

    # 把帧推入栈顶
    def push(self, frame: Frame):
        # 如果栈已经满了，抛出StackOverflowError异常
        if self.size >= self.max_size:
            raise RuntimeError("java.lang.StackOverflowError")
        if self.__top:
            frame.lower = self.__top
        self.__top = frame
        self.size += 1

    # 把栈顶帧弹出
    def pop(self):
        if self.__top is None:
            raise RuntimeError("jvm stack is empty!")

        top = self.__top
        self.__top = top.lower
        top.lower = None
        self.size -= 1

        return top

    # 返回栈顶帧，但并不弹出
    def top(self):
        if self.__top is None:
            raise RuntimeError("jvm stack is empty!")
        return self.__top

    def is_empty(self):
        return self.__top is None
