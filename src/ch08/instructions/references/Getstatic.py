#!/usr/bin/env python
# encoding: utf-8
"""
@author: HuRuiFeng
@file: Getstatic.py
@time: 2019/9/16 20:04
@desc: getstatic指令和putstatic指令正好相反，它取出类的某个静态变量值，然后推入栈顶。
"""
from ch08.instructions.base import ClassInitLogic
from ch08.instructions.base.Instruction import Index16Instruction
from ch08.rtda.Frame import Frame


class GET_STATIC(Index16Instruction):
    def execute(self, frame: Frame):
        cp = frame.method.get_class().constant_pool
        field_ref = cp.get_constant(self.index)
        field = field_ref.resolve_field()
        clazz = field.get_class()

        if not clazz.init_started:
            frame.revert_next_pc()
            ClassInitLogic.init_class(frame.thread, clazz)
            return

        # 如果解析后的字段不是静态字段，抛出IncompatibleClassChangeError异常
        if not field.is_static():
            raise RuntimeError("java.lang.IncompatibleClassChangeError")

        descriptor = field.descriptor
        slot_id = field.slot_id
        slots = clazz.static_vars
        stack = frame.operand_stack

        if descriptor[0] in {"Z", "B", "C", "S", "I", "F", "J", "D"}:
            stack.push_numeric(slots.get_numeric(slot_id))
        elif descriptor[0] in {"L", "["}:
            stack.push_ref(slots.get_ref(slot_id))
