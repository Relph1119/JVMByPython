from ch08.instructions.base.Instruction import NoOperandsInstruction
import ctypes

class I2B(NoOperandsInstruction):
    def execute(self, frame):
        stack = frame.operandStack
        i = stack.popNumeric()
        b = ctypes.c_int8(i).value
        stack.pushNumeric(b)

class I2C(NoOperandsInstruction):
    def execute(self, frame):
        stack = frame.operandStack
        i = stack.popNumeric()
        c = ctypes.c_int16(i).value
        stack.pushNumeric(c)

class I2S(NoOperandsInstruction):
    def execute(self, frame):
        stack = frame.operandStack
        i = stack.popNumeric()
        s = ctypes.c_int16(i).value
        stack.pushNumeric(s)

class I2D(NoOperandsInstruction):
    def execute(self, frame):
        stack = frame.operandStack
        i = stack.popNumeric()
        d = float(i)
        stack.pushNumeric(d)

class I2F(NoOperandsInstruction):
    def execute(self, frame):
        stack = frame.operandStack
        i = stack.popNumeric()
        f = float(i)
        stack.pushNumeric(f)

class I2L(NoOperandsInstruction):
    def execute(self, frame):
        stack = frame.operandStack
        i = stack.popNumeric()
        l = ctypes.c_int64(i).value
        stack.pushNumeric(l)