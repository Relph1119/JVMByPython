from ch06.instructions.base.Instruction import NoOperandsInstruction

def _dcmp(frame, gFlag):
    stack = frame.operandStack
    v2 = stack.popNumeric()
    v1 = stack.popNumeric()
    if v1 > v2:
        stack.pushNumeric(1)
    elif v1 == v2:
        stack.pushNumeric(0)
    elif v1 < v2:
        stack.pushNumeric(-1)
    elif gFlag:
        stack.pushNumeric(1)
    else:
        stack.pushNumeric(-1)

class DCMPG(NoOperandsInstruction):
    def execute(self, frame):
        _dcmp(frame, True)

class DCMPL(NoOperandsInstruction):
    def execute(self, frame):
        _dcmp(frame, False)