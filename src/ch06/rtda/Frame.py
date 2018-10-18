from ch06.rtda.LocalVars import LocalVars
from ch06.rtda.OperandStack import OperandStack

class Frame():
    def __init__(self, thread, method):
        self.lower = None
        self.method = method
        self.localVars = LocalVars(method.maxLocals)
        self.operandStack = OperandStack(method.maxStack)
        self.thread = thread
        self.nextPC = 0



