#!/usr/bin/env python
# encoding: utf-8
"""
@author: HuRuiFeng
@file: Interpreter.py
@time: 2019/9/15 21:59
@desc: 解释器
"""

from ch07.rtda.Thread import Thread
from ch07.rtda.heap.Method import Method


class Interpreter:

    @staticmethod
    def interpret(method: Method, log_inst: bool):
        thread = Thread()
        frame = thread.new_frame(method)
        thread.push_frame(frame)
        try:
            Interpreter.loop(thread, log_inst)
        except RuntimeError as e:
            Interpreter.log_frames(thread)
            print("LocalVars: {0}".format(frame.local_vars))
            print("OperandStack: {0}".format(frame.operand_stack))
            print(e)

    @staticmethod
    def loop(thread, log_inst):
        from instructions.base.BytecodeReader import BytecodeReader
        from instructions.Factory import Factory

        reader = BytecodeReader()

        while True:
            frame = thread.current_frame
            pc = frame.next_pc
            thread.pc = pc

            reader.reset(frame.method.code, pc)
            op_code = reader.read_uint8()
            inst = Factory.new_instruction(op_code)
            inst.fetch_operands(reader)
            frame.next_pc = reader.pc

            if log_inst:
                Interpreter.log_instruction(frame, inst)

            inst.execute(frame)

            if thread.is_stack_empty():
                break

    @staticmethod
    def log_frames(thread):
        while not thread.is_stack_empty():
            frame = thread.pop_frame()
            method = frame.method
            class_name = method.get_class().name
            print(">> pc: {0:4} {1}.{2}{3}".format(frame.next_pc, class_name, method.name, method.descriptor))

    @staticmethod
    def log_instruction(frame, inst):
        method = frame.method
        class_name = method.get_class().name
        method_name = method.name
        pc = frame.thread.pc
        print("{0}.{1}() #{2:<2} {3} {4} operand_stack: {5} local_vars: {6}".format(class_name, method_name, pc,
                                                                                    inst.__class__.__name__,
                                                                                    Interpreter.print_obj(inst),
                                                                                    frame.operand_stack,
                                                                                    frame.local_vars))

    @staticmethod
    def print_obj(obj):
        return ' '.join(['%s:%s' % item for item in obj.__dict__.items()])
