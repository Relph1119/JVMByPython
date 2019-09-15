from ch06.instructions.base.Instruction import NoOperandsInstruction

def _sub(frame):
    stack = frame.operandStack
    v1 = stack.pop_numeric()
    v2 = stack.pop_numeric()
    result = v1 - v2
    stack.push_numeric(result)

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