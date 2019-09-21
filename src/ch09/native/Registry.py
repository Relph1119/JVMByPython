#!/usr/bin/env python
# encoding: utf-8
"""
@author: HuRuiFeng
@file: Registry.py
@time: 2019/9/20 19:21
@desc: 本地方法注册表，用来注册和查找本地方法
"""

from rtda.Frame import Frame

Registry = dict()


def native_method(frame: Frame):
    pass


def register(class_name, method_name, method_descriptor, method):
    """
    类名、方法名和方法描述符加在一起才能唯一确定一个方法，把它们的组合作为本地方法注册表的键。
    该函数把上面三个信息和本地方法实现关联起来。
    :param class_name: 类名
    :param method_name: 方法名
    :param method_descriptor: 方法描述符
    :param method: 本地方法
    :return:
    """
    key = class_name + "~" + method_name + "~" + method_descriptor
    Registry[key] = method


def find_native_method(class_name, method_name, method_descriptor):
    """
    根据类名、方法名和方法描述符查找本地方法实现，如果找不到，则返回None
    :param class_name: 类名
    :param method_name: 方法名
    :param method_descriptor: 方法描述符
    :return:
    """
    key = class_name + "~" + method_name + "~" + method_descriptor
    method = Registry.get(key)
    if method is not None:
        return method
    if method_descriptor == "()V" and method_name == "registerNatives":
        return empty_native_method

    return None


def empty_native_method(frame: Frame):
    # do nothing
    pass
