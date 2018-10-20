from ch07.instructions.base.Instruction import NoOperandsInstruction

def _numericReturn(frame):
    thread = frame.thread
    currentFrame = thread.popFrame()
    invokerFrame = thread.topFrame()
    val = currentFrame.operandStack.popNumeric()
    invokerFrame.operandStack.pushNumeric(val)

class RETURN(NoOperandsInstruction):
    def execute(self, frame):
        frame.thread.popFrame()

class ARETURN(NoOperandsInstruction):
    def execute(self, frame):
        thread = frame.thread
        currentFrame = thread.popFrame()
        invokerFrame = thread.topFrame()
        ref = currentFrame.operandStack.popRef()
        invokerFrame.operandStack.pushRef(ref)

class DRETURN(NoOperandsInstruction):
    def execute(self, frame):
        _numericReturn(frame)

class FRETURN(NoOperandsInstruction):
    def execute(self, frame):
        _numericReturn(frame)

class IRETURN(NoOperandsInstruction):
    def execute(self, frame):
        _numericReturn(frame)

class LRETURN(NoOperandsInstruction):
    def execute(self, frame):
        _numericReturn(frame)
