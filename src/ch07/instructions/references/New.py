from ch07.instructions.base.Instruction import Index16Instruction

class NEW(Index16Instruction):
    def execute(self, frame):
        from ch07.instructions.base.ClassInitLogic import ClassInitLogic

        cp = frame.method.get_class().constantPool
        classRef = cp.get_constant(self.index)
        clazz = classRef.resolvedClass()

        if not clazz.initStarted:
            frame.revertNextPC()
            ClassInitLogic.initClass(frame.thread, clazz)
            return

        if clazz.is_interface() or clazz.is_abstract():
            raise RuntimeError("java.lang.InstantiationError")

        ref = clazz.new_object()
        frame.operandStack.push_ref(ref)