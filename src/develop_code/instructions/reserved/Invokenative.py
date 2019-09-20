#!/usr/bin/env python
# encoding: utf-8
"""
@author: HuRuiFeng
@file: Invokenative.py
@time: 2019/9/20 20:07
@desc: invokenative指令
"""
import importlib

from instructions.base.Instruction import NoOperandsInstruction
from native.Registry import find_native_method
from rtda.Frame import Frame

# 模块名
modules = [
    'native.Registry',
    'native.java.lang.Class',
    'native.java.lang.Object'
]


class INVOKE_NATIVE(NoOperandsInstruction):
    def execute(self, frame: Frame):
        method = frame.method
        class_name = method.get_class().name
        method_name = method.name
        method_descriptor = method.descriptor

        native_method = find_native_method(class_name, method_name, method_descriptor)
        if native_method is None:
            method_info = class_name + '.' + method_name + method_descriptor
            raise RuntimeError("java.lang.UnstatisfiedLinkError: " + method_info)

        native_method_name = native_method.__name__

        for module_name in modules:
            module = importlib.import_module(module_name)
            if native_method_name in dir(module):
                native_method(frame)
