from ch04.classfile.ConstantInfo import ConstantInfo

class ConstantClassInfo(ConstantInfo):
    def __init__(self, constantPool):
        self.cp = constantPool
        self.nameIndex = 0

    def readInfo(self, classReader):
        self.nameIndex = int.from_bytes(classReader.read_unit16(), byteorder="big")

    def name(self):
        return self.cp.get_utf8(self.nameIndex)

