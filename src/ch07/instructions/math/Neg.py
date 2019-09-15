from ch07.instructions.base.Instruction import NoOperandsInstruction

def _neg(frame):
    stack = frame.operandStack
    val = stack.pop_numeric()
    stack.push_numeric(-val)

class DNEG(NoOperandsInstruction):
    def execute(self, frame):
        _neg(frame)

class FNEG(NoOperandsInstruction):
    def execute(self, frame):
        _neg(frame)

class INEG(NoOperandsInstruction):
    def execute(self, frame):
        _neg(frame)

class LNEG(NoOperandsInstruction):
    def execute(self, frame):
        _neg(frame)

