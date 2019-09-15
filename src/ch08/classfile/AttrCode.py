from ch08.classfile.AttributeInfo import AttributeInfo

class CodeAttribute(AttributeInfo):
    def __init__(self, constantPool):
        self.cp = constantPool
        self.maxStack = 0
        self.maxLocals = 0
        self.code = None
        self.exceptionTable = []
        self.attributes = []

    def readInfo(self, classReader):
        self.maxStack = int.from_bytes(classReader.read_unit16(), byteorder="big")
        self.maxLocals = int.from_bytes(classReader.read_unit16(), byteorder="big")
        codeLength = int.from_bytes(classReader.read_unit32(), byteorder="big")
        self.code = classReader.read_bytes(codeLength)
        self.exceptionTable = self.readExceptionTable(classReader)
        self.attributes = AttributeInfo.readAttributes(classReader, self.cp)

    def readExceptionTable(self, classReader):
        exceptionTableLength = int.from_bytes(classReader.read_unit16(), byteorder="big")
        exceptionTable = []
        for _ in range(exceptionTableLength):
            exceptionTableEntry = ExceptionTableEntry()
            exceptionTableEntry.startPc = int.from_bytes(classReader.read_unit16(), byteorder="big")
            exceptionTableEntry.endPc = int.from_bytes(classReader.read_unit16(), byteorder="big")
            exceptionTableEntry.handlerPc = int.from_bytes(classReader.read_unit16(), byteorder="big")
            exceptionTableEntry.catchType = int.from_bytes(classReader.read_unit16(), byteorder="big")
            exceptionTable.append(exceptionTableEntry)
        return exceptionTable

class ExceptionTableEntry():
    def __init__(self):
        self.startPc = 0
        self.endPc = 0
        self.handlerPc = 0
        self.catchType = 0


