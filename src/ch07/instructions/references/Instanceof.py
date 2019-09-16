from ch07.instructions.base.Instruction import Index16Instruction

class INSTANCE_OF(Index16Instruction):
    def execute(self, frame):
        stack = frame.operandStack
        ref = stack.pop_ref()

        if not ref:
            stack.push_numeric(0)
            return

        cp = frame.method.get_class().constantPool
        classRef = cp.get_constant(self.index)
        clazz = classRef.resolvedClass()
        if ref.is_instance_of(clazz):
            stack.push_numeric(1)
        else:
            stack.push_numeric(0)