from ch08.rtda.Slot import Slot

class OperandStack():
    def __init__(self, maxStack):
        self.slots = []
        if maxStack > 0:
            self.slots = [Slot() for i in range(maxStack)]
        self.size = 0

    def pushNumeric(self, val):
        self.slots[self.size].num = val
        self.size += 1

    def popNumeric(self):
        self.size -= 1
        return self.slots[self.size].num

    def pushRef(self, ref):
        self.slots[self.size].ref = ref
        self.size += 1

    def popRef(self):
        self.size -= 1
        ref = self.slots[self.size].ref
        self.slots[self.size].ref = None
        return ref

    def pushSlot(self, slot):
        self.slots[self.size] = slot
        self.size += 1

    def popSlot(self):
        self.size -= 1
        return self.slots[self.size]

    def getRefFromTop(self, n):
        return self.slots[self.size - 1 - n].ref

    def __str__(self):
        return "size:{0} slots:{1}".format(self.size, [str(t) for t in self.slots])