#!/usr/bin/env python
# encoding: utf-8
"""
@author: HuRuiFeng
@file: Thread.py
@time: 2019/9/15 16:04
@desc: 线程
"""
from ch04.rtda.Stack import Stack


class Thread:
    def __init__(self):
        self.pc = 0
        self.stack = Stack(1024)

    def push_frame(self, frame):
        self.stack.push(frame)

    def pop_frame(self):
        return self.stack.pop()

    @property
    def current_frame(self):
        return self.stack.top()
