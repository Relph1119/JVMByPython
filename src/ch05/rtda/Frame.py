from ch05.rtda.LocalVars import LocalVars
from ch05.rtda.OperandStack import OperandStack

class Frame():
    def __init__(self, maxLocals, maxStack):
        self.lower = None
        self.localVars = LocalVars(maxLocals)
        self.operandStack = OperandStack(maxStack)



