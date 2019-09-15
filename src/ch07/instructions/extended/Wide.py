from ch07.instructions.base.Instruction import NoOperandsInstruction
from ch07.instructions.loads.Iload import ILOAD
from ch07.instructions.loads.Lload import LLOAD
from ch07.instructions.loads.Fload import FLOAD
from ch07.instructions.loads.Dload import DLOAD
from ch07.instructions.loads.Aload import ALOAD
from ch07.instructions.stores.Istore import ISTORE
from ch07.instructions.stores.Lstore import LSTORE
from ch07.instructions.stores.Fstore import FSTORE
from ch07.instructions.stores.Dstore import DSTORE
from ch07.instructions.stores.Astore import ASTORE
from ch07.instructions.math.Iinc import IINC

import ctypes

class WIDE(NoOperandsInstruction):
    def __init__(self):
        self.modifiedInstruction = None

    def fetchOperands(self, bytecodeReader):
        opcode = bytecodeReader.read_uint8()

        if opcode == 0x15:
            inst = ILOAD()
            inst.index = ctypes.c_uint(bytecodeReader.read_uint16())
            self.modifiedInstruction = inst
        elif opcode == 0x16:
            inst = LLOAD()
            inst.index = ctypes.c_uint(bytecodeReader.read_uint16())
            self.modifiedInstruction = inst
        elif opcode == 0x17:
            inst = FLOAD()
            inst.index = ctypes.c_uint(bytecodeReader.read_uint16())
            self.modifiedInstruction = inst
        elif opcode == 0x18:
            inst = DLOAD()
            inst.index = ctypes.c_uint(bytecodeReader.read_uint16())
            self.modifiedInstruction = inst
        elif opcode == 0x19:
            inst = ALOAD()
            inst.index = ctypes.c_uint(bytecodeReader.read_uint16())
            self.modifiedInstruction = inst
        elif opcode == 0x36:
            inst = ISTORE()
            inst.index = ctypes.c_uint(bytecodeReader.read_uint16())
            self.modifiedInstruction = inst
        elif opcode == 0x37:
            inst = LSTORE()
            inst.index = ctypes.c_uint(bytecodeReader.read_uint16())
            self.modifiedInstruction = inst
        elif opcode == 0x38:
            inst = FSTORE()
            inst.index = ctypes.c_uint(bytecodeReader.read_uint16())
            self.modifiedInstruction = inst
        elif opcode == 0x39:
            inst = DSTORE()
            inst.index = ctypes.c_uint(bytecodeReader.read_uint16())
            self.modifiedInstruction = inst
        elif opcode == 0x3a:
            inst = ASTORE()
            inst.index = ctypes.c_uint(bytecodeReader.read_uint16())
            self.modifiedInstruction = inst
        elif opcode == 0x84:
            inst = IINC()
            inst.index = ctypes.c_uint(bytecodeReader.read_uint16())
            inst.const = ctypes.c_int32(bytecodeReader.read_int16())
            self.modifiedInstruction = inst
        elif opcode == 0xa9:
            raise RuntimeError("Unsupported opcode: 0xa9!")

    def execute(self, frame):
        self.modifiedInstruction.execute(frame)
