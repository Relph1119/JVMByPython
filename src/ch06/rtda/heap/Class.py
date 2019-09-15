from ch06.rtda.heap.AccessFlags import AccessFlags

class Class():
    def __init__(self):
        self.accessFlags = 0
        self.name = ""
        self.superClassName = ""
        self.interfaceNames = []
        self.constantPool = None
        self.fields = []
        self.methods = []
        self.loader = None
        self.superClass = None
        self.interfaces = []
        self.instanceSlotCount = 0
        self.staticSlotCount = 0
        self.staticVars = None

    @staticmethod
    def newClass(classFile):
        from ch06.rtda.heap.ConstantPool import ConstantPool
        from ch06.rtda.heap.Field import Field
        from ch06.rtda.heap.Method import Method

        clazz = Class()
        clazz.accessFlags = classFile.accessFlags
        clazz.name = classFile.class_name()
        clazz.superClassName = classFile.super_class_name()
        clazz.interfaceNames = classFile.interface_names()
        clazz.constantPool = ConstantPool.newConstantPool(clazz, classFile.constantPool)
        clazz.fields = Field.newFields(clazz, classFile.fields)
        clazz.methods = Method.newMethod(clazz, classFile.methods)
        return clazz

    def isPublic(self):
        return 0 != self.accessFlags & AccessFlags.ACC_PUBLIC

    def isFinal(self):
        return 0 != self.accessFlags & AccessFlags.ACC_FINAL

    def isSuper(self):
        return 0 != self.accessFlags & AccessFlags.ACC_SUPER

    def isInterface(self):
        return 0 != self.accessFlags & AccessFlags.ACC_INTERFACE

    def isAbstract(self):
        return 0 != self.accessFlags & AccessFlags.ACC_ABSTRACT

    def isSynthetic(self):
        return 0 != self.accessFlags & AccessFlags.ACC_SYNTHETIC

    def isAnnotation(self):
        return 0 != self.accessFlags & AccessFlags.ACC_ANNOTATION

    def isEnum(self):
        return 0 != self.accessFlags & AccessFlags.ACC_ENUM

    def isAccessibleTo(self, otherClass):
        return self.isPublic() or self.getPackageName() == otherClass.getPackageName()

    def getPackageName(self):
        i = self.name.rfind("/")
        if i >= 0:
            return self.name[:i]
        return ""

    def isAssignableFrom(self, otherClass):
        s, t = otherClass, self
        if s == t:
            return True

        if not t.isInterface():
            return s.isSubClassOf(t)
        else:
            return s.isImplements(t)

    def isSubClassOf(self, otherClass):
        c = self.superClass
        while c:
            if c == otherClass:
                return True
            c = c.superClass

        return False

    def isImplements(self, iface):
        c = self
        while c:
            for interface in c.interfaces:
                if interface == iface or interface.isSubInterfaceOf(iface):
                    return True

        return False

    def isSubInterfaceOf(self, iface):
        for superInterface in self.interfaces:
            if superInterface == iface or superInterface.isSubInterfaceOf(iface):
                return True

        return False

    def getMainMethod(self):
        return self.getStaticMethod("main", "([Ljava/lang/String;)V")

    def getStaticMethod(self, name, descriptor):
        for m in self.methods:
            if m.isStatic() and m.name == "main" and m.descriptor == "([Ljava/lang/String;)V":
                return m
        return None

    def newObject(self):
        from ch06.rtda.heap.Object import Object

        return Object.newObject(self)