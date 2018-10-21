from ch08.rtda.heap.CpMemberRef import MemberRef
from ch08.rtda.heap.MethodLookup import MethodLookup

class InterfaceMethodRef(MemberRef):
    def __init__(self):
        super(InterfaceMethodRef, self).__init__()
        self.method = None

    @staticmethod
    def newInterfaceMethodRef(constantPool, refInfo):
        ref = InterfaceMethodRef()
        ref.cp = constantPool
        ref.copyMemberRefInfo(refInfo)
        return ref

    def resolvedInterfaceMethod(self):
        if not self.method:
            self.resolveInterfaceMethodRef()
        return self.method

    def resolveInterfaceMethodRef(self):
        d = self.cp.getClass
        c = self.resolvedClass()
        if not c.isInterface():
            raise RuntimeError("java.lang.IncompatibleClassChangeError")

        method = InterfaceMethodRef.lookupInterfaceMethod(c, self.name, self.descriptor)
        if not method:
            raise RuntimeError("java.lang.NoSuchMethodError")
        if not method.isAccessibleTo(d):
            raise RuntimeError("java.lang.IllegalAccessError")

        self.method = method

    @staticmethod
    def lookupInterfaceMethod(iface, name, descriptor):
        for method in iface.methods:
            if method.name == name and method.descriptor == descriptor:
                return method

        return MethodLookup.lookupMethodInInterfaces(iface.interfaces, name, descriptor)
    