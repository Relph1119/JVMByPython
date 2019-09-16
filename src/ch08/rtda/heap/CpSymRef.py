class SymRef():
    def __init__(self):
        self.cp = None
        self.className = ""
        self._class = None

    def getClass(self):
        return self._class

    def resolvedClass(self):
        if not self.getClass():
            self.resolveClassRef()

        return self.getClass()

    def resolveClassRef(self):
        d = self.cp.get_class()
        c = d.loader.load_class(self.className)
        if not c.is_accessible_to(d):
            raise RuntimeError("java.lang.IllegalAccessError")
        self._class = c
