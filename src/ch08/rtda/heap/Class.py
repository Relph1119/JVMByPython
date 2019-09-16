from ch08.rtda.heap.AccessFlags import AccessFlags

class Class:
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
        self.initStarted = False

    @staticmethod
    def newClass(classFile):
        from ch08.rtda.heap.ConstantPool import ConstantPool
        from ch08.rtda.heap.Field import Field
        from ch08.rtda.heap.Method import Method

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
        return self.isPublic() or self.getPackageName() == otherClass.get_package_name()

    def getPackageName(self):
        i = self.name.rfind("/")
        if i >= 0:
            return self.name[:i]
        return ""

    def isAssignableFrom(self, otherClass):
        s, t = otherClass, self
        if s == t:
            return True

        if not s.isArray():
            if not s.is_interface():
                if not t.isInterface():
                    return s.is_sub_class_of(t)
                else:
                    return s.is_implements(t)
            else:
                if not t.isInterface():
                    return t.isJlObject()
                else:
                    return t.isSuperInterfaceOf(s)
        else:
            if not t.isArray():
                if not t.isInterface():
                    return t.isJlObject()
                else:
                    return t.isJlCloneable() or t.isJioSerializable()
            else:
                sc = s.componentClass()
                tc = t.componentClass()
                return sc == tc or tc.is_assignable_from(sc)


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
                if interface == iface or interface.is_sub_interface_of(iface):
                    return True

        return False

    def isSubInterfaceOf(self, iface):
        for superInterface in self.interfaces:
            if superInterface == iface or superInterface.is_sub_interface_of(iface):
                return True

        return False

    def isSuperClassOf(self, otherClass):
        return otherClass.is_sub_class_of(self)

    def isSuperInterfaceOf(self, iface):
        return iface.is_sub_interface_of(self)

    def getMainMethod(self):
        return self.getStaticMethod("main", "([Ljava/lang/String;)V")

    def getStaticMethod(self, name, descriptor):
        for method in self.methods:
            if method.is_static() and method.name == name and  method.descriptor == descriptor:
                return method
        return None

    def newObject(self):
        from ch08.rtda.heap.Object import Object

        return Object.newObject(self)

    def startInit(self):
        self.initStarted = True

    def getClinitMethod(self):
        return self.getStaticMethod("<clinit>", "()V")

    ##数组Class
    def newArray(self, count):
        from ch08.rtda.heap.Object import Object
        if not self.isArray():
            raise RuntimeError("Not array class: " + self.name)
        return Object(self, count)

    def isArray(self):
        return self.name[0] == '['

    def isJlObject(self):
        return self.name == "java/lang/Object"

    def isJlCloneable(self):
        return self.name == "java/lang/Cloneable"

    def isJioSerializable(self):
        return self.name == "java/io/Serializable"

    def arrayClass(self):
        from ch08.rtda.heap.ClassNameHelper import ClassNameHelper

        arrayClassName = ClassNameHelper.getArrayClassName(self.name)
        return self.loader.load_class(arrayClassName)

    def componentClass(self):
        componentCLassName = Class.getComponentClassName(self.name)
        return self.loader.load_class(componentCLassName)

    @staticmethod
    def getComponentClassName(className):
        from ch08.rtda.heap.ClassNameHelper import ClassNameHelper

        if className[0] == '[':
            componentTypeDescriptor = className[1:]
            return ClassNameHelper.toClassName(componentTypeDescriptor)

    def getField(self, name, descriptor, isStatic):
        c = self
        while c:
            for field in c.fields:
                if field.is_static() == isStatic \
                        and field.name == name and field.descriptor == descriptor:
                    return field

            c = c.superClass
        return None