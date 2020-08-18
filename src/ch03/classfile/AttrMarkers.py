#!/usr/bin/env python
# encoding: utf-8
"""
@author: HuRuiFeng
@file: MarkerAttribute.py
@time: 2019/9/15 09:39
@desc: 起标记作用的属性
"""

from ch03.classfile.AttributeInfo import AttributeInfo


class MarkerAttribute(AttributeInfo):
    def __init__(self):
        pass

    def read_info(self, class_reader):
        pass


# Deprecate属性用于指出类、接口、字段或方法已经不建议使用，编译器等工具可以根据Deprecated属性输出警告信息。
class DeprecatedAttribute(MarkerAttribute):
    def __init__(self):
        super().__init__()


# Synthetic属性用来标记源文件中不存在、由编译器生成的类成员，引入该属性主要是为了支持嵌套类和嵌套接口。
class SyntheticAttribute(MarkerAttribute):
    def __init__(self):
        super().__init__()
