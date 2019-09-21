#!/usr/bin/env python
# encoding: utf-8
"""
@author: HuRuiFeng
@file: ClassNameHelper.py
@time: 2019/9/17 21:22
@desc: 类名-数组类名工具
"""

PrimitiveTypes = {
    "void": "V",
    "boolean": "Z",
    "byte": "B",
    "short": "S",
    "int": "I",
    "long": "J",
    "char": "C",
    "float": "F",
    "double": "D"
}


# 根据类名得到数组类名
def get_array_class_name(class_name):
    # 把类名转变成类型描述符，然后在前面加上[
    return "[" + to_descriptor(class_name)


# 把类名转变成类型描述符
def to_descriptor(class_name):
    if class_name[0] == '[':
        return class_name

    return PrimitiveTypes.get(class_name) or "L" + class_name + ";"


# 把类型描述符转变成类名
def to_class_name(descriptor):
    # 如果类型描述符以[开头，则肯定是数组，描述符即是类名。
    if descriptor[0] == '[':
        return descriptor
    # 如果类型描述符以L开头，则肯定是类描述符，去掉开头的L好末尾的;即是类名。
    if descriptor[0] == 'L':
        return descriptor[1: len(descriptor) - 1]
    # 判断是否是基本类型描述符，如果是，返回基本类型名称
    for class_name, d in PrimitiveTypes.items():
        if d == descriptor:
            return class_name

    raise RuntimeError("Invalid descriptor: " + descriptor)
