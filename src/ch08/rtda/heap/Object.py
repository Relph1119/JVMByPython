from ch08.rtda.LocalVars import LocalVars

class Object():
    def __init__(self, clazz=None, count=0):
        self._class = clazz
        self.data = [0 for i in range(count)]

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
        return self.data

    def bytes(self):
        return self.data

    def shorts(self):
        return self.data

    def ints(self):
        return self.data

    def longs(self):
        return self.data

    def chars(self):
        return self.data

    def floats(self):
        return self.data

    def doubles(self):
        return self.data

    def refs(self):
        return self.data

    def arrayLength(self):
        return len(self.data)

    def setDataSlotsValueByIndex(self, index, value):
        self.data[index] = value


