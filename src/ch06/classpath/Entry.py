#!/usr/bin/env python
# encoding: utf-8
"""
@author: HuRuiFeng
@file: Entry.py
@time: 2019/9/12 10:55
@desc: 类路径项（基类）
"""

from abc import ABCMeta, abstractmethod


class Entry(metaclass=ABCMeta):
    # 路径分隔符
    path_list_separator = ";"

    # 寻找和加载class文件，接口方法
    @abstractmethod
    def read_class(self, class_name):
        pass

    # 根据参数常见不同类型的Entry实例
    @staticmethod
    def new_entry(path):
        from ch06.classpath.CompositeEntry import CompositeEntry
        from ch06.classpath.WildcardEntry import WildcardEntry
        from ch06.classpath.ZipEntry import ZipEntry
        from ch06.classpath.DirEntry import DirEntry

        if Entry.path_list_separator in path:
            return CompositeEntry(path)
        elif path.endswith("*"):
            return WildcardEntry(path)
        elif path.endswith(".jar") or path.endswith(".JAR") or path.endswith(".zip") or path.endswith(".ZIP"):
            return ZipEntry(path)
        else:
            return DirEntry(path)
