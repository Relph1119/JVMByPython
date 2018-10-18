from ch07.rtda.heap.CpSymRef import SymRef

class MemberRef(SymRef):
    def __init__(self):
        super(MemberRef, self).__init__()
        self.name = ""
        self.descriptor = ""

    def copyMemberRefInfo(self, refInfo):
        self.className = refInfo.className()
        self.name, self.descriptor = refInfo.nameAndDescrptor()

