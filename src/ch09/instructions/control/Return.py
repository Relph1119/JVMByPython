#!/usr/bin/env python
# encoding: utf-8
"""
@author: HuRuiFeng
@file: Return.py
@time: 2019/9/17 09:34
@desc: 返回指令，方法执行完毕之后，需要把结果返回给调用方
"""

from instructions.base.Instruction import NoOperandsInstruction
from rtda.Frame import Frame


def _numeric_return(frame: Frame):
    thread = frame.thread
    current_frame = thread.pop_frame()
    invoker_frame = thread.top_frame
    val = current_frame.operand_stack.pop_numeric()
    invoker_frame.operand_stack.push_numeric(val)


class RETURN(NoOperandsInstruction):
    def execute(self, frame):
        frame.thread.pop_frame()


class ARETURN(NoOperandsInstruction):
    def execute(self, frame):
        thread = frame.thread
        current_frame = thread.pop_frame()
        invoker_frame = thread.top_frame
        ref = current_frame.operand_stack.pop_ref()
        invoker_frame.operand_stack.push_ref(ref)


class DRETURN(NoOperandsInstruction):
    def execute(self, frame):
        thread = frame.thread
        current_frame = thread.pop_frame()
        invoker_frame = thread.top_frame
        val = current_frame.operand_stack.pop_double()
        invoker_frame.operand_stack.push_double(val)


class FRETURN(NoOperandsInstruction):
    def execute(self, frame):
        thread = frame.thread
        current_frame = thread.pop_frame()
        invoker_frame = thread.top_frame
        val = current_frame.operand_stack.pop_float()
        invoker_frame.operand_stack.push_float(val)


class IRETURN(NoOperandsInstruction):
    def execute(self, frame):
        _numeric_return(frame)


class LRETURN(NoOperandsInstruction):
    def execute(self, frame):
        _numeric_return(frame)
