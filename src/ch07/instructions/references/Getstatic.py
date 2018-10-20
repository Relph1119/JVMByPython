from ch07.instructions.base.Instruction import Index16Instruction

class GET_STATIC(Index16Instruction):
    def execute(self, frame):
        from ch07.instructions.base.ClassInitLogic import ClassInitLogic

        cp = frame.method.getClass().constantPool
        fieldRef = cp.getConstant(self.index)
        field = fieldRef.resolveField()
        clazz = field.getClass()

        if not clazz.initStarted:
            frame.revertNextPC()
            ClassInitLogic.initClass(frame.thread, clazz)
            return

        if not field.isStatic():
            raise RuntimeError("java.lang.IncompatibleClassChangeError")

        descriptor = field.descriptor
        slotId = field.slotId
        slots = clazz.staticVars
        stack = frame.operandStack

        if descriptor[0] in {"Z", "B", "C", "S", "I", "F", "J", "D"}:
            stack.pushNumeric(slots.getNumeric(slotId))
        elif descriptor[0] in {"L", "["}:
            stack.pushRef(slots.getRef(slotId))