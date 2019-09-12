#!/usr/bin/env python
# encoding: utf-8
"""
@author: HuRuiFeng
@file: Main.py
@time: 2019/9/12 9:55
@desc: 主函数
"""

from optparse import OptionParser

from Cmd import Cmd


def main(input_args):
    parser = OptionParser(usage="usage:%prog [-options] class [args...]")

    parser.add_option("-v", "--version", action="store_true", default=False, dest="versionFlag",
                      help="print version and exit.")
    parser.add_option("--cp", action="store", type="string", dest="cpOption", help="classpath")
    parser.add_option("--classpath", action="store", type="string", dest="cpOption", help="classpath")
    (options, args) = parser.parse_args(input_args)
    if options:
        cmd = Cmd(options, args)
        cmd.print_classpath()


if __name__ == '__main__':
    fake_args = ['--cp', 'foo/bar', 'MyApp', 'arg1', 'arg2']
    main(fake_args)
