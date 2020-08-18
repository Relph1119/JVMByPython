#!/usr/bin/env python
# encoding: utf-8
"""
@author: HuRuiFeng
@file: CompositeEntry.py
@time: 2019/9/12 11:27
@desc: 通配符实例类（继承CompositeEntry类）
"""

import os
from ch02.classpath.ZipEntry import ZipEntry
from ch02.classpath.CompositeEntry import CompositeEntry


class WildcardEntry(CompositeEntry):

    def __init__(self, path):
        super().__init__(path)
        # 移除路径末尾的'*'符号
        base_dir = path[:-1]
        # 遍历base_dir创建zipEntry
        for root, dirs, files in os.walk(base_dir):
            for name in files:
                if name.endswith(".jar") or name.endswith(".JAR"):
                    jar_entry = ZipEntry(os.path.join(root, name))
                    self.compositeEntryList.append(jar_entry)
