from ch08.rtda.heap.CpMemberRef import MemberRef

class FieldRef(MemberRef):
    def __init__(self):
        super(FieldRef, self).__init__()
        self.field = None

    @staticmethod
    def newFieldRef(constantPool, refInfo):
        ref = FieldRef()
        ref.cp = constantPool
        ref.copyMemberRefInfo(refInfo)
        return ref

    def resolveField(self):
        if not self.field:
            self.resolveFieldRef()
        return self.field

    def resolveFieldRef(self):
        d = self.cp.get_class()
        c = self.resolvedClass()
        field = FieldRef.lookupField(c, self.name, self.descriptor)

        if not field:
            raise RuntimeError("java.lang.NoSuchFieldError")

        if not field.isAccessibleTo(d):
            raise RuntimeError("java.lang.IllegalAccessError")

        self.field = field

    @staticmethod
    def lookupField(c, name, descriptor):
        for field in c.fields:
            if field.name == name and field.descriptor == descriptor:
                return field

        for interface in c.interfaces:
            field = FieldRef.lookupField(interface, name, descriptor)
            if field:
                return field

        if c.superClass:
            return FieldRef.lookupField(c.superClass, name, descriptor)

        return None
