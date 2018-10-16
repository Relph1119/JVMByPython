

class ConstantPool():
    def __init__(self):
        self.cp = []

    def readConstantPool(self, classReader):
        from ch03.classfile.CpNumeric import ConstantLongInfo, ConstantDoubleInfo
        from ch03.classfile.ConstantInfo import ConstantInfo

        cpCount = int.from_bytes(classReader.readUnit16(), byteorder="big")
        self.cp = [0 for i in range(cpCount)]

        i = 1
        while i < cpCount:
            self.cp[i] = ConstantInfo.readConstantInfo(classReader, self.cp)
            if isinstance(self.cp[i], ConstantLongInfo) or isinstance(self.cp[i], ConstantDoubleInfo):
                i += 1
            i += 1

    def getConstantInfo(self, index):
        cpInfo = self.cp[index]
        if cpInfo:
            return cpInfo
        else:
            raise RuntimeError("Invalid constant pool index!")

    def getNameAndType(self, index):
        ntInfo = self.getConstantInfo(index)
        name = self.getUtf8(ntInfo.nameIndex)
        _type = self.getUtf8(ntInfo.descriptorIndex)
        return name, _type

    def getClassName(self, index):
        classInfo = self.getConstantInfo(index)
        return self.getUtf8(classInfo.nameIndex)

    def getUtf8(self, index):
        utf8info = self.getConstantInfo(index)
        return utf8info.str