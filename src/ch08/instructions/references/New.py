from ch08.instructions.base.Instruction import Index16Instruction

class NEW(Index16Instruction):
    def execute(self, frame):
        from ch08.instructions.base.ClassInitLogic import ClassInitLogic

        cp = frame.method.getClass().constantPool
        classRef = cp.getConstant(self.index)
        clazz = classRef.resolvedClass()

        if not clazz.initStarted:
            frame.revertNextPC()
            ClassInitLogic.initClass(frame.thread, clazz)
            return

        if clazz.isInterface() or clazz.isAbstract():
            raise RuntimeError("java.lang.InstantiationError")

        ref = clazz.newObject()
        frame.operandStack.pushRef(ref)