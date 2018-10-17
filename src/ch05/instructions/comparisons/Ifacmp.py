from ch05.instructions.base.Instruction import BranchInstruction
from ch05.instructions.base.BranchLogic import BranchLogic

def _acmpPop(frame):
    stack = frame.operandStack
    val2 = stack.popRef()
    val1 = stack.popRef()
    return val1, val2

class IF_ACMPEQ(BranchInstruction):
    def execute(self, frame):
        val1, val2 = _acmpPop(frame)
        if val1 == val2:
            BranchLogic.branch(frame, self.offset)

class IF_ACMPNE(BranchInstruction):
    def execute(self, frame):
        val1, val2 = _acmpPop(frame)
        if val1 != val2:
            BranchLogic.branch(frame, self.offset)
