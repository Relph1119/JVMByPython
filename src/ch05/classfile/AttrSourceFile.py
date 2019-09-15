from ch05.classfile.AttributeInfo import AttributeInfo

class SourceFileAttribute(AttributeInfo):
    def __init__(self, constantPool):
        self.cp = constantPool
        self.sourceFileIndex = 0

    def readInfo(self, classReader):
        self.sourceFileIndex = int.from_bytes(classReader.read_unit16(), byteorder="big")

    def fileName(self):
        return self.cp.get_utf8(self.sourceFileIndex)
