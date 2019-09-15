from ch05.classfile.ConstantInfo import ConstantInfo

class ConstantNameAndTypeInfo(ConstantInfo):
    def __init__(self):
        self.nameIndex = 0
        self.descriptorIndex = 0

    def readInfo(self, classReader):
        self.nameIndex = int.from_bytes(classReader.read_unit16(), byteorder="big")
        self.descriptorIndex = int.from_bytes(classReader.read_unit16(), byteorder="big")