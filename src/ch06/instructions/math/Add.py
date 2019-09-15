from ch06.instructions.base.Instruction import NoOperandsInstruction

def _add(frame):
    stack = frame.operandStack
    v1 = stack.pop_numeric()
    v2 = stack.pop_numeric()
    result = v1 + v2
    stack.push_numeric(result)

class DADD(NoOperandsInstruction):
    def execute(self, frame):
        _add(frame)

class FADD(NoOperandsInstruction):
    def execute(self, frame):
        _add(frame)

class IADD(NoOperandsInstruction):
    def execute(self, frame):
        _add(frame)

class LADD(NoOperandsInstruction):
    def execute(self, frame):
        _add(frame)