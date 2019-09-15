from ch06.classfile.AttributeInfo import AttributeInfo

class ExceptionsAttribute(AttributeInfo):
    def __init__(self):
        self.exceptionIndexTable = []

    def readInfo(self, classReader):
        self.exceptionIndexTable = classReader.read_unit16s()
        