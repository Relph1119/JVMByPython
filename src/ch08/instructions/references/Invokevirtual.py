#!/usr/bin/env python
# encoding: utf-8
"""
@author: HuRuiFeng
@file: Invokevirtual.py
@time: 2019/9/16 20:57
@desc: invokevirtual用于打印计算结果
"""
from ch08.instructions.base import MethodInvokeLogic
from ch08.instructions.base.Instruction import Index16Instruction
from ch08.rtda.Frame import Frame
from ch08.rtda.heap import MethodLookup
from ch08.rtda.heap.StringPool import python_string


class INVOKE_VIRTURL(Index16Instruction):
    def execute(self, frame: Frame):
        current_class = frame.method.get_class()
        cp = current_class.constant_pool
        method_ref = cp.get_constant(self.index)
        resolved_method = method_ref.resolved_method()
        if resolved_method.is_static():
            raise RuntimeError("java.lang.IncompatibleClassChangeError")

        ref = frame.operand_stack.get_ref_from_top(resolved_method.arg_slot_count - 1)
        if ref is None:
            if method_ref.name == "println":
                self._println(frame.operand_stack, method_ref.descriptor)
                return
            raise RuntimeError("java.lang.NullPointerException")

        if resolved_method.is_protected() \
                and resolved_method.get_class().is_super_class_of(current_class) \
                and resolved_method.get_class().get_package_name() != current_class.get_package_name() \
                and ref.get_class() != current_class \
                and not ref.get_class().is_sub_class_of(current_class):
            raise RuntimeError("java.lang.IllegalAccessError")

        # 从对象的类中查找真正要调用的方法。如果找不到方法，或者找到的是抽象方法，则抛出AbstractMethodError异常。
        method_to_be_invoked = MethodLookup.lookup_method_in_class(
            ref.get_class(), method_ref.name, method_ref.descriptor)
        if not method_to_be_invoked or method_to_be_invoked.is_abstract():
            raise RuntimeError("java.lang.AbstractMethodError")

        MethodInvokeLogic.invoke_method(frame, method_to_be_invoked)

    @staticmethod
    def _println(stack, descriptor):
        if descriptor == "(Z)V":
            print("{0}".format(stack.pop_numeric() != 0))
        elif descriptor in {"(C)V", "(B)V", "(S)V", "(I)V", "(J)V", "(F)V", "(D)V"}:
            print("{0}".format(stack.pop_numeric()))
        elif descriptor == "(Ljava/lang/String;)V":
            j_str = stack.pop_ref()
            python_str = python_string(j_str)
            print("{0}".format(python_str))
        else:
            raise RuntimeError("println: " + descriptor)
        stack.pop_ref()
