from ch08.instructions.base.Instruction import NoOperandsInstruction
from ch08.instructions.base.BranchLogic import BranchLogic
import ctypes

class GOTO_W(NoOperandsInstruction):
    def __init__(self):
        self.offset = 0

    def fetchOperands(self, bytecodeReader):
        self.offset = ctypes.c_int(bytecodeReader.read_int32())

    def execute(self, frame):
        BranchLogic.branch(frame, self.offset)

