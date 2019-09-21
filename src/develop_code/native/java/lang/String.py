#!/usr/bin/env python
# encoding: utf-8
"""
@author: HuRuiFeng
@file: String.py
@time: 2019/9/21 10:56
@desc: java.lang.String类
"""
from native.Registry import register
from rtda.Frame import Frame
from rtda.heap import StringPool


def intern(frame:Frame):
    this = frame.local_vars.get_this()
    interned = StringPool.intern_string(this)
    frame.operand_stack.push_ref(interned)


register("java/lang/String", "intern",
         "()Ljava/lang/String;", intern)
