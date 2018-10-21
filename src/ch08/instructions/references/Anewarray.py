from ch08.instructions.base.Instruction import Index16Instruction

class ANEW_ARRAY(Index16Instruction):
    def execute(self, frame):
        import ctypes

        cp = frame.method.getClass().constantPool
        classRef = cp.getConstant(self.index)
        componentClass = classRef.resolvedClass()

        stack = frame.operandStack
        count = stack.popNumeric()
        if count < 0:
            raise RuntimeError("java.lang.NegativeArraySizeException")

        arrClass = componentClass.arrayClass()
        arr = arrClass.newArray(ctypes.c_uint(count))
        stack.pushRef(arr)

    