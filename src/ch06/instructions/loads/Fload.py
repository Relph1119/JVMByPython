from ch06.instructions.base.Instruction import Index8Instruction, NoOperandsInstruction

def _fload(frame, index):
    val = frame.localVars.getNumeric(index)
    frame.operandStack.pushNumeric(val)

class FLOAD(Index8Instruction):
    def execute(self, frame):
        _fload(frame, self.index)

class FLOAD_0(NoOperandsInstruction):
    def execute(self, frame):
        _fload(frame, 0)

class FLOAD_1(NoOperandsInstruction):
    def execute(self, frame):
        _fload(frame, 1)

class FLOAD_2(NoOperandsInstruction):
    def execute(self, frame):
        _fload(frame, 2)

class FLOAD_3(NoOperandsInstruction):
    def execute(self, frame):
        _fload(frame, 3)