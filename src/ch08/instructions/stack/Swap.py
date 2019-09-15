from ch08.instructions.base.Instruction import NoOperandsInstruction

class SWAP(NoOperandsInstruction):
    def execute(self, frame):
        stack = frame.operandStack()
        slot1 = stack.pop_slot()
        slot2 = stack.pop_slot()
        stack.push_slot(slot1)
        stack.push_slot(slot2)