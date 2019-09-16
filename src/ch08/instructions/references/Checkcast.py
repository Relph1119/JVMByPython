from ch08.instructions.base.Instruction import Index16Instruction

class CHECK_CAST(Index16Instruction):
    def execute(self, frame):
        stack = frame.operandStack
        ref = stack.pop_ref()
        stack.push_ref(ref)
        if not ref:
            return

        cp = frame.method.get_class().constantPool
        classRef = cp.get_constant(self.index)
        clazz = classRef.resolvedClass()
        if not ref.is_instance_of(clazz):
            raise RuntimeError("java.lang.ClassCastException")


