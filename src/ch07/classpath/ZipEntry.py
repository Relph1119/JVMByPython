from ch07.classpath.Entry import Entry
import os.path
import zipfile

class ZipEntry(Entry):
    def __init__(self, path):
        self.absDir = os.path.abspath(path)

    def __str__(self):
        return self.absDir

    def readClass(self, className):
        data = None
        with zipfile.ZipFile(self.absDir, 'r') as z:
            for file in z.filelist:
                if file.filename == className:
                    data = z.open(file, 'r').read()
                    break

        return data, self
