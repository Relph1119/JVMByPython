from ch07.rtda.heap.CpMemberRef import MemberRef

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