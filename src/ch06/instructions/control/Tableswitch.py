from ch06.instructions.base.Instruction import NoOperandsInstruction
from ch06.instructions.base.BranchLogic import BranchLogic

class TABLE_SWITCH(NoOperandsInstruction):
    def __init__(self):
        self.defaultOffset = 0
        self.low = 0
        self.high = 0
        self.jumpOffsets = []

    def fetchOperands(self, bytecodeReader):
        bytecodeReader.skipPadding()
        self.defaultOffset = bytecodeReader.readInt32()
        self.low = bytecodeReader.readInt32()
        self.high = bytecodeReader.readInt32()
        jumpOffsetsCount = self.high - self.low + 1
        self.jumpOffsets = bytecodeReader.readInt32s(jumpOffsetsCount)

    def execute(self, frame):
        index = frame.operandStack.pop_numeric()

        if self.low <= index <= self.high:
            offset = self.jumpOffsets[index - self.low]
        else:
            offset = self.defaultOffset
        BranchLogic.branch(frame, offset)