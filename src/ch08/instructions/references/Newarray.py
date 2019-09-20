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
        self.atype = bytecodeReader.read_uint8()

    def execute(self, frame):
        import ctypes

        stack = frame.operandStack
        count = stack.pop_numeric()
        if count < 0:
            raise RuntimeError("java.lang.NegativeArraySizeException")

        classLoader = frame.method.get_class().loader
        arrClass = NEW_ARRAY.getPrimitiveArrayClass(classLoader, self.atype)
        arr = arrClass.new_array(ctypes.c_uint(count).value)
        stack.push_ref(arr)

    @staticmethod
    def getPrimitiveArrayClass(loader, atype):
        if atype == NEW_ARRAY.AT_BOOLEAN:
            return loader.load_class("[Z")
        elif atype == NEW_ARRAY.AT_BYTE:
            return loader.load_class("[B")
        elif atype == NEW_ARRAY.AT_CHAR:
            return loader.load_class("[C")
        elif atype == NEW_ARRAY.AT_SHORT:
            return loader.load_class("[S")
        elif atype == NEW_ARRAY.AT_INT:
            return loader.load_class("[I")
        elif atype == NEW_ARRAY.AT_LONG:
            return loader.load_class("[J")
        elif atype == NEW_ARRAY.AT_FLOAT:
            return loader.load_class("[F")
        elif atype == NEW_ARRAY.AT_DOUBLE:
            return loader.load_class("[D")
        else:
            raise RuntimeError("Invalid atype!")
