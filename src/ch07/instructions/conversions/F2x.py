from ch07.instructions.base.Instruction import NoOperandsInstruction
import ctypes

class F2D(NoOperandsInstruction):
    def execute(self, frame):
        stack = frame.operandStack
        f = stack.pop_numeric()
        d = float(f)
        stack.push_numeric(f)


class F2I(NoOperandsInstruction):
    def execute(self, frame):
        stack = frame.operandStack
        f = stack.pop_numeric()
        i = ctypes.c_int32(f)
        stack.push_numeric(i)

class F2L(NoOperandsInstruction):
    def execute(self, frame):
        stack = frame.operandStack
        f = stack.pop_numeric()
        l = ctypes.c_int64(f)
        stack.push_numeric(l)