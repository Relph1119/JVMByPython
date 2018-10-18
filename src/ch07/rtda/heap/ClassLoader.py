class ClassLoader():
    def __init__(self):
        self.cp = None
        self.classMap = None

    @staticmethod
    def newClassLoader(classPath):
        classLoader = ClassLoader()
        classLoader.cp = classPath
        classLoader.classMap = dict()
        return classLoader

    def loadClass(self, name):
        clazz = self.classMap.get(name)
        if clazz:
            return clazz
        else:
            return self.loadNonArrayClass(name)

    def loadNonArrayClass(self, name):
        data, entry = self.readClass(name)
        clazz = self.defineClass(data)
        ClassLoader.link(clazz)
        print("[Loaded {0} from {1}]".format(name, entry))
        return clazz

    def readClass(self, name):
        data, entry, error = self.cp.readClass(name)
        if error:
            raise RuntimeError("java.lang.ClassNotFoundException: " + name)
        return data, entry

    def defineClass(self, data):
        clazz = ClassLoader.parseClass(data)
        clazz.loader = self
        ClassLoader.resolveSuperClass(clazz)
        ClassLoader.resolveInterfaces(clazz)
        self.classMap[clazz.name] = clazz
        return clazz

    @staticmethod
    def parseClass(data):
        from ch07.classfile.ClassFile import ClassFile
        from ch07.rtda.heap.Class import Class

        classfile = ClassFile(data)
        cf, err = classfile.parse()
        if err:
            raise RuntimeError("java.lang.ClassFormatError!")
        else:
            return Class.newClass(cf)

    @staticmethod
    def resolveSuperClass(clazz):
        if clazz.name != "java/lang/object" and clazz.superClassName:
            clazz.superClass = clazz.loader.loadClass(clazz.superClassName)

    @staticmethod
    def resolveInterfaces(clazz):
        interfaceCount = len(clazz.interfaceNames)
        if interfaceCount > 0:
            for interfaceName in clazz.interfaceNames:
                clazz.interfaces.append(clazz.loader.loadClass(interfaceName))

    @staticmethod
    def link(clazz):
        ClassLoader.verify(clazz)
        ClassLoader.prepare(clazz)

    @staticmethod
    def verify(clazz):
        pass

    @staticmethod
    def prepare(clazz):
        ClassLoader.calcInstantceFieldSlotIds(clazz)
        ClassLoader.calcStaticFieldSlotIds(clazz)
        ClassLoader.allocAndInitStaticVars(clazz)

    @staticmethod
    def calcInstantceFieldSlotIds(clazz):
        slotId = 0
        if clazz.superClass:
            slotId = clazz.superClass.instanceSlotCount
        for field in clazz.fields:
            if not field.isStatic():
                field.slotId = slotId
                slotId += 1
                ##不需要判断long和double，每一个slot可设置为一个对象

        clazz.instanceSlotCount = slotId

    @staticmethod
    def calcStaticFieldSlotIds(clazz):
        slotId = 0
        for field in clazz.fields:
            if field.isStatic():
                field.slotId = slotId
                slotId += 1

        clazz.staticSlotCount = slotId

    @staticmethod
    def allocAndInitStaticVars(clazz):
        from ch07.rtda.LocalVars import LocalVars

        clazz.staticVars = LocalVars(clazz.staticSlotCount)
        for field in clazz.fields:
            if field.isStatic() and field.isFinal():
                ClassLoader.initStaticFinalVar(clazz, field)

    @staticmethod
    def initStaticFinalVar(clazz, field):
        vars = clazz.staticVars
        cp = clazz.constantPool
        cpIndex = field.constValueIndex
        slotId = field.slotId

        if cpIndex > 0:
            if field.descriptor in {"Z", "B", "C", "S", "I","J", "F", "D"}:
                val = cp.getConstant(cpIndex)
                vars.setNumeric(slotId, val)
            elif field.descriptor == "Ljava/lang/String":
                raise RuntimeError("todo")



