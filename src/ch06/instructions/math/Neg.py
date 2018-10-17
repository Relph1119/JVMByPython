from ch06.instructions.base.Instruction import NoOperandsInstruction

def _neg(frame):
    stack = frame.operandStack
    val = stack.popNumeric()
    stack.pushNumeric(-val)

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

