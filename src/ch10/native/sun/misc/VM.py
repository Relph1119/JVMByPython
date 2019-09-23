#!/usr/bin/env python
# encoding: utf-8
"""
@author: HuRuiFeng
@file: VM.py
@time: 2019/9/21 15:31
@desc: VM
"""
from instructions.base import MethodInvokeLogic
from native.Registry import register
from rtda.Frame import Frame
from rtda.heap import StringPool


def initialize(frame: Frame):
    vm_class = frame.method.get_class()
    saved_props = vm_class.get_ref_var("savedProps", "Ljava/util/Properties;")
    key = StringPool.j_string(vm_class.loader, "foo")
    val = StringPool.j_string(vm_class.loader, "bar")
    frame.operand_stack.push_ref(saved_props)
    frame.operand_stack.push_ref(key)
    frame.operand_stack.push_ref(val)
    props_class = vm_class.loader.load_class("java/util/Properties")
    set_prop_method = props_class.get_instance_method("setProperty",
                                                      "(Ljava/lang/String;Ljava/lang/String;)Ljava/lang/Object;")
    MethodInvokeLogic.invoke_method(frame, set_prop_method)


register("sun/misc/VM", "initialize", "()V", initialize)
