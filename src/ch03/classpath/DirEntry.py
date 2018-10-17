from ch03.classpath.Entry import Entry
import os

class DirEntry(Entry):
    def __init__(self, path):
        self.absDir = os.path.abspath(path)

    def readClass(self,className):
        fileName = os.path.join(self.absDir, className)
        data = open(fileName, "rb").read()
        return data, self

    def __str__(self):
        return self.absDir