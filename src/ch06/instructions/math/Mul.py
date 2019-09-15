from ch06.instructions.base.Instruction import NoOperandsInstruction

def _mul(frame):
    stack = frame.operandStack
    v1 = stack.pop_numeric()
    v2 = stack.pop_numeric()
    result = v1 * v2
    stack.push_numeric(result)

class DMUL(NoOperandsInstruction):
    def execute(self, frame):
        _mul(frame)

class FMUL(NoOperandsInstruction):
    def execute(self, frame):
        _mul(frame)

class IMUL(NoOperandsInstruction):
    def execute(self, frame):
        _mul(frame)

class LMUL(NoOperandsInstruction):
    def execute(self, frame):
        _mul(frame)