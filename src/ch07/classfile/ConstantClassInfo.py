from ch07.classfile.ConstantInfo import ConstantInfo
from ch07.classfile.ConstantPool import ConstantPool

class ConstantClassInfo(ConstantInfo):
    def __init__(self, constantPool):
        self.cp = ConstantPool(constantPool)
        self.nameIndex = 0

    def readInfo(self, classReader):
        self.nameIndex = int.from_bytes(classReader.readUnit16(), byteorder="big")

    def name(self):
        return self.cp.getUtf8(self.nameIndex)

