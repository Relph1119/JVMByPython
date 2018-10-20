from ch07.rtda.LocalVars import LocalVars
from ch07.rtda.OperandStack import OperandStack

class Frame():
    def __init__(self, thread, method):
        self.lower = None
        self.method = method
        self.localVars = LocalVars(method.maxLocals)
        self.operandStack = OperandStack(method.maxStack)
        self.thread = thread
        self.nextPC = 0

    def revertNextPC(self):
        self.nextPC = self.thread.pc


