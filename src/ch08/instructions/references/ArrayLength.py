from ch08.instructions.base.Instruction import NoOperandsInstruction

class ARRAY_LENGTH(NoOperandsInstruction):
    def execute(self, frame):
        stack = frame.operandStack
        arrRef = stack.pop_ref()
        if not arrRef:
            raise RuntimeError("java.lang.NullPointerException")

        arrLen = arrRef.array_length()
        stack.push_numeric(arrLen)