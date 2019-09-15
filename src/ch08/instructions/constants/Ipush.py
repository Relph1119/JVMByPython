from ch08.instructions.base.Instruction import Instruction

class BIPUSH(Instruction):
    def __init__(self):
        self.val = 0

    def fetchOperands(self, bytecodeReader):
        self.val = bytecodeReader.read_int8()

    def execute(self, frame):
        i = self.val
        frame.operandStack.push_numeric(i)

class SIPUSH(Instruction):
    def __init__(self):
        self.val = 0

    def fetchOperands(self, bytecodeReader):
        self.val = bytecodeReader.read_int16()

    def execute(self, frame):
        i = self.val
        frame.operandStack.push_numeric(i)