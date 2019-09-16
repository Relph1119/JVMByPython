from ch08.rtda.heap.CpMemberRef import MemberRef
from ch08.rtda.heap.MethodLookup import MethodLookup

class MethodRef(MemberRef):
    def __init__(self):
        super(MethodRef, self).__init__()
        self.method = None

    @staticmethod
    def newMethodRef(constantPool, refInfo):
        ref = MethodRef()
        ref.cp = constantPool
        ref.copyMemberRefInfo(refInfo)
        return ref

    def resolvedMethod(self):
        if not self.method:
            self.resolveMethodRef()
        return self.method

    def resolveMethodRef(self):
        d = self.cp.get_class()
        c = self.resolvedClass()
        if c.is_interface():
            raise RuntimeError("java.lang.IncompatibleClassChangeError")

        method = MethodRef.lookupMethod(c, self.name, self.descriptor)
        if not method:
            raise RuntimeError("java.lang.NoSuchMethodError")
        if not method.is_accessible_to(d):
            raise RuntimeError("java.lang.IllegalAccessError")

        self.method = method

    @staticmethod
    def lookupMethod(clazz, name, descriptor):
        method = MethodLookup.lookupMethodInClass(clazz, name, descriptor)
        if not method:
            method = MethodLookup.lookupMethodInInterfaces(clazz.interfaces, name, descriptor)
        return method
