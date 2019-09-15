from ch08.instructions.base.Instruction import NoOperandsInstruction

def _xor(frame):
    stack = frame.operandStack
    v2 = stack.pop_numeric()
    v1 = stack.pop_numeric()
    result = v1 ^ v2
    stack.push_numeric(result)

class IXOR(NoOperandsInstruction):
    def execute(self, frame):
        _xor(frame)

class LXOR(NoOperandsInstruction):
    def execute(self, frame):
        _xor(frame)