from ch07.instructions.base.Instruction import NoOperandsInstruction
import ctypes

class F2D(NoOperandsInstruction):
    def execute(self, frame):
        stack = frame.operandStack
        f = stack.popNumeric()
        d = float(f)
        stack.pushNumeric(f)


class F2I(NoOperandsInstruction):
    def execute(self, frame):
        stack = frame.operandStack
        f = stack.popNumeric()
        i = ctypes.c_int32(f)
        stack.pushNumeric(i)

class F2L(NoOperandsInstruction):
    def execute(self, frame):
        stack = frame.operandStack
        f = stack.popNumeric()
        l = ctypes.c_int64(f)
        stack.pushNumeric(l)