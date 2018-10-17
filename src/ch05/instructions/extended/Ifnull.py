from ch05.instructions.base.Instruction import BranchInstruction
from ch05.instructions.base.BranchLogic import BranchLogic

class IFNULL(BranchInstruction):
    def execute(self, frame):
        ref = frame.operandStack.popRef()
        if not ref:
            BranchLogic.branch(frame, self.offset)

class IFNONNULL(BranchInstruction):
    def execute(self, frame):
        ref = frame.operandStack.popRef()
        if ref:
            BranchLogic.branch(frame, self.offset)