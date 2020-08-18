#!/usr/bin/env python
# encoding: utf-8
"""
@author: HuRuiFeng
@file: Wide.py
@time: 2019/9/15 21:45
@desc: 加载类指令、存储类指令、ret指令和iinc指令需要按索引访问局部变量表，索引以uint8的形式存在字节码中。
对于大部分方法来说，局部变量表大小都不会超过256，
所以用一字节表示索引就够了，如果有方法超过这限制，就用wide指令扩展。
wide指令只是增加索引宽度，并不改变子指令操作。
"""

import ctypes

from ch05.instructions.base.Instruction import NoOperandsInstruction
from ch05.instructions.loads.Aload import ALOAD
from ch05.instructions.loads.Dload import DLOAD
from ch05.instructions.loads.Fload import FLOAD
from ch05.instructions.loads.Iload import ILOAD
from ch05.instructions.loads.Lload import LLOAD
from ch05.instructions.math.Iinc import IINC
from ch05.instructions.stores.Astore import ASTORE
from ch05.instructions.stores.Dstore import DSTORE
from ch05.instructions.stores.Fstore import FSTORE
from ch05.instructions.stores.Istore import ISTORE
from ch05.instructions.stores.Lstore import LSTORE


class WIDE(NoOperandsInstruction):
    def __init__(self):
        self.modified_instruction = None

    def fetch_operands(self, reader):
        opcode = reader.read_uint8()

        if opcode == 0x15:
            inst = ILOAD()
            inst.index = ctypes.c_uint(reader.read_uint16()).value
            self.modified_instruction = inst
        elif opcode == 0x16:
            inst = LLOAD()
            inst.index = ctypes.c_uint(reader.read_uint16()).value
            self.modified_instruction = inst
        elif opcode == 0x17:
            inst = FLOAD()
            inst.index = ctypes.c_uint(reader.read_uint16()).value
            self.modified_instruction = inst
        elif opcode == 0x18:
            inst = DLOAD()
            inst.index = ctypes.c_uint(reader.read_uint16()).value
            self.modified_instruction = inst
        elif opcode == 0x19:
            inst = ALOAD()
            inst.index = ctypes.c_uint(reader.read_uint16()).value
            self.modified_instruction = inst
        elif opcode == 0x36:
            inst = ISTORE()
            inst.index = ctypes.c_uint(reader.read_uint16()).value
            self.modified_instruction = inst
        elif opcode == 0x37:
            inst = LSTORE()
            inst.index = ctypes.c_uint(reader.read_uint16()).value
            self.modified_instruction = inst
        elif opcode == 0x38:
            inst = FSTORE()
            inst.index = ctypes.c_uint(reader.read_uint16()).value
            self.modified_instruction = inst
        elif opcode == 0x39:
            inst = DSTORE()
            inst.index = ctypes.c_uint(reader.read_uint16()).value
            self.modified_instruction = inst
        elif opcode == 0x3a:
            inst = ASTORE()
            inst.index = ctypes.c_uint(reader.read_uint16()).value
            self.modified_instruction = inst
        elif opcode == 0x84:
            inst = IINC()
            inst.index = ctypes.c_uint(reader.read_uint16()).value
            inst.const = ctypes.c_int32(reader.read_int16()).value
            self.modified_instruction = inst
        elif opcode == 0xa9:
            raise RuntimeError("Unsupported opcode: 0xa9!")

    def execute(self, frame):
        self.modified_instruction.execute(frame)
