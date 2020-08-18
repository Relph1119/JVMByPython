#!/usr/bin/env python
# encoding: utf-8
"""
@author: HuRuiFeng
@file: StringPool.py
@time: 2019/9/20 15:54
@desc: 字符串池
"""

from ch08.rtda.heap.ClassLoader import ClassLoader
from ch08.rtda.heap.Object import Object

# 字符串池
interned_strings = dict()


def j_string(loader: ClassLoader, python_str):
    """
    根据python字符串返回相应的Java字符串实例
    :param loader: 
    :param python_str: 
    :return:
    """

    # 如果Java字符串已经在池中，直接返回
    interned_str = interned_strings.get(python_str)
    if interned_str:
        return interned_str

    # 把python字符串（utf-8格式）转成Java字符数组（utf-16格式）
    chars = string_to_utf16(python_str)
    # 创建一个Java字符串实例
    j_chars = Object(loader.load_class("[C"), chars)

    # 把字符串实例的value变量设置成刚刚转换过来的字符数组
    j_str = loader.load_class("java/lang/String").new_object()
    j_str.set_ref_var("value", "[C", j_chars)

    # 把Java字符串放入池中
    interned_strings[python_str] = j_str
    return j_str


def string_to_utf16(s):
    return s.encode("utf-8")


# 得到python字符串
def python_string(j_str):
    # 拿到String对象的value变量值
    char_array = j_str.get_ref_var("value", "[C")
    # 把字符数组转换成python字符串
    return utf16_to_string(char_array.chars())


def utf16_to_string(s):
    return s.decode('utf-8')
