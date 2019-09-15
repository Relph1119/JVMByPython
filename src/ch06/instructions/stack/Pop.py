from ch06.instructions.base.Instruction import NoOperandsInstruction

class POP(NoOperandsInstruction):
    def execute(self, frame):
        stack = frame.operandStack
        stack.pop_slot()

class POP2(NoOperandsInstruction):
    ##由于实现中采用的是python的无类型数，不管是double还是int都占用一个操作数栈位置
    def execute(self, frame):
        stack = frame.operandStack
        stack.pop_slot()
