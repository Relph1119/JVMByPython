from ch07.instructions.base.Instruction import NoOperandsInstruction

class LCMP(NoOperandsInstruction):
    def execute(self, frame):
        stack = frame.operandStack
        v2 = stack.popNumeric()
        v1 = stack.popNumeric()
        if v1 > v2:
            stack.pushNumeric(1)
        elif v1 == v2:
            stack.pushNumeric(0)
        else:
            stack.pushNumeric(-1)