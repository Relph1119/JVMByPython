from abc import ABCMeta, abstractstaticmethod

class Instruction(metaclass=ABCMeta):

    @abstractstaticmethod
    def fetchOperands(self, bytecodeReader):
        pass

    @abstractstaticmethod
    def execute(self, frame):
        pass

class NoOperandsInstruction(Instruction):
    def fetchOperands(self, bytecodeReader):
        pass

    def execute(self, frame):
        pass

class BranchInstruction(Instruction):
    def __init__(self):
        self.offset = 0

    def fetchOperands(self, bytecodeReader):
        self.offset = bytecodeReader.read_int16()

    @abstractstaticmethod
    def execute(self, frame):
        pass

class Index8Instruction(Instruction):
    def __init__(self):
        self.index = 0

    def fetchOperands(self, bytecodeReader):
        self.index = bytecodeReader.read_uint8()

    @abstractstaticmethod
    def execute(self, frame):
        pass

class Index16Instruction(Instruction):
    def __init__(self):
        self.index = 0

    def fetchOperands(self, bytecodeReader):
        self.index = bytecodeReader.read_uint16()

    @abstractstaticmethod
    def execute(self, frame):
        pass

