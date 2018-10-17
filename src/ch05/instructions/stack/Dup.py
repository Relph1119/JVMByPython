from ch05.instructions.base.Instruction import NoOperandsInstruction

class DUP(NoOperandsInstruction):
    def execute(self, frame):
        stack = frame.operandStack
        slot = stack.popSlot()
        stack.pushSlot(slot)
        stack.pushSlot(slot)

class DUP_X1(NoOperandsInstruction):
    def execute(self, frame):
        stack = frame.operandStack
        slot1 = stack.popSlot()
        slot2 = stack.popSlot()
        stack.pushSlot(slot1)
        stack.pushSlot(slot2)
        stack.pushSlot(slot1)

class DUP_X2(NoOperandsInstruction):
    def execute(self, frame):
        stack = frame.operandStack
        slot1 = stack.popSlot()
        slot2 = stack.popSlot()
        slot3 = stack.popSlot()
        stack.pushSlot(slot1)
        stack.pushSlot(slot3)
        stack.pushSlot(slot2)
        stack.pushSlot(slot1)

class DUP2(NoOperandsInstruction):
    def execute(self, frame):
        stack = frame.operandStack()
        slot1 = stack.popSlot()
        slot2 = stack.popSlot()
        stack.pushSlot(slot2)
        stack.pushSlot(slot1)
        stack.pushSlot(slot2)
        stack.pushSlot(slot1)

class DUP2_X1(NoOperandsInstruction):
    def execute(self, frame):
        stack = frame.operandStack()
        slot1 = stack.popSlot()
        slot2 = stack.popSlot()
        slot3 = stack.popSlot()
        stack.pushSlot(slot2)
        stack.pushSlot(slot1)
        stack.pushSlot(slot3)
        stack.pushSlot(slot2)
        stack.pushSlot(slot1)

class DUP2_X2(NoOperandsInstruction):
    def execute(self, frame):
        stack = frame.operandStack()
        slot1 = stack.popSlot()
        slot2 = stack.popSlot()
        slot3 = stack.popSlot()
        slot4 = stack.popSlot()
        stack.pushSlot(slot2)
        stack.pushSlot(slot1)
        stack.pushSlot(slot4)
        stack.pushSlot(slot3)
        stack.pushSlot(slot2)
        stack.pushSlot(slot1)
