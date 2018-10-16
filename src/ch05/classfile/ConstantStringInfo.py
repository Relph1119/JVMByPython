from ch05.classfile.ConstantInfo import ConstantInfo

class ConstantStringInfo(ConstantInfo):
    def __init__(self, constantPool):
        self.cp = constantPool
        self.stringIndex = ""

    def readInfo(self, classReader):
        self.stringIndex = int.from_bytes(classReader.readUnit16(), byteorder="big")

    def String(self):
        return self.cp.getUtf8(self.stringIndex)