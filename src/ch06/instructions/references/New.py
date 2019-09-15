from ch06.instructions.base.Instruction import Index16Instruction

class NEW(Index16Instruction):
    def execute(self, frame):
        cp = frame.method.getClass().constantPool
        classRef = cp.getConstant(self.index)
        clazz = classRef.resolveClass()

        if clazz.isInterface() or clazz.isAbstract():
            raise RuntimeError("java.lang.InstantiationError")

        ref = clazz.newObject()
        frame.operandStack.push_ref(ref)