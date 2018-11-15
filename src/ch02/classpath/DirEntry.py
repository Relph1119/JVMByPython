from ch02.classpath.Entry import Entry
import os

class DirEntry(Entry):
    def __init__(self, path):
        self.absDir = os.path.abspath(path)

    def readClass(self,className):
        fileName = os.path.join(self.absDir, className)
        data, error = None, None
        try:
            data = open(fileName, "rb").read()
        except IOError as e:
            error = e
        return data, self, error

    def __str__(self):
        return self.absDir