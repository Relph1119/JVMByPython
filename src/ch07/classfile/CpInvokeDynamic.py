from ch07.classfile.ConstantInfo import ConstantInfo

class ConstantMethodHandleInfo(ConstantInfo):
    def __init__(self):
        self.referenceKind = 0
        self.referenceIndex = 0

    def readInfo(self, classReader):
        self.referenceKind = classReader.read_unit8()
        self.referenceIndex = int.from_bytes(classReader.read_unit8(), byteorder="big")

class ConstantMethodTypeInfo(ConstantInfo):
    def __init__(self):
        self.descriptorIndex = 0

    def readInfo(self, classReader):
        self.descriptorIndex = int.from_bytes(classReader.read_unit16(), byteorder="big")

class ConstantInvokeDynamicInfo(ConstantInfo):
    def __init__(self):
        self.bootstrapMethodAttrIndex = 0
        self.nameAndTypeIndex = 0

    def readInfo(self, classReader):
        self.bootstrapMethodAttrIndex = int.from_bytes(classReader.read_unit16(), byteorder="big")
        self.nameAndTypeIndex = int.from_bytes(classReader.read_unit16(), byteorder="big")