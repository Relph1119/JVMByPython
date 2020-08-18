from classfile.ConstantInfo import ConstantInfo


class ConstantMethodHandleInfo(ConstantInfo):
    def __init__(self):
        self.referenceKind = 0
        self.referenceIndex = 0

    def read_info(self, class_reader):
        self.referenceKind = class_reader.read_unit8()
        self.referenceIndex = int.from_bytes(class_reader.read_unit16(), byteorder="big")


class ConstantMethodTypeInfo(ConstantInfo):
    def __init__(self):
        self.descriptorIndex = 0

    def read_info(self, class_reader):
        self.descriptorIndex = int.from_bytes(class_reader.read_unit16(), byteorder="big")


class ConstantInvokeDynamicInfo(ConstantInfo):
    def __init__(self):
        self.bootstrapMethodAttrIndex = 0
        self.nameAndTypeIndex = 0

    def read_info(self, class_reader):
        self.bootstrapMethodAttrIndex = int.from_bytes(class_reader.read_unit16(), byteorder="big")
        self.nameAndTypeIndex = int.from_bytes(class_reader.read_unit16(), byteorder="big")
