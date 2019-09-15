from ch08.instructions.base.Instruction import NoOperandsInstruction

def checkNotNone(ref):
    if not ref:
        raise RuntimeError("java.lang.NullPointerException")

def checkIndex(arrLen, index):
    import ctypes

    if index < 0 or index >= ctypes.c_int32(arrLen).value:
        raise RuntimeError("ArrayIndexOutOfBoundsException")


class AALOAD(NoOperandsInstruction):
    def execute(self, frame):
        stack = frame.operandStack
        index = stack.pop_numeric()
        arrRef = stack.pop_ref()

        checkNotNone(arrRef)
        refs = arrRef.refs()
        checkIndex(len(refs), index)
        stack.push_ref(refs[index])

class BALOAD(NoOperandsInstruction):
    def execute(self, frame):
        stack = frame.operandStack
        index = stack.pop_numeric()
        arrRef = stack.pop_ref()

        checkNotNone(arrRef)
        bytes = arrRef.bytes()
        checkIndex(len(bytes), index)
        stack.push_numeric(bytes[index])

class CALOAD(NoOperandsInstruction):
    def execute(self, frame):
        stack = frame.operandStack
        index = stack.pop_numeric()
        arrRef = stack.pop_ref()

        checkNotNone(arrRef)
        chars = arrRef.chars()
        checkIndex(len(chars), index)
        stack.push_numeric(chars[index])

class DALOAD(NoOperandsInstruction):
    def execute(self, frame):
        stack = frame.operandStack
        index = stack.pop_numeric()
        arrRef = stack.pop_ref()

        checkNotNone(arrRef)
        doubles = arrRef.doubles()
        checkIndex(len(doubles), index)
        stack.push_numeric(doubles[index])

class FALOAD(NoOperandsInstruction):
    def execute(self, frame):
        stack = frame.operandStack
        index = stack.pop_numeric()
        arrRef = stack.pop_ref()

        checkNotNone(arrRef)
        floats = arrRef.floats()
        checkIndex(len(floats), index)
        stack.push_numeric(floats[index])

class IALOAD(NoOperandsInstruction):
    def execute(self, frame):
        stack = frame.operandStack
        index = stack.pop_numeric()
        arrRef = stack.pop_ref()

        checkNotNone(arrRef)
        ints = arrRef.ints()
        checkIndex(len(ints), index)
        stack.push_numeric(ints[index])

class LALOAD(NoOperandsInstruction):
    def execute(self, frame):
        stack = frame.operandStack
        index = stack.pop_numeric()
        arrRef = stack.pop_ref()

        checkNotNone(arrRef)
        longs = arrRef.longs()
        checkIndex(len(longs), index)
        stack.push_numeric(longs[index])

class SALOAD(NoOperandsInstruction):
    def execute(self, frame):
        stack = frame.operandStack
        index = stack.pop_numeric()
        arrRef = stack.pop_ref()

        checkNotNone(arrRef)
        shorts = arrRef.shorts()
        checkIndex(len(shorts), index)
        stack.push_numeric(shorts[index])
