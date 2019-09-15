from ch06.instructions.base.Instruction import Index8Instruction, NoOperandsInstruction

def _dstore(frame, index):
    val = frame.operandStack.pop_numeric()
    frame.localVars.set_numeric(index, val)


class DSTORE(Index8Instruction):
    def execute(self, frame):
        _dstore(frame, self.index)

class DSTORE_0(NoOperandsInstruction):
    def execute(self, frame):
        _dstore(frame, 0)

class DSTORE_1(NoOperandsInstruction):
    def execute(self, frame):
        _dstore(frame, 1)

class DSTORE_2(NoOperandsInstruction):
    def execute(self, frame):
        _dstore(frame, 2)

class DSTORE_3(NoOperandsInstruction):
    def execute(self, frame):
        _dstore(frame, 3)