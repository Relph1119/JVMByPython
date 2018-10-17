from ch05.classpath.Entry import Entry

class CompositeEntry(Entry):

    compositeEntryList = []

    def __init__(self, pathList):
        for _, path in pathList.split(Entry.pathListSeparator):
            entry = Entry.newEntry(path)
            self.compositeEntryList.append(entry)

    def readClass(self,className):
        for entry in self.compositeEntryList:
            data, fromEntry = entry.readClass(className)
            if data:
                return data, fromEntry, None
        return None, None, "class not found:{0}".format(className)

    def __str__(self):
        return Entry.pathListSeparator.join(str(entry) for entry in self.compositeEntryList)