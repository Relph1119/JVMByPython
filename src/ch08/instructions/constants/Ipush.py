from ch08.instructions.base.Instruction import Instruction

class BIPUSH(Instruction):
    def __init__(self):
        self.val = 0

    def fetchOperands(self, bytecodeReader):
        self.val = bytecodeReader.readInt8()

    def execute(self, frame):
        i = self.val
        frame.operandStack.push_numeric(i)

class SIPUSH(Instruction):
    def __init__(self):
        self.val = 0

    def fetchOperands(self, bytecodeReader):
        self.val = bytecodeReader.readInt16()

    def execute(self, frame):
        i = self.val
        frame.operandStack.push_numeric(i)