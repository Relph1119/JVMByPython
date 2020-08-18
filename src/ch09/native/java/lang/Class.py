#!/usr/bin/env python
# encoding: utf-8
"""
@author: HuRuiFeng
@file: Class.py
@time: 2019/9/20 20:57
@desc: java.lang.Class类
"""
from ch09.native.Registry import register
from ch09.rtda.Frame import Frame
from ch09.rtda.heap.StringPool import python_string, j_string


def get_primitive_class(frame: Frame):
    """
    static native Class<?> getPrimitiveClass(String name);
    getPrimitiveClass()是静态方法
    :param frame:
    :return:
    """
    # 从局部变量表中拿到类名，这是个Java字符串
    name_obj = frame.local_vars.get_ref(0)
    # 把它转成python字符串
    name = python_string(name_obj)

    # 基本类型的类已经加载到了方法区中，直接调用类加载器的load_class()获取
    loader = frame.method.get_class().loader
    clazz = loader.load_class(name).j_class

    # 把类对象引用推入操作数栈顶
    frame.operand_stack.push_ref(clazz)


def get_name_0(frame: Frame):
    """
    private native String getName0()
    :param frame:
    :return:
    """
    # 从局部变量表中拿到this引用，这是一个类对象引用
    this = frame.local_vars.get_this()
    # 通过extra获得与之对应的Class对象
    clazz = this.extra

    # 获取类名
    name = clazz.java_name
    # 转成Java字符串
    name_obj = j_string(clazz.loader, name)

    # 将其推入操作数栈顶
    frame.operand_stack.push_ref(name_obj)


def desired_assertion_status_0(frame: Frame):
    """
    private static native boolean desiredAssertionStatus0(Class<?> clazz);
    :param frame:
    :return:
    """
    # 把false推入操作数栈顶
    frame.operand_stack.push_boolean(False)


register("java/lang/Class", "getPrimitiveClass",
         "(Ljava/lang/String;)Ljava/lang/Class;", get_primitive_class)
register("java/lang/Class", "getName0",
         "()Ljava/lang/String;", get_name_0)
register("java/lang/Class", "desiredAssertionStatus0",
         "(Ljava/lang/Class;)Z", desired_assertion_status_0)
