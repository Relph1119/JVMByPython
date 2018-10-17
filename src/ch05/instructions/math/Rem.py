from ch05.instructions.base.Instruction import NoOperandsInstruction
import math

class DREM(NoOperandsInstruction):
    def execute(self, frame):
        stack = frame.operandStack()
        v2 = stack.popNumeric()
        v1 = stack.popNumeric()
        if v2 == 0.0:
            result = math.nan
        else:
            result = math.fmod(v1, v2)
        stack.pushNumeric(result)

class FREM(NoOperandsInstruction):
    def execute(self, frame):
        stack = frame.operandStack()
        v2 = stack.popNumeric()
        v1 = stack.popNumeric()
        if v2 == 0.0:
            result = math.nan
        else:
            result = math.fmod(v1, v2)
        stack.pushNumeric(result)

class IREM(NoOperandsInstruction):
    def execute(self, frame):
        stack = frame.operandStack()
        v2 = stack.popNumeric()
        v1 = stack.popNumeric()
        if v2 == 0:
            raise RuntimeError("java.lang.ArithmeticException: / by zero")
        result = v1 % v2
        stack.pushNumeric(result)

class LREM(NoOperandsInstruction):
    def execute(self, frame):
        stack = frame.operandStack()
        v2 = stack.popNumeric()
        v1 = stack.popNumeric()
        if v2 == 0:
            raise RuntimeError("java.lang.ArithmeticException: / by zero")
        result = v1 % v2
        stack.pushNumeric(result)
