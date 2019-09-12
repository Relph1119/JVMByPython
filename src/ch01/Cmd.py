#!/usr/bin/env python
# encoding: utf-8
"""
@author: HuRuiFeng
@file: Cmd.py
@time: 2019/9/12 9:55
@desc: 命令行类
"""


class Cmd:
    # 版本号
    version_flag = False
    # 指定用户类路径
    cpOption = ""
    # 类名
    class_name = ""
    # 传入的其他参数，或者是类参数
    args = []

    def __init__(self, options, argvs):
        # 打印版本号
        if options.version_flag:
            self.__print_version()
        elif options.cpOption:
            self.cpOption = options.cpOption

        if argvs:
            self.class_name = argvs[0]
            self.args = argvs[1:] or []

    @staticmethod
    def __print_version():
        print("version 0.0.1")

    def print_classpath(self):
        print("classpath:{0} class:{1} args:{2}\n".format(self.cpOption, self.class_name, self.print_args()))

    # 打印传入参数
    def print_args(self):
        return '[' + ' '.join(self.args) + ']'
