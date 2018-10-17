from ch06.instructions.base.Instruction import NoOperandsInstruction
import ctypes

class ISHL(NoOperandsInstruction):
    def execute(self, frame):
        stack = frame.operandStack()
        v2 = stack.popNumeric()
        v1 = stack.popNumeric()
        s = v2 & 0x1f
        result = v1 << s
        stack.pushNumeric(result)

class ISHR(NoOperandsInstruction):
    def execute(self, frame):
        stack = frame.operandStack()
        v2 = stack.popNumeric()
        v1 = stack.popNumeric()
        s = v2 & 0x1f
        result = v1 >> s
        stack.pushNumeric(result)

class IUSHR(NoOperandsInstruction):
    def execute(self, frame):
        stack = frame.operandStack()
        v2 = stack.popNumeric()
        v1 = stack.popNumeric()
        s = v2 & 0x1f
        result = ctypes.c_uint32(v1).value >> s
        stack.pushNumeric(result)

class LSHL(NoOperandsInstruction):
    def execute(self, frame):
        stack = frame.operandStack()
        v2 = stack.popNumeric()
        v1 = stack.popNumeric()
        s = v2 & 0x3f
        result = v1 << s
        stack.pushNumeric(result)

class LSHR(NoOperandsInstruction):
    def execute(self, frame):
        stack = frame.operandStack()
        v2 = stack.popNumeric()
        v1 = stack.popNumeric()
        s = v2 & 0x3f
        result = v1 >> s
        stack.pushNumeric(result)

class LUSHR(NoOperandsInstruction):
    def execute(self, frame):
        stack = frame.operandStack()
        v2 = stack.popNumeric()
        v1 = stack.popNumeric()
        s = v2 & 0x3f
        result = ctypes.c_uint32(v1).value >> s
        stack.pushNumeric(result)

