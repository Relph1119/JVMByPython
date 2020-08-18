#!/usr/bin/env python
# encoding: utf-8
"""
@author: HuRuiFeng
@file: ClassInitLogic.py
@time: 2019/9/17 10:42
@desc: 类的初始化
"""
from ch10.rtda.Thread import Thread
from ch10.rtda.heap.Class import Class


# 查找并调用类的初始化方法
def init_class(thread: Thread, clazz: Class):
    # 把类的init_started状态设置成true
    clazz.start_init()
    schedule_clinit(thread, clazz)
    init_super_class(thread, clazz)


# 准备执行类的初始化方法
def schedule_clinit(thread: Thread, clazz: Class):
    clinit = clazz.get_clinit_method()
    if clinit is not None:
        new_frame = thread.new_frame(clinit)
        thread.push_frame(new_frame)


# 超类的初始化方法
def init_super_class(thread: Thread, clazz: Class):
    if not clazz.is_interface():
        super_class = clazz.super_class
        if super_class is not None and not super_class.init_started:
            init_class(thread, super_class)
