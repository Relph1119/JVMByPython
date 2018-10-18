from ch07.rtda.heap.ClassMember import ClassMember

class Method(ClassMember):
    def __init__(self):
        super(Method, self).__init__()
        self.maxStack = 0
        self.maxLocals = 0
        self.code = []

    @staticmethod
    def newMethod(clazz, cfMethods):
        methods = []
        for cfMethod in cfMethods:
            method = Method()
            method.setClass(clazz)
            method.copyMemberInfo(cfMethod)
            method.copyAttributes(cfMethod)
            methods.append(method)
        return methods

    def copyAttributes(self, cfMethod):
        codeAttr = cfMethod.codeAttribute()
        if codeAttr:
            self.maxStack = codeAttr.maxStack
            self.maxLocals = codeAttr.maxLocals
            self.code = codeAttr.code

    
