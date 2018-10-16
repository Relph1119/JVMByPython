from ch04.rtda.LocalVars import LocalVars
from ch04.rtda.OperandStack import OperandStack

class Frame():
    def __init__(self, maxLocals, maxStack):
        self.lower = None
        self.localVars = LocalVars(maxLocals)
        self.operandStack = OperandStack(maxStack)



