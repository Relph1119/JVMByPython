from ch08.instructions.base.Instruction import Index16Instruction

class PUT_STATIC(Index16Instruction):
    def execute(self, frame):
        from ch08.instructions.base.ClassInitLogic import ClassInitLogic


        currentMethod = frame.method
        currentClass = currentMethod.get_class()
        cp = currentClass.constantPool
        fieldRef = cp.get_constant(self.index)
        field = fieldRef.resolve_field()
        clazz = field.get_class()

        if not clazz.initStarted:
            frame.revertNextPC()
            ClassInitLogic.initClass(frame.thread, clazz)
            return

        if not field.is_static():
            raise RuntimeError("java.lang.IncompatibleClassChangeError")
        if field.is_final():
            if currentClass != clazz or currentMethod.name != "<clinit>":
                raise RuntimeError("java.lang.IllegalAccessError")

        descriptor = field.descriptor
        slotId = field.slotId
        slots = clazz.staticVars
        stack = frame.operandStack

        if descriptor[0] in {"Z", "B", "C", "S", "I", "F", "J", "D"}:
            slots.set_numeric(slotId, stack.pop_numeric())
        elif descriptor[0] == "L":
            slots.set_ref(slotId, stack.pop_ref())
