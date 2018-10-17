from ch06.instructions.base.Instruction import NoOperandsInstruction
import ctypes

class L2D(NoOperandsInstruction):
    def execute(self, frame):
        stack = frame.operandStack
        l = stack.popNumeric()
        d = float(l)
        stack.pushNumeric(d)

class L2F(NoOperandsInstruction):
    def execute(self, frame):
        stack = frame.operandStack
        l = stack.popNumeric()
        f = float(l)
        stack.pushNumeric(f)

class L2I(NoOperandsInstruction):
    def execute(self, frame):
        stack = frame.operandStack
        l = stack.popNumeric()
        i = ctypes.c_int32(l).value
        stack.pushNumeric(i)