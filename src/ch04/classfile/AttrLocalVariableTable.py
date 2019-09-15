from ch04.classfile.AttributeInfo import AttributeInfo

class LocalVariableTableAttribute(AttributeInfo):
    def __init__(self):
        self.localVariableTable = []

    def readInfo(self, classReader):
        localVariableTableLength = int.from_bytes(classReader.read_unit16(), byteorder="big")
        for i in range(localVariableTableLength):
            localVariableTableEntry = LocalVariableTableEntry()
            localVariableTableEntry.startPc = int.from_bytes(classReader.read_unit16(), byteorder="big")
            localVariableTableEntry.length = int.from_bytes(classReader.read_unit16(), byteorder="big")
            localVariableTableEntry.nameIndex = int.from_bytes(classReader.read_unit16(), byteorder="big")
            localVariableTableEntry.descriptorIndex = int.from_bytes(classReader.read_unit16(), byteorder="big")
            localVariableTableEntry.index = int.from_bytes(classReader.read_unit16(), byteorder="big")
            self.localVariableTable.append(localVariableTableEntry)


class LocalVariableTableEntry():
    def __init__(self):
        self.startPc = 0
        self.length = 0
        self.nameIndex = 0
        self.descriptorIndex = 0
        self.index = 0
