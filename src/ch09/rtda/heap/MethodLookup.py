#!/usr/bin/env python
# encoding: utf-8
"""
@author: HuRuiFeng
@file: MethodLookup.py
@time: 2019/9/17 08:57
@desc: 查找方法
"""
from ch09.rtda.heap.Class import Class


# 在类中查找方法
def lookup_method_in_class(clazz: Class, name, descriptor):
    c = clazz
    while c:
        for method in c.methods:
            if method.name == name and method.descriptor == descriptor:
                return method
        c = c.super_class
    return None


# 在接口中查找方法
def lookup_method_in_interfaces(ifaces, name, descriptor):
    for iface in ifaces:
        for method in iface.methods:
            if method.name == name and method.descriptor == descriptor:
                return method
        method = lookup_method_in_interfaces(iface.interfaces, name, descriptor)
        if method:
            return method

    return None
