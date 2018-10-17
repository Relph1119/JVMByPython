from ch06.classfile.AttributeInfo import AttributeInfo

class LocalVariableTypeTableAttribute(AttributeInfo):
    def __init__(self):
        self.localVariableTable = []

    def readInfo(self, classReader):
        localVariableTableLength = int.from_bytes(classReader.readUnit16(), byteorder="big")
        for i in range(localVariableTableLength):
            localVariableTypeTableEntry = localVariableTypeTableEntry()
            localVariableTypeTableEntry.startPc = int.from_bytes(classReader.readUnit16(), byteorder="big")
            localVariableTypeTableEntry.length = int.from_bytes(classReader.readUnit16(), byteorder="big")
            localVariableTypeTableEntry.nameIndex = int.from_bytes(classReader.readUnit16(), byteorder="big")
            localVariableTypeTableEntry.descriptorIndex = int.from_bytes(classReader.readUnit16(), byteorder="big")
            localVariableTypeTableEntry.index = int.from_bytes(classReader.readUnit16(), byteorder="big")
            self.localVariableTable.append(localVariableTypeTableEntry)


class localVariableTypeTableEntry():
    def __init__(self):
        self.startPc = 0
        self.length = 0
        self.nameIndex = 0
        self.descriptorIndex = 0
        self.index = 0
