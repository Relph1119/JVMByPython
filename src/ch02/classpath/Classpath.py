import os.path
from ch02.classpath.WildcardEntry import WildcardEntry
from ch02.classpath.Entry import Entry

class Classpath:
    def __init__(self):
        self.bootClasspath = None
        self.extClassPath = None
        self.userClasspath = None

    @staticmethod
    def parse(jreOption, cpOption):
        cp = Classpath()
        cp.parse_boot_and_ext_classpath(jreOption)
        cp.parse_user_classpath(cpOption)
        return cp

    def parse_boot_and_ext_classpath(self, jreOption):
        jreDir = self.__getJreDir(jreOption)

        jreLibPath = os.path.join(jreDir, "lib", "*")
        self.bootClasspath = WildcardEntry.newWildcardEntry(jreLibPath)

        jreExtPath = os.path.join(jreDir, "lib", "ext", "*")
        self.extClassPath = WildcardEntry.newWildcardEntry(jreExtPath)

    #得到Jre路径
    def __getJreDir(self, jreOption):
        if jreOption and self.__exists(jreOption):
            return jreOption
        if self.__exists("./jre"):
            return "./jre"
        jh = os.environ.get("JAVA_HOME")
        if jh:
            return os.path.join(jh, "jre")
        raise RuntimeError("Can not find jre folder!")

    ##判断路径是否存在
    def __exists(self, path):
        if os.path.isdir(path):
            return True
        else:
            return False

    def parse_user_classpath(self, cpOption):
        if not cpOption:
            cpOption = "."
        self.userClasspath = Entry.newEntry(cpOption)

    def readClass(self, className):
        className = className + ".class"
        if self.bootClasspath:
            data, entry, error = self.bootClasspath.readClass(className)
            return data, entry, error
        if self.extClassPath:
            data, entry, error = self.extClassPath.readClass(className)
            return data, entry, error
        return self.userClasspath.readClass(className)

    def __str__(self):
        return self.userClasspath.__str__()


