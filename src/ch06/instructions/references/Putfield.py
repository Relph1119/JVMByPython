from ch06.instructions.base.Instruction import Index16Instruction

class PUT_FIELD(Index16Instruction):
    def execute(self, frame):
        currentMethod = frame.method
        currentClass = currentMethod.getClass()
        cp = currentClass.constantPool
        fieldRef = cp.getConstant(self.index)
        field = fieldRef.resolveField()

        if field.isStatic():
            raise RuntimeError("java.lang.IncompatibleClassChangeError")
        if field.isFinal():
            if currentClass != field.getClass() or currentMethod.name != "<init>":
                raise RuntimeError("java.lang.IllegalAccessError")

        descriptor = field.descriptor
        slotId = field.slotId
        stack = frame.operandStack

        if descriptor[0] in {"Z", "B", "C", "S", "I", "F", "J", "D"}:
            val = stack.popNumeric()
            ref = stack.popRef()
            if not ref:
                raise RuntimeError("java.lang.NollPointerException")
            ref.fields.setNumeric(slotId, val)
        elif descriptor[0] in {"L", "["}:
            val = stack.popRef()
            ref = stack.popRef()
            if not ref:
                raise RuntimeError("java.lang.NollPointerException")
            ref.fields.setRef(slotId, val)