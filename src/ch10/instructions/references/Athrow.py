#!/usr/bin/env python
# encoding: utf-8
"""
@author: HuRuiFeng
@file: Athrow.py
@time: 2019/9/22 12:57
@desc: athrow指令，操作数是一个异常对象引用，从操作数栈弹出。
"""
from instructions.base.Instruction import NoOperandsInstruction
from rtda.Frame import Frame
from rtda.heap import StringPool


class ATHROW(NoOperandsInstruction):
    def execute(self, frame: Frame):
        # 先从操作数栈中弹出异常对象引用
        ex = frame.operand_stack.pop_ref()
        # 如果该引用是None，则抛出NullPointerException异常
        if ex is None:
            raise RuntimeError("java.lang.NullPointerException")

        # 否则看是否可以找到并跳转到异常处理代码
        thread = frame.thread
        if not find_and_goto_exception_handler(thread, ex):
            # 遍历完Java虚拟机栈还是找不到异常处理代码，则打印出Java虚拟机栈信息
            handle_uncaught_exception(thread, ex)


def find_and_goto_exception_handler(thread, ex) -> bool:
    """
    从当前帧开始，遍历Java虚拟机栈，查找方法的异常处理表。
    假设遍历到帧F，如果在F对应的方法中找不到异常处理项，则把F弹出，继续遍历。
    如果找到了异常处理项，在跳转到异常处理代码之前，要先把F的操作数栈清空，然后把异常对象引用推入栈顶。
    :param thread:
    :param ex:
    :return:
    """
    while True:
        frame = thread.current_frame
        pc = frame.next_pc - 1

        handler_pc = frame.method.find_exception_handler(ex.get_class(), pc)
        if handler_pc > 0:
            stack = frame.operand_stack
            stack.clear()
            stack.push_ref(ex)
            frame.next_pc = handler_pc
            return True

        thread.pop_frame()
        # 由于Java虚拟机栈已经空了，所以解释器也就终止执行了。
        if thread.is_stack_empty():
            break

    return False


# 打印Java虚拟机栈信息
def handle_uncaught_exception(thread, ex):
    """
    把Java虚拟机栈清空，然后打印出异常信息。
    :param thread:
    :param ex:
    :return:
    """
    thread.clear_stack()

    j_msg = ex.get_ref_var("detailMessage", "Ljava/lang/String;")
    python_msg = StringPool.python_string(j_msg)
    print(ex.get_class().java_name + ": " + python_msg)

    # 打印异常信息
    for ste in ex.extra:
        print("\tat", ste)
