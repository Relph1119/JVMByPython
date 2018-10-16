from ch04.rtda.Slot import Slot

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
