#!/usr/bin/env python
# encoding: utf-8
"""
@author: HuRuiFeng
@file: Throwable.py
@time: 2019/9/22 10:44
@desc: java.lang.Throwable类
"""
from native.Registry import register

from rtda.Frame import Frame

# 用于记录Java虚拟机栈帧信息
from rtda.heap.Class import Class


class StackTraceElement:
    def __init__(self):
        # 类所在的文件名
        self.file_name = ""
        # 声明方法的类名
        self.class_name = ""
        # 方法名
        self.method_name = ""
        # 帧正在执行的代码行号
        self.line_number = 0

    def __str__(self):
        return "{0}.{1}({2}:{3})".format(self.class_name, self.method_name, self.file_name, self.line_number)


def fill_in_stack_trace(frame: Frame):
    """
    private native Throwable fillInStackTrace(int dummy);
    (I)Ljava/lang/Throwable;
    :param frame:
    :return:
    """

    this = frame.local_vars.get_this()
    frame.operand_stack.push_ref(this)

    stes = create_stack_trace_elements(this, frame.thread)
    this.extra = stes


def create_stack_trace_elements(t_obj, thread):
    # 由于栈顶两帧正在执行fillInStackTrace(int)和fillInStackTrace()方法，需要跳过这两帧。
    # 下面几帧正在执行异常类的构造函数，也需要跳过，具体要跳过多少帧树需要看异常类的继承层次。
    skip = distance_to_object(t_obj.get_class()) + 2
    # 获得完整的Java虚拟机栈
    frames = thread.get_frames()[skip:]
    stes = []
    for _, frame in enumerate(frames):
        stes.append(create_stack_trace_element(frame))

    return stes


# 计算所需跳过的帧数
def distance_to_object(clazz: Class):
    distance = 0
    c = clazz.super_class
    while c is not None:
        distance += 1
        c = c.super_class

    return distance


# 根据帧创建StackTraceElement实例
def create_stack_trace_element(frame):
    method = frame.method
    clazz = method.get_class()
    stack_trace_element = StackTraceElement()
    stack_trace_element.file_name = clazz.source_file
    stack_trace_element.class_name = clazz.java_name
    stack_trace_element.method_name = method.name
    stack_trace_element.line_number = method.get_line_number(frame.next_pc - 1)

    return stack_trace_element


jlThrowable = "java/lang/Throwable"
register(jlThrowable, "fillInStackTrace", "(I)Ljava/lang/Throwable;", fill_in_stack_trace)
