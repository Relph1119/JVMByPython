from ch04.classfile.AttributeInfo import AttributeInfo

class ConstantValueAttribute(AttributeInfo):
    def __init__(self):
        self.constantValueIndex = 0

    def readInfo(self, classReader):
        self.constantValueIndex = int.from_bytes(classReader.read_unit16(), byteorder="big")

    