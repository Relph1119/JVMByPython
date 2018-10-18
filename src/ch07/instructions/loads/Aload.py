from ch07.instructions.base.Instruction import Index8Instruction, NoOperandsInstruction

def _aload(frame, index):
    ref = frame.localVars.getRef(index)
    frame.operandStack.pushRef(ref)

class ALOAD(Index8Instruction):
    def execute(self, frame):
        _aload(frame, self.index)

class ALOAD_0(NoOperandsInstruction):
    def execute(self, frame):
        _aload(frame, 0)

class ALOAD_1(NoOperandsInstruction):
    def execute(self, frame):
        _aload(frame, 1)

class ALOAD_2(NoOperandsInstruction):
    def execute(self, frame):
        _aload(frame, 2)

class ALOAD_3(NoOperandsInstruction):
    def execute(self, frame):
        _aload(frame, 3)