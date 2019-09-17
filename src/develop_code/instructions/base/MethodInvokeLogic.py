#!/usr/bin/env python
# encoding: utf-8
"""
@author: HuRuiFeng
@file: MethodInvokeLogic.py
@time: 2019/9/16 09:05
@desc: 在定位到需要调用的方法之后，Java虚拟机要给这个方法创建一个新的帧并把它推入Java虚拟机栈顶，然后传递参数。
"""
from rtda.Frame import Frame
from rtda.heap.Method import Method


def invoke_method(invoker_frame: Frame, method: Method):
    # 创建新的帧并推入Java虚拟机栈
    thread = invoker_frame.thread
    new_frame = thread.new_frame(method)
    thread.push_frame(new_frame)

    # 确定方法的参数在局部变量表中占用多少位置
    arg_slot_slot = method.arg_slot_count
    if arg_slot_slot > 0:
        for i in range(arg_slot_slot - 1, -1, -1):
            slot = invoker_frame.operand_stack.pop_slot()
            new_frame.local_vars.set_slot(i, slot)

    if method.is_native():
        if method.name == "registerNatives":
            thread.pop_frame()
        else:
            raise RuntimeError(
                "native method: {0}.{1}{2}".format(method.get_class().name, method.name, method.descriptor))
