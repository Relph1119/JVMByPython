import os.path
from ch03.classpath.WildcardEntry import WildcardEntry
from ch03.classpath.Entry import Entry

class Classpath:
    def __init__(self):
        self.cpOption = None
        self.jreOption = None

    def parse(self, jreOption, cpOption):
        self.jreOption = jreOption
        self.cpOption = cpOption
        self.parse_boot_and_ext_classpath()
        self.parse_user_classpath()
        return self

    def parse_boot_and_ext_classpath(self):
        jreDir = self.__getJreDir()

        jreLibPath = os.path.join(jreDir, "lib", "*")
        self.bootClasspath = WildcardEntry(jreLibPath)

        jreExtPath = os.path.join(jreDir, "lib", "ext", "*")
        self.extClassPath = WildcardEntry(jreExtPath)

    #得到Jre路径
    def __getJreDir(self):
        if self.jreOption:
            return self.jreOption
        if self.__exists("./jre"):
            return "./jre"
        jr = os.environ.get("JAVA_HOME")
        if jr:
            return os.path.join(jr, "jre")
        raise RuntimeError("Can not find jre folder!")

    ##判断路径是否存在
    @staticmethod
    def __exists(self, path):
        if os.path.isdir(path):
            return True
        else:
            return False

    def parse_user_classpath(self):
        if not self.cpOption:
            self.cpOption = "."
        self.userClasspath = Entry.newEntry(self.cpOption)

    def readClass(self, className):
        className = className + ".class"
        if self.bootClasspath:
            data, entry, error = self.bootClasspath.readClass(className)
            if not error:
                return data, entry
        if self.extClassPath:
            data, entry, error = self.extClassPath.readClass(className)
            if not error:
                return data, entry
        return self.userClasspath.read_class(className)

    def __str__(self):
        return self.userClasspath.__str__()


