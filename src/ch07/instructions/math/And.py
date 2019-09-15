from ch07.instructions.base.Instruction import NoOperandsInstruction

def _and(frame):
    stack = frame.operandStack
    v2 = stack.pop_numeric()
    v1 = stack.pop_numeric()
    result = v1 & v2
    stack.push_numeric(result)

class IAND(NoOperandsInstruction):
    def execute(self, frame):
        _and(frame)

class LAND(NoOperandsInstruction):
    def execute(self, frame):
        _and(frame)