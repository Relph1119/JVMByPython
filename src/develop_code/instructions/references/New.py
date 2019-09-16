#!/usr/bin/env python
# encoding: utf-8
"""
@author: HuRuiFeng
@file: New.py
@time: 2019/9/16 19:44
@desc: new指令
"""

from instructions.base.Instruction import Index16Instruction
from rtda.Frame import Frame


class NEW(Index16Instruction):
    def execute(self, frame: Frame):
        """
        从当前类的运行时常量池中找到一个类符号索引，解析这个类符号引用，拿到类数据，然后创建对象，并把对象引用推入栈顶。
        :param frame:
        :return:
        """
        cp = frame.method.get_class().constant_pool
        class_ref = cp.get_constant(self.index)
        clazz = class_ref.resolve_class()

        if clazz.is_interface() or clazz.is_abstract():
            raise RuntimeError("java.lang.InstantiationError")

        ref = clazz.new_object()
        frame.operand_stack.push_ref(ref)
