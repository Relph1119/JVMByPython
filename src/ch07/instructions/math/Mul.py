from ch07.instructions.base.Instruction import NoOperandsInstruction

def _mul(frame):
    stack = frame.operandStack
    v1 = stack.popNumeric()
    v2 = stack.popNumeric()
    result = v1 * v2
    stack.pushNumeric(result)

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