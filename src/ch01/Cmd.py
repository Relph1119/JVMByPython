from ch01.ArgList import ArgList

class Cmd():
    helpFlag = False
    versionFlag = False
    cpOption = ""
    className = ""
    args = []

    def __init__(self, argvs):
        if len(argvs) > 1:
            if argvs[1] in {"-help", "?"}:
                self.printUsage(argvs[0])
                self.helpFlag = True
            elif argvs[1] in {"-version", "-v"}:
                self.printVersion()
                self.versionFlag = True
            elif argvs[1] == "-cp":
                self.cpOption = argvs[2] if not argvs[2] else ""
                self.className = argvs[3] if not argvs[3] else ""
                self.args = ArgList(argvs[4:]) if not argvs[4] else []
                self.printClasspath()
        else:
            self.printUsage(argvs[0])

    def printUsage(self, argv):
        print("Usage:{0} [-options] class [args...]".format(argv))

    def printVersion(self):
        print("version 0.0.1")

    def printClasspath(self):
        print("classpath:{0} class:{1} args:{2}\n".format(self.cpOption, self.className, self.args))