#!/usr/bin/env python
# encoding: utf-8
"""
@author: HuRuiFeng
@file: Slot.py
@time: 2019/9/15 16:22
@desc: Slot类，可以容纳一个int值和一个引用值
"""


class Slot:
    def __init__(self):
        # 存放整数
        self.num = 0
        # 存放引用
        self.ref = None
