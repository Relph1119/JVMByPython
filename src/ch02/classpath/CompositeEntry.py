#!/usr/bin/env python
# encoding: utf-8
"""
@author: HuRuiFeng
@file: CompositeEntry.py
@time: 2019/9/12 11:19
@desc: 由更小的Entry组成（继承Entry类）
"""

from ch02.classpath.Entry import Entry


class CompositeEntry(Entry):
    def __init__(self, path_list):
        self.compositeEntryList = []

        if path_list.find(Entry.path_list_separator) > 0:
            # 把参数（路径列表）按分隔符分成小路径，然后把每个小路径都转换成具体的Entry实例
            for _, path in path_list.split(Entry.path_list_separator):
                entry = Entry.new_entry(path)
                self.compositeEntryList.append(entry)

    # 依次调用每一个子路径的read_class()方法
    def read_class(self, class_name):
        for entry in self.compositeEntryList:
            data, from_entry, error = entry.read_class(class_name)
            if not error:
                return data, from_entry, None
        return None, None, "class not found:{0}".format(class_name)

    def __str__(self):
        return Entry.path_list_separator.join(str(entry) for entry in self.compositeEntryList)
