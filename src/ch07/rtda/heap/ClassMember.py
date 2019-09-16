from ch07.rtda.heap.AccessFlags import AccessFlags

class ClassMember():
    def __init__(self):
        self.accessFlags = 0
        self.name = ""
        self.descriptor = ""
        self._class = None

    def copyMemberInfo(self, memberInfo):
        self.accessFlags = memberInfo.accessFlags
        self.name = memberInfo.name()
        self.descriptor = memberInfo.descriptor()

    def setClass(self, clazz):
        self._class = clazz

    def getClass(self):
        return self._class

    def isPublic(self):
        return 0 != self.accessFlags & AccessFlags.ACC_PUBLIC

    def isPrivate(self):
        return 0 != self.accessFlags & AccessFlags.ACC_PRIVATE

    def isProtected(self):
        return 0 != self.accessFlags & AccessFlags.ACC_PROTECTED

    def isStatic(self):
        return 0 != self.accessFlags & AccessFlags.ACC_STATIC

    def isFinal(self):
        return 0 != self.accessFlags & AccessFlags.ACC_FINAL

    def isSynthetic(self):
        return 0 != self.accessFlags & AccessFlags.ACC_SYNTHETIC

    def isAccessibleTo(self, d):
        if self.isPublic():
            return True

        c = self._class
        if self.isProtected():
            return d == c or d.is_sub_class_of(c) or c.get_package_name() == d.get_package_name()

        if not self.isPrivate():
            return c.get_package_name() == d.get_package_name()

        return d == c