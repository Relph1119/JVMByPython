from ch08.instructions.base.Instruction import NoOperandsInstruction
import ctypes

class IINC(NoOperandsInstruction):
    def __init__(self):
        self.index = 0
        self.const = 0

    def fetchOperands(self, bytecodeReader):
        self.index = ctypes.c_uint(bytecodeReader.read_uint8()).value
        self.const = ctypes.c_int32(bytecodeReader.read_int8()).value

    def execute(self, frame):
        localVars = frame.localVars
        val = localVars.get_numeric(self.index)
        val += self.const
        localVars.set_numeric(self.index, val)