#!/usr/bin/env python
# encoding: utf-8
"""
@author: HuRuiFeng
@file: ExceptionTable.py
@time: 2019/9/22 10:56
@desc: 异常处理表类
"""


class ExceptionTable(list):
    def __init__(self):
        super().__init__()

    def find_exception_handler(self, exClass, pc):
        """
        1. start_pc给出的是try{}语句块的第一条指令，end_pc给出的是try{}语句块的下一条指令。
        2. 如果catch_type是None（在class文件中是0），表示可以处理所有异常，这是用来实现finally子句的。
        :param exClass:
        :param pc:
        :return:
        """
        for _, handler in enumerate(self):
            if handler.start_pc <= pc < handler.end_pc:
                if handler.catch_type is None:
                    return handler

                catch_class = handler.catch_type.resolved_class()
                if catch_class == exClass or catch_class.is_super_class_of(exClass):
                    return handler

        return None


class ExceptionHandler:
    def __init__(self):
        # start_pc和end_pc可以锁定一部分字节码，这些字节码对应某个可能抛出异常的try{}代码。
        self.start_pc = 0
        self.end_pc = 0
        # 指出负责异常处理的catch{}块的位置
        self.handler_pc = 0
        # catch_type是个索引，通过它可以从运行时常量池中查到一个类符号引用。
        self.catch_type = None


# 把Class文件中的异常处理表转换成ExceptionTable类型
def new_exception_table(entries, constant_pool):
    table = []
    for entry in entries:
        exception_handler = ExceptionHandler()
        exception_handler.start_pc = int(entry.start_pc)
        exception_handler.end_pc = int(entry.end_pc)
        exception_handler.handler_pc = int(entry.handler_pc)
        exception_handler.catch_type = get_catch_type(int(entry.catch_type), constant_pool)
        table.append(exception_handler)


def get_catch_type(index, constant_pool):
    """
    从运行时常量池中查找类符号引用。
    异常处理项的catch_type有可能是0，我们知道0是无效的常量池索引，
    但是这里0并非表示catch-none，而是表示catch-all
    :param index:
    :param constant_pool:
    :return:
    """
    if index == 0:
        return None

    return constant_pool.get_constant(index)
