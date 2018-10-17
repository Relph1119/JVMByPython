from ch06.instructions.base.Instruction import NoOperandsInstruction

class SWAP(NoOperandsInstruction):
    def execute(self, frame):
        stack = frame.operandStack()
        slot1 = stack.popSlot()
        slot2 = stack.popSlot()
        stack.pushSlot(slot1)
        stack.pushSlot(slot2)