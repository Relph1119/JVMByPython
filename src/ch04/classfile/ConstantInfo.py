from abc import ABCMeta, abstractstaticmethod

class ConstantInfo(metaclass=ABCMeta):

    CONSTANT_Class = 7
    CONSTANT_Fieldref = 9
    CONSTANT_Methodref = 10
    CONSTANT_InterfaceMethodref = 11
    CONSTANT_String = 8
    CONSTANT_Integer = 3
    CONSTANT_Float = 4
    CONSTANT_Long = 5
    CONSTANT_Double = 6
    CONSTANT_NameAndType = 12
    CONSTANT_Utf8 = 1
    CONSTANT_MethodHandler = 15
    CONSTANT_MethodType = 16
    CONSTANT_InvokeDynamic = 18

    @abstractstaticmethod
    def readInfo(self, classReader):
        pass

    @staticmethod
    def readConstantInfo(classReader, constantPool):
        tag = int.from_bytes(classReader.readUnit8(), byteorder="big")
        c = ConstantInfo.newConstatnInfo(tag, constantPool)
        c.readInfo(classReader)
        return c

    @staticmethod
    def newConstatnInfo(tag, constantPool):
        from ch04.classfile.CpNumeric import ConstantDoubleInfo, ConstantLongInfo, ConstantFloatInfo, ConstantIntgerInfo
        from ch04.classfile.ConstantUtf8Info import ConstantUtf8Info
        from ch04.classfile.ConstantStringInfo import ConstantStringInfo
        from ch04.classfile.ConstantMemberrefInfo import ConstantFieldrefInfo, ConstantInterfaceMethodrefInfo, \
            ConstantMethodrefInfo
        from ch04.classfile.ConstantNameAndTypeInfo import ConstantNameAndTypeInfo
        from ch04.classfile.ConstantClassInfo import ConstantClassInfo
        from ch04.classfile.CpInvokeDynamic import ConstantInvokeDynamicInfo, ConstantMethodHandleInfo, \
            ConstantMethodTypeInfo

        if tag == ConstantInfo.CONSTANT_Integer:
            return ConstantIntgerInfo()
        elif tag == ConstantInfo.CONSTANT_Float:
            return ConstantFloatInfo()
        elif tag == ConstantInfo.CONSTANT_Long:
            return ConstantLongInfo()
        elif tag == ConstantInfo.CONSTANT_Double:
            return ConstantDoubleInfo()
        elif tag == ConstantInfo.CONSTANT_Utf8:
            return ConstantUtf8Info()
        elif tag == ConstantInfo.CONSTANT_String:
            return ConstantStringInfo(constantPool)
        elif tag == ConstantInfo.CONSTANT_Class:
            return ConstantClassInfo(constantPool)
        elif tag == ConstantInfo.CONSTANT_Fieldref:
            return ConstantFieldrefInfo(constantPool)
        elif tag == ConstantInfo.CONSTANT_Methodref:
            return ConstantMethodrefInfo(constantPool)
        elif tag == ConstantInfo.CONSTANT_InterfaceMethodref:
            return ConstantInterfaceMethodrefInfo(constantPool)
        elif tag == ConstantInfo.CONSTANT_NameAndType:
            return ConstantNameAndTypeInfo()
        elif tag == ConstantInfo.CONSTANT_MethodHandler:
            return ConstantMethodHandleInfo()
        elif tag == ConstantInfo.CONSTANT_MethodType:
            return ConstantMethodTypeInfo()
        elif tag == ConstantInfo.CONSTANT_InvokeDynamic:
            return ConstantInvokeDynamicInfo()
        else:
            raise RuntimeError("java.lang.ClassFormatError: constant pool tag!")

