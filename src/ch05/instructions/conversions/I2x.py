from ch05.instructions.base.Instruction import NoOperandsInstruction
import ctypes

class I2B(NoOperandsInstruction):
    def execute(self, frame):
        stack = frame.operandStack
        i = stack.pop_numeric()
        b = ctypes.c_int8(i).value
        stack.push_numeric(b)

class I2C(NoOperandsInstruction):
    def execute(self, frame):
        stack = frame.operandStack
        i = stack.pop_numeric()
        c = ctypes.c_int16(i).value
        stack.push_numeric(c)

class I2S(NoOperandsInstruction):
    def execute(self, frame):
        stack = frame.operandStack
        i = stack.pop_numeric()
        s = ctypes.c_int16(i).value
        stack.push_numeric(s)

class I2D(NoOperandsInstruction):
    def execute(self, frame):
        stack = frame.operandStack
        i = stack.pop_numeric()
        d = float(i)
        stack.push_numeric(d)

class I2F(NoOperandsInstruction):
    def execute(self, frame):
        stack = frame.operandStack
        i = stack.pop_numeric()
        f = float(i)
        stack.push_numeric(f)

class I2L(NoOperandsInstruction):
    def execute(self, frame):
        stack = frame.operandStack
        i = stack.pop_numeric()
        l = ctypes.c_int64(i).value
        stack.push_numeric(l)