#!/usr/bin/env python
# encoding: utf-8
"""
@author: HuRuiFeng
@file: Main.py
@time: 2019/9/12 9:55
@desc: 主函数
"""

import os
from optparse import OptionParser

from Cmd import Cmd
from classfile.ClassFile import ClassFile
from classpath import Classpath


def main(input_args):
    # 设置传入参数
    parser = OptionParser(usage="usage:%prog [-options] class [args...]")

    parser.add_option("-v", "--version", action="store_true", default=False, dest="version_flag",
                      help="print version and exit.")
    parser.add_option("--cp", action="store", type="string", dest="cpOption", help="classpath")
    parser.add_option("--classpath", action="store", type="string", dest="cpOption", help="classpath")
    parser.add_option("--Xjre", action="store", type="string", dest="XjreOption", help="path to jre")
    # 解析参数
    (options, args) = parser.parse_args(input_args)
    if options:
        cmd = Cmd(options, args)

        if not options.version_flag:
            # 启动JVM
            start_JVM(cmd)


# 启动JVM函数
def start_JVM(cmd):
    # 解析类路径
    class_path = Classpath.Classpath.parse(cmd.XjreOption, cmd.cpOption)
    # 读取主类数据
    class_name = cmd.class_name.replace(".", "/")

    class_file = load_class(class_name, class_path)
    print(cmd.class_name)
    print_class_info(class_file)


# 加载class
def load_class(class_name, class_path):
    class_data, _, error = class_path.read_class(class_name)

    class_file = ClassFile()
    cf = class_file.parse(class_data)
    return cf


# 把class文件的一些重要信息打印出来
def print_class_info(class_file):
    print("version: {0}.{1}".format(class_file.major_version, class_file.minor_version))
    print("constants count: {0}".format(len(class_file.constant_pool.cp)))
    print("access flags: {0}".format(hex(int.from_bytes(class_file.access_flags, byteorder="big"))))
    print("this class: {0}".format(class_file.class_name))
    print("super class: {0}".format(class_file.super_class_name))
    print("interfaces: {0}".format(class_file.interface_names))
    print("fields count: {0}".format(len(class_file.fields)))
    for f in class_file.fields:
        print("   {0}".format(f.name))
    print("methods count: {0}".format(len(class_file.methods)))
    for m in class_file.methods:
        print("   {0}".format(m.name))


if __name__ == '__main__':
    Xjre_path = os.path.join(os.environ.get("JAVA_HOME"), "jre")

    # 指定-Xjre选项和类名
    fake_args = ['--Xjre', Xjre_path, 'java.lang.String']
    # fake_args = ['--Xjre', Xjre_path, 'java/lang/CharSequence']
    main(fake_args)
