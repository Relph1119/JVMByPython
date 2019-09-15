from ch08.instructions.base.Instruction import BranchInstruction
from ch08.instructions.base.BranchLogic import BranchLogic

class IFNULL(BranchInstruction):
    def execute(self, frame):
        ref = frame.operandStack.pop_ref()
        if not ref:
            BranchLogic.branch(frame, self.offset)

class IFNONNULL(BranchInstruction):
    def execute(self, frame):
        ref = frame.operandStack.pop_ref()
        if ref:
            BranchLogic.branch(frame, self.offset)