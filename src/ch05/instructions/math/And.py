from ch05.instructions.base.Instruction import NoOperandsInstruction

def _and(frame):
    stack = frame.operandStack
    v2 = stack.popNumeric()
    v1 = stack.popNumeric()
    result = v1 & v2
    stack.pushNumeric(result)

class IAND(NoOperandsInstruction):
    def execute(self, frame):
        _and(frame)

class LAND(NoOperandsInstruction):
    def execute(self, frame):
        _and(frame)