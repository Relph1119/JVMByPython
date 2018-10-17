from ch06.rtda.LocalVars import LocalVars
from ch06.rtda.OperandStack import OperandStack

class Frame():
    def __init__(self, thread ,maxLocals, maxStack):
        self.lower = None
        self.localVars = LocalVars(maxLocals)
        self.operandStack = OperandStack(maxStack)
        self.thread = thread
        self.nextPC = 0



