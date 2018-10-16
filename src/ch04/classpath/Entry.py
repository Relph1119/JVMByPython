from abc import ABCMeta, abstractstaticmethod

class Entry(metaclass=ABCMeta):
    pathListSeparator = ";"

    @abstractstaticmethod
    def readClass(self,className):
        pass

    def newEntry(path):
        from ch04.classpath.CompositeEntry import CompositeEntry
        from ch04.classpath.WildcardEntry import WildcardEntry
        from ch04.classpath.ZipEntry import ZipEntry
        from ch04.classpath.DirEntry import DirEntry
        if Entry.pathListSeparator in path:
            return CompositeEntry(path)
        elif path.endswith("*"):
            return WildcardEntry(path)
        elif path.endswith(".jar") or path.endswith(".JAR") or path.endswith(".zip") or path.endswith(".ZIP"):
            return ZipEntry(path)
        else:
            return DirEntry(path)
