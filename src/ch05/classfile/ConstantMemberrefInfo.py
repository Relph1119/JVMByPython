from ch05.classfile.ConstantInfo import ConstantInfo

class ConstantMemberrefInfo(ConstantInfo):
    def __init__(self, constantPool):
        self.cp = constantPool
        self.classIndex = 0
        self.nameAndTypeIndex = 0

    def readInfo(self, classReader):
        self.classIndex =  int.from_bytes(classReader.read_unit16(), byteorder="big")
        self.nameAndTypeIndex =  int.from_bytes(classReader.read_unit16(), byteorder="big")

    def className(self):
        return self.cp.class_name(self.classIndex)

    def nameAndDescrptor(self):
        return self.cp.get_name_and_type(self.nameAndTypeIndex)

class ConstantFieldrefInfo(ConstantMemberrefInfo):

    def __init__(self, constantPool):
        super(ConstantFieldrefInfo, self).__init__(constantPool)

class ConstantMethodrefInfo(ConstantMemberrefInfo):

    def __init__(self, constantPool):
        super(ConstantMethodrefInfo, self).__init__(constantPool)
        
class ConstantInterfaceMethodrefInfo(ConstantMemberrefInfo):

    def __init__(self, constantPool):
        super(ConstantInterfaceMethodrefInfo, self).__init__(constantPool)