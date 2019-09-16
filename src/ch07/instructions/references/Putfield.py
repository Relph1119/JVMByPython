from ch07.instructions.base.Instruction import Index16Instruction

class PUT_FIELD(Index16Instruction):
    def execute(self, frame):
        currentMethod = frame.method
        currentClass = currentMethod.get_class()
        cp = currentClass.constantPool
        fieldRef = cp.get_constant(self.index)
        field = fieldRef.resolve_field()

        if field.is_static():
            raise RuntimeError("java.lang.IncompatibleClassChangeError")
        if field.is_final():
            if currentClass != field.get_class() or currentMethod.name != "<init>":
                raise RuntimeError("java.lang.IllegalAccessError")

        descriptor = field.descriptor
        slotId = field.slotId
        stack = frame.operandStack

        if descriptor[0] in {"Z", "B", "C", "S", "I", "F", "J", "D"}:
            val = stack.pop_numeric()
            ref = stack.pop_ref()
            if not ref:
                raise RuntimeError("java.lang.NollPointerException")
            ref.fields.set_numeric(slotId, val)
        elif descriptor[0] in {"L", "["}:
            val = stack.pop_ref()
            ref = stack.pop_ref()
            if not ref:
                raise RuntimeError("java.lang.NollPointerException")
            ref.fields.set_ref(slotId, val)