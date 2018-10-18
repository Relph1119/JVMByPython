from ch07.instructions.base.Instruction import NoOperandsInstruction

def _or(frame):
    stack = frame.operandStack
    v2 = stack.popNumeric()
    v1 = stack.popNumeric()
    result = v1 | v2
    stack.pushNumeric(result)

class IOR(NoOperandsInstruction):
    def execute(self, frame):
        _or(frame)

class LOR(NoOperandsInstruction):
    def execute(self, frame):
        _or(frame)