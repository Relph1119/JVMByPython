from ch07.instructions.base.Instruction import Index16Instruction

class INVOKE_SPECIAL(Index16Instruction):
    def execute(self, frame):
        frame.operandStack.popRef()

    