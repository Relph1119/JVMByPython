from ch07.instructions.base.Instruction import NoOperandsInstruction
import ctypes

class ISHL(NoOperandsInstruction):
    def execute(self, frame):
        stack = frame.operandStack()
        v2 = stack.pop_numeric()
        v1 = stack.pop_numeric()
        s = v2 & 0x1f
        result = v1 << s
        stack.push_numeric(result)

class ISHR(NoOperandsInstruction):
    def execute(self, frame):
        stack = frame.operandStack()
        v2 = stack.pop_numeric()
        v1 = stack.pop_numeric()
        s = v2 & 0x1f
        result = v1 >> s
        stack.push_numeric(result)

class IUSHR(NoOperandsInstruction):
    def execute(self, frame):
        stack = frame.operandStack()
        v2 = stack.pop_numeric()
        v1 = stack.pop_numeric()
        s = v2 & 0x1f
        result = ctypes.c_uint32(v1).value >> s
        stack.push_numeric(result)

class LSHL(NoOperandsInstruction):
    def execute(self, frame):
        stack = frame.operandStack()
        v2 = stack.pop_numeric()
        v1 = stack.pop_numeric()
        s = v2 & 0x3f
        result = v1 << s
        stack.push_numeric(result)

class LSHR(NoOperandsInstruction):
    def execute(self, frame):
        stack = frame.operandStack()
        v2 = stack.pop_numeric()
        v1 = stack.pop_numeric()
        s = v2 & 0x3f
        result = v1 >> s
        stack.push_numeric(result)

class LUSHR(NoOperandsInstruction):
    def execute(self, frame):
        stack = frame.operandStack()
        v2 = stack.pop_numeric()
        v1 = stack.pop_numeric()
        s = v2 & 0x3f
        result = ctypes.c_uint32(v1).value >> s
        stack.push_numeric(result)

