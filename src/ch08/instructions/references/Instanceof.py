from ch08.instructions.base.Instruction import Index16Instruction

class INSTANCE_OF(Index16Instruction):
    def execute(self, frame):
        stack = frame.operandStack
        ref = stack.pop_ref()

        if not ref:
            stack.push_numeric(0)
            return

        cp = frame.method.getClass().constantPool
        classRef = cp.getConstant(self.index)
        clazz = classRef.resolvedClass()
        if ref.isInstanceOf(clazz):
            stack.push_numeric(1)
        else:
            stack.push_numeric(0)