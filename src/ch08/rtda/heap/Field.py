from ch08.rtda.heap.ClassMember import ClassMember
from ch08.rtda.heap.AccessFlags import AccessFlags

class Field(ClassMember):
    def __init__(self):
        super(Field, self).__init__()
        self.constValueIndex = 0
        self.slotId = 0


    @staticmethod
    def newFields(clazz, cfFields):
        fields = []
        for cfField in cfFields:
            field = Field()
            field.setClass(clazz)
            field.copyMemberInfo(cfField)
            field.copyAttributes(cfField)
            fields.append(field)
        return fields

    def isVolatile(self):
        return 0 != self.accessFlags & AccessFlags.ACC_VOLATILE

    def isTransient(self):
        return 0 != self.accessFlags & AccessFlags.ACC_TRANSIENT

    def isEnum(self):
        return 0 != self.accessFlags & AccessFlags.ACC_ENUM

    def copyAttributes(self, cfField):
        valAttr = cfField.constant_value_index()
        if valAttr:
            self.constValueIndex = valAttr.constant_value_index

