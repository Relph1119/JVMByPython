from ch06.instructions.base.Instruction import Index8Instruction, NoOperandsInstruction

def _dload(frame, index):
    val = frame.localVars.getNumeric(index)
    frame.operandStack.pushNumeric(val)

class DLOAD(Index8Instruction):
    def execute(self, frame):
        _dload(frame, self.index)

class DLOAD_0(NoOperandsInstruction):
    def execute(self, frame):
        _dload(frame, 0)

class DLOAD_1(NoOperandsInstruction):
    def execute(self, frame):
        _dload(frame, 1)

class DLOAD_2(NoOperandsInstruction):
    def execute(self, frame):
        _dload(frame, 2)

class DLOAD_3(NoOperandsInstruction):
    def execute(self, frame):
        _dload(frame, 3)