#!/usr/bin/env python
# encoding: utf-8
"""
@author: HuRuiFeng
@file: CpSymRef.py
@time: 2019/9/16 17:53
@desc: 符号引用基类
"""


class SymRef:
    def __init__(self):
        # 用于存放符号引用所在的运行时常量池
        self.cp = None
        # 类的完全限定名
        self.class_name = ""
        # 缓存解析后的类
        self._class = None

    def get_class(self):
        return self._class

    # 解析类
    def resolved_class(self):
        if self.get_class() is None:
            self.resolve_class_ref()

        return self.get_class()

    # 类符号引用解析
    def resolve_class_ref(self):
        """
        如果类D通过符号引用N应用类C的话，要解析N，先用D的类加载器加载C，然后检查D是否有权限访问C，
        如果没有，则抛出IllegalAccessError异常。
        :return:
        """
        d = self.cp.get_class()
        c = d.loader.load_class(self.class_name)
        if not c.is_accessible_to(d):
            raise RuntimeError("java.lang.IllegalAccessError")
        self._class = c
