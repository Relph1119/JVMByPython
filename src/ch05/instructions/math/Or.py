from ch05.instructions.base.Instruction import NoOperandsInstruction

def _or(frame):
    stack = frame.operandStack
    v2 = stack.pop_numeric()
    v1 = stack.pop_numeric()
    result = v1 | v2
    stack.push_numeric(result)

class IOR(NoOperandsInstruction):
    def execute(self, frame):
        _or(frame)

class LOR(NoOperandsInstruction):
    def execute(self, frame):
        _or(frame)