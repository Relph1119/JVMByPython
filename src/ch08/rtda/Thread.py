#!/usr/bin/env python
# encoding: utf-8
"""
@author: HuRuiFeng
@file: Thread.py
@time: 2019/9/15 16:04
@desc: 线程
"""

from ch08.rtda.heap.Method import Method


class Thread:
    def __init__(self):
        from ch08.rtda.Stack import Stack
        self.pc = 0
        self.stack = Stack(1024)

    def push_frame(self, frame):
        self.stack.push(frame)

    def pop_frame(self):
        return self.stack.pop()

    @property
    def current_frame(self):
        return self.stack.top()

    def new_frame(self, method: Method):
        from ch08.rtda.Frame import Frame
        return Frame(self, method)

    @property
    def top_frame(self):
        return self.stack.top()

    def is_stack_empty(self):
        return self.stack.is_empty()
