from ch07.classfile.AttributeInfo import AttributeInfo

class ExceptionsAttribute(AttributeInfo):
    def __init__(self):
        self.exceptionIndexTable = []

    def readInfo(self, classReader):
        self.exceptionIndexTable = classReader.readUnit16s()
        