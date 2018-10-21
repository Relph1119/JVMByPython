from ch08.rtda.heap.ClassMember import ClassMember
from ch08.rtda.heap.MethodDescriptorParser import MethodDescriptorParser
from ch08.rtda.heap.AccessFlags import AccessFlags

class Method(ClassMember):
    def __init__(self):
        super(Method, self).__init__()
        self.maxStack = 0
        self.maxLocals = 0
        self.code = []
        self.argSlotCount = 0

    @staticmethod
    def newMethod(clazz, cfMethods):
        methods = []
        for cfMethod in cfMethods:
            method = Method()
            method.setClass(clazz)
            method.copyMemberInfo(cfMethod)
            method.copyAttributes(cfMethod)
            method.calcArgSlotCount()
            methods.append(method)
        return methods

    def copyAttributes(self, cfMethod):
        codeAttr = cfMethod.codeAttribute()
        if codeAttr:
            self.maxStack = codeAttr.maxStack
            self.maxLocals = codeAttr.maxLocals
            self.code = codeAttr.code

    def calcArgSlotCount(self):
        parsedDescriptor = MethodDescriptorParser.parseMethodDescriptor(self.descriptor)
        for paramType in parsedDescriptor.parameterTypes:
            self.argSlotCount += 1

        if not self.isStatic():
            self.argSlotCount += 1

    def isSynchronized(self):
        return 0 != self.accessFlags & AccessFlags.ACC_SYNCHRONIZED

    def isBridge(self):
        return 0 != self.accessFlags & AccessFlags.ACC_BRIDGE

    def isVarargs(self):
        return 0 != self.accessFlags & AccessFlags.ACC_VARARGS

    def isNative(self):
        return 0 != self.accessFlags & AccessFlags.ACC_NATIVE

    def isAbstract(self):
        return 0 != self.accessFlags & AccessFlags.ACC_ABSTRACT

    def isStrict(self):
        return 0 != self.accessFlags & AccessFlags.ACC_STRICT
