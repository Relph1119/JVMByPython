from ch08.instructions.base.Instruction import NoOperandsInstruction
import ctypes

def checkNotNone(ref):
    if not ref:
        raise RuntimeError("java.lang.NullPointerException")

def checkIndex(arrLen, index):
    import ctypes

    if index < 0 or index >= ctypes.c_int32(arrLen).value:
        raise RuntimeError("ArrayIndexOutOfBoundsException")

class AASTORE(NoOperandsInstruction):
    def execute(self, frame):
        stack = frame.operandStack
        ref = stack.pop_ref()
        index = stack.pop_numeric()
        arrRef = stack.pop_ref()

        checkNotNone(arrRef)
        refs = arrRef.refs()
        checkIndex(len(refs), index)
        arrRef.setDataSlotsValueByIndex(index, ref)

class BASTORE(NoOperandsInstruction):
    def execute(self, frame):
        stack = frame.operandStack
        val = stack.pop_numeric()
        index = stack.pop_numeric()
        arrRef = stack.pop_ref()

        checkNotNone(arrRef)
        bytes = arrRef.bytes()
        checkIndex(len(bytes), index)
        arrRef.setDataSlotsValueByIndex(index, ctypes.c_int8(val).value)

class CASTORE(NoOperandsInstruction):
    def execute(self, frame):
        stack = frame.operandStack
        val = stack.pop_numeric()
        index = stack.pop_numeric()
        arrRef = stack.pop_ref()

        checkNotNone(arrRef)
        chars = arrRef.chars()
        checkIndex(len(chars), index)
        arrRef.setDataSlotsValueByIndex(index, ctypes.c_uint16(val).value)

class DASTORE(NoOperandsInstruction):
    def execute(self, frame):
        stack = frame.operandStack
        val = stack.pop_numeric()
        index = stack.pop_numeric()
        arrRef = stack.pop_ref()

        checkNotNone(arrRef)
        doubles = arrRef.doubles()
        checkIndex(len(doubles), index)
        arrRef.setDataSlotsValueByIndex(index, ctypes.c_float(val).value)

class FASTORE(NoOperandsInstruction):
    def execute(self, frame):
        stack = frame.operandStack
        val = stack.pop_numeric()
        index = stack.pop_numeric()
        arrRef = stack.pop_ref()

        checkNotNone(arrRef)
        floats = arrRef.floats()
        checkIndex(len(floats), index)
        arrRef.setDataSlotsValueByIndex(index, ctypes.c_float(val).value)

class IASTORE(NoOperandsInstruction):
    def execute(self, frame):
        stack = frame.operandStack
        val = stack.pop_numeric()
        index = stack.pop_numeric()
        arrRef = stack.pop_ref()

        checkNotNone(arrRef)
        ints = arrRef.ints()
        checkIndex(len(ints), index)
        arrRef.setDataSlotsValueByIndex(index, ctypes.c_int32(val).value)

class LASTORE(NoOperandsInstruction):
    def execute(self, frame):
        stack = frame.operandStack
        val = stack.pop_numeric()
        index = stack.pop_numeric()
        arrRef = stack.pop_ref()

        checkNotNone(arrRef)
        longs = arrRef.longs()
        checkIndex(len(longs), index)
        arrRef.setDataSlotsValueByIndex(index, ctypes.c_int64(val).value)

class SASTORE(NoOperandsInstruction):
    def execute(self, frame):
        stack = frame.operandStack
        val = stack.pop_numeric()
        index = stack.pop_numeric()
        arrRef = stack.pop_ref()

        checkNotNone(arrRef)
        shorts = arrRef.shorts()
        checkIndex(len(shorts), index)
        arrRef.setDataSlotsValueByIndex(index, ctypes.c_int16(val).value)
