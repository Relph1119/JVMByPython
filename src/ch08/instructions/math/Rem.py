from ch08.instructions.base.Instruction import NoOperandsInstruction
import math

class DREM(NoOperandsInstruction):
    def execute(self, frame):
        stack = frame.operandStack()
        v2 = stack.pop_numeric()
        v1 = stack.pop_numeric()
        if v2 == 0.0:
            result = math.nan
        else:
            result = math.fmod(v1, v2)
        stack.push_numeric(result)

class FREM(NoOperandsInstruction):
    def execute(self, frame):
        stack = frame.operandStack()
        v2 = stack.pop_numeric()
        v1 = stack.pop_numeric()
        if v2 == 0.0:
            result = math.nan
        else:
            result = math.fmod(v1, v2)
        stack.push_numeric(result)

class IREM(NoOperandsInstruction):
    def execute(self, frame):
        stack = frame.operandStack()
        v2 = stack.pop_numeric()
        v1 = stack.pop_numeric()
        if v2 == 0:
            raise RuntimeError("java.lang.ArithmeticException: / by zero")
        result = v1 % v2
        stack.push_numeric(result)

class LREM(NoOperandsInstruction):
    def execute(self, frame):
        stack = frame.operandStack()
        v2 = stack.pop_numeric()
        v1 = stack.pop_numeric()
        if v2 == 0:
            raise RuntimeError("java.lang.ArithmeticException: / by zero")
        result = v1 % v2
        stack.push_numeric(result)
