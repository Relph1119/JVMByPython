from ch03.classfile.ConstantInfo import ConstantInfo

class ConstantClassInfo(ConstantInfo):
    def __init__(self, constantPool):
        self.cp = constantPool
        self.nameIndex = 0

    def readInfo(self, classReader):
        self.nameIndex = int.from_bytes(classReader.readUnit16(), byteorder="big")

    def name(self):
        return self.cp.getUtf8(self.nameIndex)

