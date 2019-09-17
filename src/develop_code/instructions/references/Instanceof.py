#!/usr/bin/env python
# encoding: utf-8
"""
@author: HuRuiFeng
@file: Instanceof.py
@time: 2019/9/16 20:15
@desc: instanceof指令是判断对象是否是某个类的实例（或者对象的类是否实现了某个接口），并把结果推入操作数栈。
需要两个操作数，第一个操作数是uint16索引，从方法的字节码中获取，通过这个索引可以从当前类的运行时常量池中找到一个类符号引用。
第二个操作数是对象引用，从操作数栈中弹出。
"""
from instructions.base.Instruction import Index16Instruction
from rtda.Frame import Frame


class INSTANCE_OF(Index16Instruction):
    def execute(self, frame: Frame):
        stack = frame.operand_stack
        # 弹出对象引用
        ref = stack.pop_ref()

        # 如果是null，则把0推入操作数栈。
        if not ref:
            stack.push_numeric(0)
            return

        cp = frame.method.get_class().constant_pool
        class_ref = cp.get_constant(self.index)
        clazz = class_ref.resolved_class()
        if ref.is_instance_of(clazz):
            stack.push_numeric(1)
        else:
            stack.push_numeric(0)
