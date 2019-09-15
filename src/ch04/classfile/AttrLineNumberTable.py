from ch04.classfile.AttributeInfo import AttributeInfo

class LineNumberTableAttribute(AttributeInfo):
    def __init__(self):
        self.lineNumberTable = []

    def readInfo(self, classReader):
        lineNumberTableLength = int.from_bytes(classReader.read_unit16(), byteorder="big")
        self.lineNumberTable = []
        for i in range(lineNumberTableLength):
            lineNumberTableEntry = LineNumberTableEntry()
            lineNumberTableEntry.startPc = int.from_bytes(classReader.read_unit16(), byteorder="big")
            lineNumberTableEntry.lineNumber = int.from_bytes(classReader.read_unit16(), byteorder="big")
            self.lineNumberTable.append(lineNumberTableEntry)

class LineNumberTableEntry():
    def __init__(self):
        self.startPc = 0
        self.lineNumber = 0