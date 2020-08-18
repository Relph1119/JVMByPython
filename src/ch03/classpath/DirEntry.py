#!/usr/bin/env python
# encoding: utf-8
"""
@author: HuRuiFeng
@file: DirEntry.py
@time: 2019/9/12 11:05
@desc: 目录形式的类路径（继承Entry类）
"""

from ch03.classpath.Entry import Entry
import os


class DirEntry(Entry):

    # 构造函数
    def __init__(self, path):
        # 将参数转换成绝对路径
        self.absDir = os.path.abspath(path)

    def read_class(self, class_name):
        file_name = os.path.join(self.absDir, class_name)
        data, error = None, None
        try:
            data = open(file_name, "rb").read()
        except IOError as e:
            error = e
        return data, self, error

    def __str__(self):
        return self.absDir
