from ch08.instructions.base.Instruction import Index16Instruction

class GET_STATIC(Index16Instruction):
    def execute(self, frame):
        from ch08.instructions.base.ClassInitLogic import ClassInitLogic

        cp = frame.method.get_class().constantPool
        fieldRef = cp.get_constant(self.index)
        field = fieldRef.resolve_field()
        clazz = field.get_class()

        if not clazz.initStarted:
            frame.revertNextPC()
            ClassInitLogic.initClass(frame.thread, clazz)
            return

        if not field.is_static():
            raise RuntimeError("java.lang.IncompatibleClassChangeError")

        descriptor = field.descriptor
        slotId = field.slotId
        slots = clazz.staticVars
        stack = frame.operandStack

        if descriptor[0] in {"Z", "B", "C", "S", "I", "F", "J", "D"}:
            stack.push_numeric(slots.get_numeric(slotId))
        elif descriptor[0] in {"L", "["}:
            stack.push_ref(slots.get_ref(slotId))