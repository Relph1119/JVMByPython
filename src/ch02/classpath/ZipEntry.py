from ch02.classpath.Entry import Entry
import os.path
import zipfile

class ZipEntry(Entry):
    def __init__(self, path):
        self.absDir = os.path.abspath(path)

    def __str__(self):
        return self.absDir

    def readClass(self, className):
        error, data = None, None
        with zipfile.ZipFile(self.absDir, 'r') as z:
            for file in z.filelist:
                if file.filename == className:
                    try:
                        data = z.open(file, 'r').read()
                        data = [hex(d) for d in data]
                    except Exception as e:
                        error = e
                        return None, None, error
                    break
        if not data:
            error = "class not found:{0}".format(className)
            return None, None, error
        return data, self, error
