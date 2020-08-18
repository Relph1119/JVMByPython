#!/usr/bin/env python
# encoding: utf-8
"""
@author: HuRuiFeng
@file: Main.py
@time: 2019/9/12 9:55
@desc: 主函数
"""

from optparse import OptionParser

from ch01.Cmd import Cmd


def main(input_args):
    # 设置传入参数
    parser = OptionParser(usage="usage:%prog [-options] class [args...]")

    parser.add_option("-v", "--version", action="store_true", default=False, dest="version_flag",
                      help="print version and exit.")
    parser.add_option("--cp", action="store", type="string", dest="cpOption", help="classpath")
    parser.add_option("--classpath", action="store", type="string", dest="cpOption", help="classpath")
    # 解析参数
    (options, args) = parser.parse_args(input_args)
    if options:
        cmd = Cmd(options, args)

        if not options.version_flag:
            # 启动JVM
            start_JVM(cmd)


# 启动JVM函数，暂时只是打印一些信息而已
def start_JVM(cmd):
    cmd.print_classpath()


if __name__ == '__main__':
    # 打印帮助
    # fake_args = ['-h']
    # main(fake_args)

    # 打印版本
    fake_args = ['-v']
    main(fake_args)

    # 使用输入参数测试
    fake_args = ['--cp', 'foo/bar', 'MyApp', 'arg1', 'arg2']
    main(fake_args)
