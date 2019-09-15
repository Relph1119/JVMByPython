from ch06.instructions.base.Instruction import NoOperandsInstruction
import copy

class DUP(NoOperandsInstruction):
    def execute(self, frame):
        stack = frame.operandStack
        slot = stack.pop_slot()
        stack.push_slot(slot)
        stack.push_slot(copy.deepcopy(slot))

class DUP_X1(NoOperandsInstruction):
    def execute(self, frame):
        stack = frame.operandStack
        slot1 = stack.pop_slot()
        slot2 = stack.pop_slot()
        stack.push_slot(slot1)
        stack.push_slot(slot2)
        stack.push_slot(copy.deepcopy(slot1))

class DUP_X2(NoOperandsInstruction):
    def execute(self, frame):
        stack = frame.operandStack
        slot1 = stack.pop_slot()
        slot2 = stack.pop_slot()
        slot3 = stack.pop_slot()
        stack.push_slot(slot1)
        stack.push_slot(slot3)
        stack.push_slot(slot2)
        stack.push_slot(copy.deepcopy(slot1))

class DUP2(NoOperandsInstruction):
    def execute(self, frame):
        stack = frame.operandStack()
        slot1 = stack.pop_slot()
        slot2 = stack.pop_slot()
        stack.push_slot(slot2)
        stack.push_slot(slot1)
        stack.push_slot(copy.deepcopy(slot2))
        stack.push_slot(copy.deepcopy(slot1))

class DUP2_X1(NoOperandsInstruction):
    def execute(self, frame):
        stack = frame.operandStack()
        slot1 = stack.pop_slot()
        slot2 = stack.pop_slot()
        slot3 = stack.pop_slot()
        stack.push_slot(slot2)
        stack.push_slot(slot1)
        stack.push_slot(slot3)
        stack.push_slot(copy.deepcopy(slot2))
        stack.push_slot(copy.deepcopy(slot1))

class DUP2_X2(NoOperandsInstruction):
    def execute(self, frame):
        stack = frame.operandStack()
        slot1 = stack.pop_slot()
        slot2 = stack.pop_slot()
        slot3 = stack.pop_slot()
        slot4 = stack.pop_slot()
        stack.push_slot(slot2)
        stack.push_slot(slot1)
        stack.push_slot(slot4)
        stack.push_slot(slot3)
        stack.push_slot(copy.deepcopy(slot2))
        stack.push_slot(copy.deepcopy(slot1))
