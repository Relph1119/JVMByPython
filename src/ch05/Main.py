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
from Interpreter import Interpreter
from classfile.ClassFile import ClassFile
from classpath import Classpath


def main(input_args=None):
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
    # 打印命令行参数
    print("classpath:{0} class:{1} args:{2}".format(class_path, cmd.class_name, cmd.args))

    class_name = cmd.class_name.replace(".", "/")
    # 读取并解析class文件
    cf = load_class(class_name, class_path)
    # 查找类的main()方法
    main_method = get_main_method(cf)
    if main_method:
        # 调用interpret()函数解释执行main()方法
        Interpreter.interpret(main_method)
    else:
        print("Main method not found in class {0}".format(cmd.class_name))


# 读取并解析class文件
def load_class(class_name, class_path: Classpath):
    class_data, _, error = class_path.read_class(class_name)

    class_file = ClassFile(class_data)
    cf = class_file.parse()
    return cf


# 查找类的main()方法
def get_main_method(classFile):
    for m in classFile.methods:
        if m.name == "main" and m.descriptor == "([Ljava/lang/String;)V":
            return m
    return None


if __name__ == '__main__':
    Xjre_path = os.path.join(os.environ.get("JAVA_HOME"), "jre")
    # 得到项目路径的绝对地址
    root_path = os.path.abspath(os.path.join(os.path.dirname(__file__), os.pardir))
    # 得到java的用户类路径
    resources_path = os.path.join(os.path.dirname(root_path), "java")

    # 采用指定用户类路径--cp，执行GaussTest程序
    fake_args = ['--Xjre', Xjre_path, '--cp', resources_path, 'jvmgo.book.ch05.GaussTest']
    main(fake_args)

    # 采用指定用户类路径--cp，执行ShTest程序
    # fake_args = ['--Xjre', Xjre_path, '--cp', resources_path, 'jvmgo.book.ch05.ShTest']
    # main(fake_args)
