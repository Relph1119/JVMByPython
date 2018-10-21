from ch08.instructions.base.Instruction import NoOperandsInstruction

def _xor(frame):
    stack = frame.operandStack
    v2 = stack.popNumeric()
    v1 = stack.popNumeric()
    result = v1 ^ v2
    stack.pushNumeric(result)

class IXOR(NoOperandsInstruction):
    def execute(self, frame):
        _xor(frame)

class LXOR(NoOperandsInstruction):
    def execute(self, frame):
        _xor(frame)