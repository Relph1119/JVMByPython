from ch07.classfile.ConstantInfo import ConstantInfo
from ch07.classfile.ConstantPool import ConstantPool

class ConstantMemberrefInfo(ConstantInfo):
    def __init__(self, constantPool):
        self.cp = ConstantPool(constantPool)
        self.classIndex = 0
        self.nameAndTypeIndex = 0

    def readInfo(self, classReader):
        self.classIndex =  int.from_bytes(classReader.readUnit16(), byteorder="big")
        self.nameAndTypeIndex =  int.from_bytes(classReader.readUnit16(), byteorder="big")

    def className(self):
        return self.cp.getClassName(self.classIndex)

    def nameAndDescrptor(self):
        return self.cp.getNameAndType(self.nameAndTypeIndex)

class ConstantFieldrefInfo(ConstantMemberrefInfo):

    def __init__(self, constantPool):
        super(ConstantFieldrefInfo, self).__init__(constantPool)

class ConstantMethodrefInfo(ConstantMemberrefInfo):

    def __init__(self, constantPool):
        super(ConstantMethodrefInfo, self).__init__(constantPool)
        
class ConstantInterfaceMethodrefInfo(ConstantMemberrefInfo):

    def __init__(self, constantPool):
        super(ConstantInterfaceMethodrefInfo, self).__init__(constantPool)