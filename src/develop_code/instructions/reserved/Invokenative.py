#!/usr/bin/env python
# encoding: utf-8
"""
@author: HuRuiFeng
@file: Invokenative.py
@time: 2019/9/20 20:07
@desc: invokenative指令，调用本地方法
"""
import importlib

from instructions.base.Instruction import NoOperandsInstruction
from native.Registry import find_native_method
from rtda.Frame import Frame

# 模块名
modules = [
    'native.Registry',
    'native.java.lang.Class',
    'native.java.lang.Object',
    'native.java.lang.String',
    'native.java.lang.Double',
    'native.java.lang.Float',
    'native.java.lang.System',
]


class INVOKE_NATIVE(NoOperandsInstruction):
    def execute(self, frame: Frame):
        method = frame.method
        class_name = method.get_class().name
        method_name = method.name
        method_descriptor = method.descriptor

        # 根据类名、方法名和方法描述符从本地方法注册表中查找本地方法实现
        native_method = find_native_method(class_name, method_name, method_descriptor)
        # 如果找不到，抛出UnstatisfiedLinkError异常
        if native_method is None:
            method_info = class_name + '.' + method_name + method_descriptor
            raise RuntimeError("java.lang.UnstatisfiedLinkError: " + method_info)

        # 否则调用本地方法
        native_method_name = native_method.__name__

        for module_name in modules:
            # 动态模块加载
            module = importlib.import_module(module_name)
            # 如果方法在模块内
            if native_method_name in dir(module):
                # 执行该方法
                native_method(frame)
