from ch05.instructions.base.Instruction import NoOperandsInstruction
import ctypes

class L2D(NoOperandsInstruction):
    def execute(self, frame):
        stack = frame.operandStack
        l = stack.pop_numeric()
        d = float(l)
        stack.push_numeric(d)

class L2F(NoOperandsInstruction):
    def execute(self, frame):
        stack = frame.operandStack
        l = stack.pop_numeric()
        f = float(l)
        stack.push_numeric(f)

class L2I(NoOperandsInstruction):
    def execute(self, frame):
        stack = frame.operandStack
        l = stack.pop_numeric()
        i = ctypes.c_int32(l).value
        stack.push_numeric(i)