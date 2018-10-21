from ch08.instructions.base.Instruction import Instruction

class NEW_ARRAY(Instruction):

    AT_BOOLEAN = 4
    AT_CHAR = 5
    AT_FLOAT = 6
    AT_DOUBLE = 7
    AT_BYTE = 8
    AT_SHORT = 9
    AT_INT = 10
    AT_LONG = 11

    def __init__(self):
        self.atype = 0

    def fetchOperands(self, bytecodeReader):
        self.atype = bytecodeReader.readUint8()

    def execute(self, frame):
        import ctypes

        stack = frame.operandStack
        count = stack.popNumeric()
        if count < 0:
            raise RuntimeError("java.lang.NegativeArraySizeException")

        classLoader = frame.method.getClass().loader
        arrClass = NEW_ARRAY.getPrimitiveArrayClass(classLoader, self.atype)
        arr = arrClass.newArray(ctypes.c_uint(count).value)
        stack.pushRef(arr)

    @staticmethod
    def getPrimitiveArrayClass(loader, atype):
        if atype == NEW_ARRAY.AT_BOOLEAN:
            return loader.loadClass("[Z")
        elif atype == NEW_ARRAY.AT_BYTE:
            return loader.loadClass("[B")
        elif atype == NEW_ARRAY.AT_CHAR:
            return loader.loadClass("[C")
        elif atype == NEW_ARRAY.AT_SHORT:
            return loader.loadClass("[S")
        elif atype == NEW_ARRAY.AT_INT:
            return loader.loadClass("[I")
        elif atype == NEW_ARRAY.AT_LONG:
            return loader.loadClass("[J")
        elif atype == NEW_ARRAY.AT_FLOAT:
            return loader.loadClass("[F")
        elif atype == NEW_ARRAY.AT_DOUBLE:
            return loader.loadClass("[D")
        else:
            raise RuntimeError("Invalid atype!")
