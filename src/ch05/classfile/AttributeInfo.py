from abc import ABCMeta, abstractstaticmethod

class AttributeInfo(metaclass=ABCMeta):

    @abstractstaticmethod
    def readInfo(self, classReader):
        pass

    @staticmethod
    def readAttributes(classReader, constantPool):
        attributesCount = int.from_bytes(classReader.read_unit16(), byteorder="big")
        attributes = []
        for i in range(attributesCount):
            attributes.append(AttributeInfo.readAttribute(classReader, constantPool))
        return attributes

    @staticmethod
    def readAttribute(classReader, constantPool):
        attrNameIndex = int.from_bytes(classReader.read_unit16(), byteorder="big")
        attrName = ""
        if attrNameIndex != 0:
           attrName = constantPool.get_utf8(attrNameIndex)
        attrLen = int.from_bytes(classReader.read_unit32(), byteorder="big")
        attrInfo = AttributeInfo.newAttributeInfo(attrName, attrLen, constantPool)
        attrInfo.readInfo(classReader)
        return attrInfo

    @staticmethod
    def newAttributeInfo(attrName, attrLen, constantPool):
        from ch05.classfile.AttrCode import CodeAttribute
        from ch05.classfile.AttrConstantValue import ConstantValueAttribute
        from ch05.classfile.AttrMarkers import DeprecatedAttribute, SyntheticAttribute
        from ch05.classfile.AttrExceptions import ExceptionsAttribute
        from ch05.classfile.AttrLineNumberTable import LineNumberTableAttribute
        from ch05.classfile.AttrSourceFile import SourceFileAttribute
        from ch05.classfile.AttrUnparsed import UnparsedAttribute
        from ch05.classfile.AttrLocalVariableTable import LocalVariableTableAttribute

        if attrName == "Code":
            return CodeAttribute(constantPool)
        elif attrName == "ConstantValue":
            return ConstantValueAttribute()
        elif attrName == "Deprecated":
            return DeprecatedAttribute()
        elif attrName == "Exceptions":
            return ExceptionsAttribute()
        elif attrName == "LineNumberTable":
            return LineNumberTableAttribute()
        elif attrName == "LocalVariableTable":
            return LocalVariableTableAttribute()
        elif attrName == "SourceFile":
            return SourceFileAttribute(constantPool)
        elif attrName == "Synthetic":
            return SyntheticAttribute()
        else:
            return UnparsedAttribute(attrName, attrLen)



