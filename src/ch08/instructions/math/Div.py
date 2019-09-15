from ch08.instructions.base.Instruction import NoOperandsInstruction
import math

class DDIV(NoOperandsInstruction):
    def execute(self, frame):
        stack = frame.operandStack
        v1 = stack.pop_numeric()
        v2 = stack.pop_numeric()
        if v2 == 0.0:
            result = math.inf
        else:
            result = v1 / v2
        stack.push_numeric(result)

class FDIV(NoOperandsInstruction):
    def execute(self, frame):
        stack = frame.operandStack
        v1 = stack.pop_numeric()
        v2 = stack.pop_numeric()
        if v2 == 0.0:
            result = math.inf
        else:
            result = v1 / v2
        stack.push_numeric(result)

class IDIV(NoOperandsInstruction):
    def execute(self, frame):
        stack = frame.operandStack
        v1 = stack.pop_numeric()
        v2 = stack.pop_numeric()
        if v2 == 0:
           raise RuntimeError("java.lang.ArithmeticException: / by zero")
        result = v1 / v2
        stack.push_numeric(result)

class LDIV(NoOperandsInstruction):
    def execute(self, frame):
        stack = frame.operandStack
        v1 = stack.pop_numeric()
        v2 = stack.pop_numeric()
        if v2 == 0:
            raise RuntimeError("java.lang.ArithmeticException: / by zero")
        result = v1 / v2
        stack.push_numeric(result)