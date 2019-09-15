from ch07.instructions.base.Instruction import Index16Instruction

class CHECK_CAST(Index16Instruction):
    def execute(self, frame):
        stack = frame.operandStack
        ref = stack.pop_ref()
        stack.push_ref(ref)
        if not ref:
            return

        cp = frame.method.getClass().constantPool
        classRef = cp.getConstant(self.index)
        clazz = classRef.resolvedClass()
        if not ref.isInstanceOf(clazz):
            raise RuntimeError("java.lang.ClassCastException")


