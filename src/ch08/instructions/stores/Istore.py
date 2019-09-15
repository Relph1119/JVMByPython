from ch08.instructions.base.Instruction import NoOperandsInstruction, Index8Instruction

def _istore(frame, index):
    val = frame.operandStack.pop_numeric()
    frame.localVars.set_numeric(index, val)

class ISTORE(Index8Instruction):
    def execute(self, frame):
        _istore(frame, self.index)

class ISTORE_0(NoOperandsInstruction):
    def execute(self, frame):
        _istore(frame, 0)

class ISTORE_1(NoOperandsInstruction):
    def execute(self, frame):
        _istore(frame, 1)

class ISTORE_2(NoOperandsInstruction):
    def execute(self, frame):
        _istore(frame, 2)

class ISTORE_3(NoOperandsInstruction):
    def execute(self, frame):
        _istore(frame, 3)