from ch05.instructions.base.Instruction import Index8Instruction, NoOperandsInstruction

def _lload(frame, index):
    val = frame.localVars.getNumeric(index)
    frame.operandStack.pushNumeric(val)

class LLOAD(Index8Instruction):
    def execute(self, frame):
        _lload(frame, self.index)

class LLOAD_0(NoOperandsInstruction):
    def execute(self, frame):
        _lload(frame, 0)

class LLOAD_1(NoOperandsInstruction):
    def execute(self, frame):
        _lload(frame, 1)

class LLOAD_2(NoOperandsInstruction):
    def execute(self, frame):
        _lload(frame, 2)

class LLOAD_3(NoOperandsInstruction):
    def execute(self, frame):
        _lload(frame, 3)