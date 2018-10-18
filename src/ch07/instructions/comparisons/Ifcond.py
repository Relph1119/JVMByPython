from ch07.instructions.base.Instruction import BranchInstruction
from ch07.instructions.base.BranchLogic import BranchLogic

class IFEQ(BranchInstruction):
    def execute(self, frame):
        val = frame.operandStack.popNumeric()
        if val == 0:
            BranchLogic.branch(frame, self.offset)

class IFNE(BranchInstruction):
    def execute(self, frame):
        val = frame.operandStack.popNumeric()
        if val != 0:
            BranchLogic.branch(frame, self.offset)

class IFLT(BranchInstruction):
    def execute(self, frame):
        val = frame.operandStack.popNumeric()
        if val < 0:
            BranchLogic.branch(frame, self.offset)

class IFLE(BranchInstruction):
    def execute(self, frame):
        val = frame.operandStack.popNumeric()
        if val <= 0:
            BranchLogic.branch(frame, self.offset)

class IFGT(BranchInstruction):
    def execute(self, frame):
        val = frame.operandStack.popNumeric()
        if val > 0:
            BranchLogic.branch(frame, self.offset)

class IFGE(BranchInstruction):
    def execute(self, frame):
        val = frame.operandStack.popNumeric()
        if val >= 0:
            BranchLogic.branch(frame, self.offset)