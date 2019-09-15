from ch07.instructions.base.Instruction import NoOperandsInstruction
from ch07.instructions.base.BranchLogic import BranchLogic
import ctypes

class LOOKUP_SWITCH(NoOperandsInstruction):
    def __init__(self):
        self.defaultOffset = 0
        self.npairs = 0
        self.matchOffsets = []

    def fetchOperands(self, bytecodeReader):
        bytecodeReader.skipPadding()
        self.defaultOffset = bytecodeReader.readInt32()
        self.npairs = bytecodeReader.readInt32()
        self.matchOffsets = bytecodeReader.readInt32s(self.npairs * 2)

    def execute(self, frame):
        key = frame.operandStack.pop_numeric()
        for i in range(0, self.npairs * 2, 2):
            if self.matchOffsets[i] == key:
                offset = self.matchOffsets[i+1]
                BranchLogic.branch(frame, ctypes.c_int(offset))
                return
        BranchLogic.branch(frame, ctypes.c_int(self.defaultOffset))
