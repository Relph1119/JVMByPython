from ch07.instructions.base.Instruction import Index16Instruction

class INSTANCE_OF(Index16Instruction):
    def execute(self, frame):
        stack = frame.operandStack
        ref = stack.popRef()

        if not ref:
            stack.pushNumeric(0)
            return

        cp = frame.method.getClass().constantPool
        classRef = cp.getConstant(self.index)
        clazz = classRef.resolveClass()
        if ref.isInstanceOf(clazz):
            stack.pushNumeric(1)
        else:
            stack.pushNumeric(0)