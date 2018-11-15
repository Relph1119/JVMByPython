from ch08.rtda.LocalVars import LocalVars

class Object:
    def __init__(self, clazz=None, count=0):
        self._class = clazz
        self.data = LocalVars(count)

    def setClass(self, clazz):
        self._class = clazz

    def getClass(self):
        return self._class

    @staticmethod
    def newObject(clazz):
        obj = Object()
        obj._class = clazz
        obj.data = LocalVars(clazz.instanceSlotCount)
        return obj

    def isInstanceOf(self, clazz):
        return clazz.isAssignableFrom(self._class)

    def fields(self):
        return self.data.slots

    def bytes(self):
        return self.data.slots

    def shorts(self):
        return self.data.slots

    def ints(self):
        return self.data.slots

    def longs(self):
        return self.data.slots

    def chars(self):
        return self.data.slots

    def floats(self):
        return self.data.slots

    def doubles(self):
        return self.data.slots

    def refs(self):
        return self.data.slots

    def arrayLength(self):
        return len(self.data.slots)

    def setDataSlotsValueByIndex(self, index, value):
        self.data.slots[index] = value

    def setRefVar(self, name, descriptor, ref):
        field = self._class.getField(name, descriptor, False)
        slots = self.data
        slots.setRef(field.slotId, ref)

    def getRefVar(self, name, descriptor):
        field = self._class.getField(name, descriptor, False)
        slots = self.data
        return slots.getRef(field.slotId)

