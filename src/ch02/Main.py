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
    cp = Classpath.Classpath.parse(cmd.XjreOption, cmd.cpOption)
    # 打印命令行参数
    print("classpath: {0} class: {1} args: {2}".format(cp, cmd.class_name, cmd.args))

    # 读取主类数据
    class_name = cmd.class_name.replace(".", "/")
    class_data, _, error = cp.read_class(class_name)
    if error:
        print("Could not find or load main class {0}\n".format(cmd.class_name))
        exit(0)

    # 打印class里面的数据信息
    print("class data: {0}".format([int(hex(d),16) for d in class_data]))


if __name__ == '__main__':
    Xjre_path = os.path.join(os.environ.get("JAVA_HOME"), "jre")

    # 指定-Xjre选项和类名
    fake_args = ['--Xjre', Xjre_path, 'java.lang.Object']
    main(fake_args)
