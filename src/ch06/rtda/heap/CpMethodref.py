from ch06.rtda.heap.CpMemberRef import MemberRef

class MethodRef(MemberRef):
    def __init__(self):
        super(MethodRef, self).__init__()
        self.method = None

    @staticmethod
    def newMethodRef(constantPool, refInfo):
        ref = MemberRef()
        ref.cp = constantPool
        ref.copyMemberRefInfo(refInfo)
        return ref