from abc import ABCMeta, abstractstaticmethod

class Entry(metaclass=ABCMeta):
    pathListSeparator = ";"

    @abstractstaticmethod
    def readClass(self,className):
        pass

    @staticmethod
    def newEntry(path):
        from ch02.classpath.CompositeEntry import CompositeEntry
        from ch02.classpath.WildcardEntry import WildcardEntry
        from ch02.classpath.ZipEntry import ZipEntry
        from ch02.classpath.DirEntry import DirEntry
        if Entry.pathListSeparator in path:
            return CompositeEntry.newCompositeEntry(path)
        elif path.endswith("*"):
            return WildcardEntry.newWildcardEntry(path)
        elif path.endswith(".jar") or path.endswith(".JAR") or path.endswith(".zip") or path.endswith(".ZIP"):
            return ZipEntry(path)
        else:
            return DirEntry(path)
