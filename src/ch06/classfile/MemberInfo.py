

class MemberInfo():
    def __init__(self, constantPool):
        self.cp = constantPool
        self.accessFlags = ""
        self.nameIndex = ""
        self.descriptorIndex = ""
        self.attributes = []

    def readMembers(self, classReader, constantPool):
        memberCount =  int.from_bytes(classReader.readUnit16(), byteorder = 'big')
        members = []
        for i in range(memberCount):
            members.append(self.readMember(classReader, constantPool))
        return members

    def readMember(self, classReader, constantPool):
        from ch06.classfile.AttributeInfo import AttributeInfo

        member = MemberInfo(constantPool)
        member.accessFlags = int.from_bytes(classReader.readUnit16(), byteorder="big")
        member.nameIndex = int.from_bytes(classReader.readUnit16(), byteorder="big")
        member.descriptorIndex = int.from_bytes(classReader.readUnit16(), byteorder="big")
        member.attributes = AttributeInfo.readAttributes(classReader, constantPool)
        return member

    def name(self):
        return self.cp.getUtf8(self.nameIndex)

    def descriptor(self):
        return self.cp.getUtf8(self.descriptorIndex)

    def codeAttribute(self):
        from ch06.classfile.AttrCode import CodeAttribute

        for attrInfo in self.attributes:
            if isinstance(attrInfo, CodeAttribute):
                return attrInfo

        return None

    def constantValueIndex(self):
        from ch06.classfile.AttrConstantValue import ConstantValueAttribute

        for attrInfo in self.attributes:
            if isinstance(attrInfo, ConstantValueAttribute):
                return attrInfo

        return None