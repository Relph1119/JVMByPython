#!/usr/bin/env python
# encoding: utf-8
"""
@author: HuRuiFeng
@file: Classpath.py
@time: 2019/9/12 11:36
@desc: 类路径执行类
"""

import os.path
from ch09.classpath.WildcardEntry import WildcardEntry
from ch09.classpath.Entry import Entry


class Classpath:
    def __init__(self):
        # 启动类路径
        self.boot_classpath = None
        # 扩展类路径
        self.ext_classPath = None
        # 用户类路径
        self.user_classpath = None

    # 解析类路径方法
    @staticmethod
    def parse(jreOption, cpOption):
        cp = Classpath()
        # -Xjre选项解析启动类路径和扩展类路径
        cp.parse_boot_and_ext_classpath(jreOption)
        # -classpath/-cp选项解析用户类路径
        cp.parse_user_classpath(cpOption)
        return cp

    def parse_boot_and_ext_classpath(self, jreOption):
        jre_dir = self.__get_jre_dir(jreOption)

        jre_lib_path = os.path.join(jre_dir, "lib", "*")
        self.boot_classpath = WildcardEntry(jre_lib_path)

        jre_ext_path = os.path.join(jre_dir, "lib", "ext", "*")
        self.ext_classPath = WildcardEntry(jre_ext_path)

    # 得到JRE路径
    def __get_jre_dir(self, jreOption):
        if jreOption and self.__exists(jreOption):
            return jreOption
        if self.__exists("./jre"):
            return "./jre"
        jh = os.environ.get("JAVA_HOME")
        if jh:
            return os.path.join(jh, "jre")
        raise RuntimeError("Can not find jre folder!")

    # 判断路径是否存在
    @staticmethod
    def __exists(path):
        if os.path.isdir(path):
            return True
        return False

    def parse_user_classpath(self, cp_option):
        if not cp_option:
            cp_option = "."
        self.user_classpath = Entry.new_entry(cp_option)

    def read_class(self, class_name):
        global data, entry, error
        class_name = class_name + ".class"
        if self.boot_classpath:
            data, entry, error = self.boot_classpath.read_class(class_name)
            if not data and self.ext_classPath:
                    data, entry, error = self.ext_classPath.read_class(class_name)
                    if not data and self.user_classpath:
                        return self.user_classpath.read_class(class_name)

        return data, entry, error

    def __str__(self):
        return self.user_classpath.__str__()
