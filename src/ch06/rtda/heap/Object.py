class Object():
    def __init__(self):
        self._class = None
        self.fields = []

    def setClass(self, clazz):
        self._class = clazz

    def getClass(self):
        return self._class

    @staticmethod
    def newObject(clazz):
        from ch06.rtda.LocalVars import LocalVars

        obj = Object()
        obj._class = clazz
        obj.fields = LocalVars(clazz.instanceSlotCount)
        return obj

    def isInstanceOf(self, clazz):
        return clazz.isAssignableFrom(self._class)