from ch08.instructions.base.Instruction import Index8Instruction, Index16Instruction
from ch08.rtda.heap.StringPool import StringPool

def _ldc(frame, index):
    stack = frame.operandStack
    clazz = frame.method.getClass()
    c = clazz.constantPool.getConstant(index)

    if isinstance(c, int):
        stack.pushNumeric(c)
    elif isinstance(c, float):
        stack.pushNumeric(c)
    elif isinstance(c, str):
        internedStr = StringPool.JString(clazz.loader, c)
        stack.pushRef(internedStr)
    else:
        raise RuntimeError("todo: ldc!")


class LDC(Index8Instruction):
    def execute(self, frame):
        _ldc(frame, self.index)

class LDC_W(Index16Instruction):
    def execute(self, frame):
        _ldc(frame, self.index)

class LDC2_W(Index16Instruction):
    def execute(self, frame):
        stack = frame.operandStack
        cp = frame.method.getClass().constantPool
        c = cp.getConstant(self.index)

        if isinstance(c, int):
            stack.pushNumeric(c)
        elif isinstance(c, float):
            stack.pushNumeric(c)
        else:
            raise RuntimeError("java.lang.ClassFormatError")