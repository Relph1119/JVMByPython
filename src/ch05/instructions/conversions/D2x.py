from ch05.instructions.base.Instruction import NoOperandsInstruction
import ctypes

class D2F(NoOperandsInstruction):
    def execute(self, frame):
        stack = frame.operandStack
        d = stack.pop_numeric()
        f = float(d)
        stack.push_numeric(f)


class D2I(NoOperandsInstruction):
    def execute(self, frame):
        stack = frame.operandStack
        d = stack.pop_numeric()
        i = ctypes.c_int32(d)
        stack.push_numeric(i)

class D2L(NoOperandsInstruction):
    def execute(self, frame):
        stack = frame.operandStack
        d = stack.pop_numeric()
        l = ctypes.c_int64(d)
        stack.push_numeric(l)