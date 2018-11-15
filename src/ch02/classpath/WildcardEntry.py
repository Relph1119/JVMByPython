import os
from ch02.classpath.ZipEntry import ZipEntry
from ch02.classpath.CompositeEntry import CompositeEntry

class WildcardEntry(CompositeEntry):

    @staticmethod
    def newWildcardEntry(path):
        baseDir = path[:-1]
        compositeEntry = CompositeEntry()
        for root, dirs, files in os.walk(baseDir):
            for name in files:
                if name.endswith(".jar") or name.endswith(".JAR"):
                    jarEntry = ZipEntry(os.path.join(root, name))
                    compositeEntry.compositeEntryList.append(jarEntry)
        return compositeEntry



