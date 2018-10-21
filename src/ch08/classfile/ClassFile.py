from ch08.classfile.ClassReader import ClassReader
from ch08.classfile.ConstantPool import ConstantPool
from ch08.classfile.MemberInfo import MemberInfo
from ch08.classfile.AttributeInfo import AttributeInfo

class ClassFile():
    def __init__(self, classData):
        self.classData = classData
        self.magic = ""
        self.minorVersion = ""
        self.majorVersion = ""
        self.constantPool = None
        self.accessFlags = ""
        self.thisClass = ""
        self.superClass = ""
        self.interfaces = []
        self.fields = []
        self.methods = []
        self.attributes = []

    def parse(self):
        try:
            cr = ClassReader(self.classData)
            self.read(cr)
            return self, None
        except Exception as e:
            return self, e

    def read(self, classReader):
        self.readAndCheckMaigc(classReader)
        self.readAndCheckVersion(classReader)
        self.constantPool = ConstantPool()
        self.constantPool.readConstantPool(classReader)
        self.accessFlags = int.from_bytes(classReader.readUnit16(), byteorder="big")
        self.thisClass = int.from_bytes(classReader.readUnit16(), byteorder="big")
        self.superClass = int.from_bytes(classReader.readUnit16(), byteorder="big")
        self.interfaces = classReader.readUnit16s()
        memberInfo = MemberInfo(self.constantPool)
        self.fields = memberInfo.readMembers(classReader, self.constantPool)
        self.methods = memberInfo.readMembers(classReader, self.constantPool)
        self.attributes = AttributeInfo.readAttributes(classReader, self.constantPool)

    def readAndCheckMaigc(self, classReader):
        magic = classReader.readUnit32()
        if magic != b'\xca\xfe\xba\xbe':
            raise RuntimeError("java.lang.ClassFormatError: magic")

    def readAndCheckVersion(self, classReader):
        self.minorVersion = int.from_bytes(classReader.readUnit16(), byteorder = 'big')
        self.majorVersion = int.from_bytes(classReader.readUnit16(), byteorder = 'big')
        if self.majorVersion == 45:
            return
        elif self.majorVersion in {46, 47, 48, 49, 50, 51, 52}:
            if self.minorVersion == 0:
                return
        raise RuntimeError("java.lang.UnsupportedClassVersionError!")

    def className(self):
        return self.constantPool.getClassName(self.thisClass)

    def superClassName(self):
        if self.superClass:
            return self.constantPool.getClassName(self.superClass)
        return ""

    def interfaceNames(self):
        return [self.constantPool.getClassName(cpName) for cpName in self.interfaces]

