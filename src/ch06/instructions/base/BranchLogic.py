#!/usr/bin/env python
# encoding: utf-8
"""
@author: HuRuiFeng
@file: BranchLogic.py
@time: 2019/9/15 21:01
@desc: 跳转逻辑
"""
from ch06.rtda import Frame


def branch(frame: Frame, offset):
    pc = frame.thread.pc
    next_pc = pc + offset
    frame.next_pc = next_pc
