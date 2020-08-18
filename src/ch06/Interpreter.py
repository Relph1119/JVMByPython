#!/usr/bin/env python
# encoding: utf-8
"""
@author: HuRuiFeng
@file: Interpreter.py
@time: 2019/9/15 21:59
@desc: 解释器
"""

from ch06.rtda.Thread import Thread
from ch06.rtda.heap.Method import Method


class Interpreter:

    @staticmethod
    def interpret(method: Method):
        thread = Thread()
        frame = thread.new_frame(method)
        thread.push_frame(frame)
        try:
            Interpreter.loop(thread, method.code)
        except RuntimeError as e:
            print("LocalVars: {0}".format(frame.local_vars))
            print("OperandStack: {0}".format(frame.operand_stack))
            print(e)

    @staticmethod
    def loop(thread, bytecode):
        from ch06.instructions.base.BytecodeReader import BytecodeReader
        from ch06.instructions.Factory import Factory

        frame = thread.pop_frame()
        reader = BytecodeReader()

        while True:
            pc = frame.next_pc
            thread.pc = pc

            reader.reset(bytecode, pc)
            opcode = reader.read_uint8()
            inst = Factory.new_instruction(opcode)
            inst.fetch_operands(reader)
            frame.next_pc = reader.pc

            print("pc:{0} opcode:{1} inst:{2} [{3}]".format(pc, hex(opcode), inst.__class__.__name__,
                                                            Interpreter.print_obj(inst)))
            inst.execute(frame)

    @staticmethod
    def print_obj(obj):
        return ' '.join(['%s:%s' % item for item in obj.__dict__.items()])
