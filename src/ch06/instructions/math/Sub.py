from ch06.instructions.base.Instruction import NoOperandsInstruction

def _sub(frame):
    stack = frame.operandStack
    v1 = stack.popNumeric()
    v2 = stack.popNumeric()
    result = v1 - v2
    stack.pushNumeric(result)

class DSUB(NoOperandsInstruction):
    def execute(self, frame):
        _sub(frame)

class FSUB(NoOperandsInstruction):
    def execute(self, frame):
        _sub(frame)

class ISUB(NoOperandsInstruction):
    def execute(self, frame):
        _sub(frame)

class LSUB(NoOperandsInstruction):
    def execute(self, frame):
        _sub(frame)