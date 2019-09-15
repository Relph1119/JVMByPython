from ch05.instructions.base.Instruction import NoOperandsInstruction

class LCMP(NoOperandsInstruction):
    def execute(self, frame):
        stack = frame.operandStack
        v2 = stack.pop_numeric()
        v1 = stack.pop_numeric()
        if v1 > v2:
            stack.push_numeric(1)
        elif v1 == v2:
            stack.push_numeric(0)
        else:
            stack.push_numeric(-1)