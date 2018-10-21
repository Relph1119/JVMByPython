class Cmd():
    versionFlag = False
    verboseClassFlag = False
    verboseInstFlag = False
    cpOption = ""
    className = ""
    XjreOption = ""
    args = []

    def __init__(self, options, argvs):
        if options.versionFlag:
            self.__printVersion()
        if options.cpOption:
            self.cpOption = options.cpOption
        if options.XjreOption:
            self.XjreOption = options.XjreOption
        if options.verboseClassFlag:
            self.verboseClassFlag = options.verboseClassFlag
        if options.verboseInstFlag:
            self.verboseInstFlag = options.verboseInstFlag

        if argvs:
            self.className = argvs[0]
            self.args = argvs[1:] if argvs[1:] else []

    def __printVersion(self):
        print("version 0.0.1")

    def printClasspath(self):
        print("classpath:{0} class:{1} args:{2}\n".format(self.cpOption, self.className, " ".join(self.args)))