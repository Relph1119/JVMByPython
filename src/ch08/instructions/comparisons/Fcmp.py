from ch08.instructions.base.Instruction import NoOperandsInstruction

def _fcmp(frame, gFlag):
    stack = frame.operandStack
    v2 = stack.pop_numeric()
    v1 = stack.pop_numeric()
    if v1 > v2:
        stack.push_numeric(1)
    elif v1 == v2:
        stack.push_numeric(0)
    elif v1 < v2:
        stack.push_numeric(-1)
    elif gFlag:
        stack.push_numeric(1)
    else:
        stack.push_numeric(-1)

class FCMPG(NoOperandsInstruction):
    def execute(self, frame):
        _fcmp(frame, True)

class FCMPL(NoOperandsInstruction):
    def execute(self, frame):
        _fcmp(frame, False)