class SymRef():
    def __init__(self):
        self.cp = None
        self.className = ""
        self._class = None

    def getClass(self):
        return self._class

    def resolveClass(self):
        if not self.getClass():
            self.resolveClassRef()

        return self.getClass()

    def resolveClassRef(self):
        d = self.cp.getClass()
        c = d.loader.loadClass(self.className)
        if not c.isAccessibleTo(d):
            raise RuntimeError("java.lang.IllegalAccessError")
        self._class = c
