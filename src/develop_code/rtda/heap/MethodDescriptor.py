#!/usr/bin/env python
# encoding: utf-8
"""
@author: HuRuiFeng
@file: MethodDescriptor.py
@time: 2019/9/16 09:29
@desc: 方法描述符
"""


class MethodDescriptor:
    def __init__(self):
        self.parameter_types = []
        self.return_type = ""

    def add_parameter_type(self, t):
        self.parameter_types.append(t)
