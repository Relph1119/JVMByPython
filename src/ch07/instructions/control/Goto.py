from ch07.instructions.base.Instruction import BranchInstruction
from ch07.instructions.base.BranchLogic import BranchLogic

class GOTO(BranchInstruction):
    def execute(self, frame):
        BranchLogic.branch(frame, self.offset)

