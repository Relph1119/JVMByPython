from ch07.instructions.base.Instruction import Index16Instruction

class GET_FIELD(Index16Instruction):
    def execute(self, frame):
        cp = frame.method.get_class().constantPool
        fieldRef = cp.get_constant(self.index)
        field = fieldRef.resolve_field()

        if field.is_static():
            raise RuntimeError("java.lang.IncompatibleClassChangeError")

        stack = frame.operandStack
        ref = stack.pop_ref()
        if not ref:
            raise RuntimeError("java.lang.NollPointerException")

        descriptor = field.descriptor
        slotId = field.slotId
        slots = ref.fields

        if descriptor[0] in {"Z", "B", "C", "S", "I", "F", "J", "D"}:
            stack.push_numeric(slots.get_numeric(slotId))
        elif descriptor[0] in {"L", "["}:
            stack.push_ref(slots.get_ref(slotId))