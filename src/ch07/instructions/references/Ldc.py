from ch07.instructions.base.Instruction import Index8Instruction, Index16Instruction

def _ldc(frame, index):
    stack = frame.operandStack
    cp = frame.method.get_class().constantPool
    c = cp.get_constant(index)

    if isinstance(c, int):
        stack.push_numeric(c)
    elif isinstance(c, float):
        stack.push_numeric(c)
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
        cp = frame.method.get_class().constantPool
        c = cp.get_constant(self.index)

        if isinstance(c, int):
            stack.push_numeric(c)
        elif isinstance(c, float):
            stack.push_numeric(c)
        else:
            raise RuntimeError("java.lang.ClassFormatError")