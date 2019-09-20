#!/usr/bin/env python
# encoding: utf-8
"""
@author: HuRuiFeng
@file: Getfield.py
@time: 2019/9/16 20:12
@desc: getfield指令获取对象的实例变量值，然后推入操作数栈，它需要两个操作数。
第一个是uint16索引，第二个操作数是对象引用。
"""
from instructions.base.Instruction import Index16Instruction
from rtda.Frame import Frame


class GET_FIELD(Index16Instruction):
    def execute(self, frame: Frame):
        cp = frame.method.get_class().constant_pool
        field_ref = cp.get_constant(self.index)
        field = field_ref.resolve_field()

        if field.is_static():
            raise RuntimeError("java.lang.IncompatibleClassChangeError")

        stack = frame.operand_stack
        ref = stack.pop_ref()
        if ref is None:
            raise RuntimeError("java.lang.NollPointerException")

        descriptor = field.descriptor
        slot_id = field.slot_id
        slots = ref.fields

        if descriptor[0] in {"Z", "B", "C", "S", "I", "F", "J", "D"}:
            stack.push_numeric(slots.get_numeric(slot_id))
        elif descriptor[0] in {"L", "["}:
            stack.push_ref(slots.get_ref(slot_id))
