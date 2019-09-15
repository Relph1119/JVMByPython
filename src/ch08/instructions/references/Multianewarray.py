from ch08.instructions.base.Instruction import Instruction
import ctypes
import copy

def popAndCheckCounts(stack, dimensions):
    counts = [0 for i in range(dimensions)]
    for i in range(dimensions-1, -1, -1):
        counts[i] = stack.pop_numeric()
        if counts[i] < 0:
            raise RuntimeError("java.lang.NegativeArraySizeException")

    return counts

def newMultiDimensionalArray(counts, arrClass):
    count = ctypes.c_uint(counts[0]).value
    arr = arrClass.newArray(count)

    if len(counts) > 1:
        refs = arr.refs()
        for i in range(refs):
            refs[i] = newMultiDimensionalArray(copy.deepcopy(counts[1:]), arrClass.componentClass())


class MULTI_ANEW_ARRAY(Instruction):
    def __init__(self):
        self.index = 0
        self.dimensions = 0

    def fetchOperands(self, bytecodeReader):
        self.index = bytecodeReader.readUint16()
        self.dimensions = bytecodeReader.readUint8()

    def execute(self, frame):
        cp = frame.method.getClass().constantPool
        classRef = cp.getConstant(ctypes.c_uint(self.index).value)
        arrClass = classRef.resolvedClass()

        stack = frame.operandStack
        counts = popAndCheckCounts(stack, int(self.dimensions))
        arr = newMultiDimensionalArray(counts, arrClass)
        stack.push_ref(arr)

