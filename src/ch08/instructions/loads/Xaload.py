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
        index = stack.popNumeric()
        arrRef = stack.popRef()

        checkNotNone(arrRef)
        refs = arrRef.refs()
        checkIndex(len(refs), index)
        stack.pushRef(refs[index])

class BALOAD(NoOperandsInstruction):
    def execute(self, frame):
        stack = frame.operandStack
        index = stack.popNumeric()
        arrRef = stack.popRef()

        checkNotNone(arrRef)
        bytes = arrRef.bytes()
        checkIndex(len(bytes), index)
        stack.pushRef(bytes[index])

class CALOAD(NoOperandsInstruction):
    def execute(self, frame):
        stack = frame.operandStack
        index = stack.popNumeric()
        arrRef = stack.popRef()

        checkNotNone(arrRef)
        chars = arrRef.chars()
        checkIndex(len(chars), index)
        stack.pushRef(chars[index])

class DALOAD(NoOperandsInstruction):
    def execute(self, frame):
        stack = frame.operandStack
        index = stack.popNumeric()
        arrRef = stack.popRef()

        checkNotNone(arrRef)
        doubles = arrRef.doubles()
        checkIndex(len(doubles), index)
        stack.pushRef(doubles[index])

class FALOAD(NoOperandsInstruction):
    def execute(self, frame):
        stack = frame.operandStack
        index = stack.popNumeric()
        arrRef = stack.popRef()

        checkNotNone(arrRef)
        floats = arrRef.floats()
        checkIndex(len(floats), index)
        stack.pushRef(floats[index])

class IALOAD(NoOperandsInstruction):
    def execute(self, frame):
        stack = frame.operandStack
        index = stack.popNumeric()
        arrRef = stack.popRef()

        checkNotNone(arrRef)
        ints = arrRef.ints()
        checkIndex(len(ints), index)
        stack.pushRef(ints[index])

class LALOAD(NoOperandsInstruction):
    def execute(self, frame):
        stack = frame.operandStack
        index = stack.popNumeric()
        arrRef = stack.popRef()

        checkNotNone(arrRef)
        longs = arrRef.longs()
        checkIndex(len(longs), index)
        stack.pushRef(longs[index])

class SALOAD(NoOperandsInstruction):
    def execute(self, frame):
        stack = frame.operandStack
        index = stack.popNumeric()
        arrRef = stack.popRef()

        checkNotNone(arrRef)
        shorts = arrRef.shorts()
        checkIndex(len(shorts), index)
        stack.pushRef(shorts[index])
