from ch05.classfile.AttributeInfo import AttributeInfo

class UnparsedAttribute(AttributeInfo):
    def __init__(self, attrName, attrLen):
        self.name = attrName
        self.length = attrLen
        self.info = ""

    def readInfo(self, classReader):
        self.info = classReader.read_bytes(self.length)
