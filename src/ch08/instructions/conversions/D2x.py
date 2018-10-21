from ch08.instructions.base.Instruction import NoOperandsInstruction
import ctypes

class D2F(NoOperandsInstruction):
    def execute(self, frame):
        stack = frame.operandStack
        d = stack.popNumeric()
        f = float(d)
        stack.pushNumeric(f)


class D2I(NoOperandsInstruction):
    def execute(self, frame):
        stack = frame.operandStack
        d = stack.popNumeric()
        i = ctypes.c_int32(d)
        stack.pushNumeric(i)

class D2L(NoOperandsInstruction):
    def execute(self, frame):
        stack = frame.operandStack
        d = stack.popNumeric()
        l = ctypes.c_int64(d)
        stack.pushNumeric(l)