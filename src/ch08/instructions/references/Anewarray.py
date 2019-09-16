from ch08.instructions.base.Instruction import Index16Instruction

class ANEW_ARRAY(Index16Instruction):
    def execute(self, frame):
        import ctypes

        cp = frame.method.get_class().constantPool
        classRef = cp.get_constant(self.index)
        componentClass = classRef.resolvedClass()

        stack = frame.operandStack
        count = stack.pop_numeric()
        if count < 0:
            raise RuntimeError("java.lang.NegativeArraySizeException")

        arrClass = componentClass.arrayClass()
        arr = arrClass.newArray(ctypes.c_uint(count))
        stack.push_ref(arr)

    