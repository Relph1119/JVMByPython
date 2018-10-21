from ch08.instructions.base.Instruction import NoOperandsInstruction

class ARRAY_LENGTH(NoOperandsInstruction):
    def execute(self, frame):
        stack = frame.operandStack
        arrRef = stack.popRef()
        if not arrRef:
            raise RuntimeError("java.lang.NullPointerException")

        arrLen = arrRef.arrayLength()
        stack.pushNumeric(arrLen)