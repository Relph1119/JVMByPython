from ch08.instructions.base.Instruction import NoOperandsInstruction

def _fcmp(frame, gFlag):
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

class FCMPG(NoOperandsInstruction):
    def execute(self, frame):
        _fcmp(frame, True)

class FCMPL(NoOperandsInstruction):
    def execute(self, frame):
        _fcmp(frame, False)