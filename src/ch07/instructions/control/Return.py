from ch07.instructions.base.Instruction import NoOperandsInstruction

def _numericReturn(frame):
    thread = frame.thread
    currentFrame = thread.pop_frame()
    invokerFrame = thread.topFrame()
    val = currentFrame.operandStack.pop_numeric()
    invokerFrame.operandStack.push_numeric(val)

class RETURN(NoOperandsInstruction):
    def execute(self, frame):
        frame.thread.pop_frame()

class ARETURN(NoOperandsInstruction):
    def execute(self, frame):
        thread = frame.thread
        currentFrame = thread.pop_frame()
        invokerFrame = thread.topFrame()
        ref = currentFrame.operandStack.pop_ref()
        invokerFrame.operandStack.push_ref(ref)

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
