from ch03.classfile.AttributeInfo import AttributeInfo

class SourceFileAttribute(AttributeInfo):
    def __init__(self, constantPool):
        self.cp = constantPool
        self.sourceFileIndex = 0

    def readInfo(self, classReader):
        self.sourceFileIndex = int.from_bytes(classReader.readUnit16(), byteorder="big")

    def fileName(self):
        return self.cp.getUtf8(self.sourceFileIndex)
