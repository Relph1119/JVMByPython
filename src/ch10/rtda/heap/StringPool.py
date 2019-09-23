#!/usr/bin/env python
# encoding: utf-8
"""
@author: HuRuiFeng
@file: StringPool.py
@time: 2019/9/20 15:54
@desc: 字符串池
"""

from rtda.heap.ClassLoader import ClassLoader
from rtda.heap.Object import Object

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


# 把python字符串（utf-8格式）转成Java字符数组（utf-16格式）
def string_to_utf16(s):
    """
    不能采用直接utf-8编码[s.encode("utf-8")]的原因：由于在python中存储的是字符串汉字（一个字符串表示三个字符，即三个整数），
    但是在Java中只能是一个汉字字符表示一个整数
    :param s:
    :return:
    """
    return [ord(char) for char in s]


# 得到python字符串
def python_string(j_str):
    # 拿到String对象的value变量值
    char_array = j_str.get_ref_var("value", "[C")
    # if not isinstance(char_array, bytes):
    #     char_array.data = bytes(char_array.data)
    # 把字符数组转换成python字符串
    return utf16_to_string(char_array.chars())


def utf16_to_string(data):
    return "".join([chr(d) for d in data])


def intern_string(j_str):
    """
    如果字符串还没有入池，把它放入并返回该字符串，否则找到已入池字符串并返回。
    :param j_str:
    :return:
    """
    python_str = python_string(j_str)
    interned = interned_strings.get(python_str)
    if interned is not None:
        return interned

    interned_strings[python_str] = j_str
    return j_str
