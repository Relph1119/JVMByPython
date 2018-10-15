import os
from ch02.classpath.ZipEntry import ZipEntry
from ch02.classpath.CompositeEntry import CompositeEntry

class WildcardEntry(CompositeEntry):
    def __init__(self, path):
        baseDir = path[:-1]
        for root, dirs, files in os.walk(baseDir):
            for name in files:
                if name.endswith(".jar") or name.endswith(".JAR"):
                    jarEntry = ZipEntry(os.path.join(root, name))
                    self.compositeEntryList.append(jarEntry)




