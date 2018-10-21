from ch08.instructions.base.Instruction import NoOperandsInstruction
import ctypes

class IINC(NoOperandsInstruction):
    def __init__(self):
        self.index = 0
        self.const = 0

    def fetchOperands(self, bytecodeReader):
        self.index = ctypes.c_uint(bytecodeReader.readUint8()).value
        self.const = ctypes.c_int32(bytecodeReader.readInt8()).value

    def execute(self, frame):
        localVars = frame.localVars
        val = localVars.getNumeric(self.index)
        val += self.const
        localVars.setNumeric(self.index, val)