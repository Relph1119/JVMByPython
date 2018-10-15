from ch01.ArgList import ArgList

class Cmd():

    versionFlag = False
    cpOption = ""
    className = ""
    args = []

    def __init__(self, options, args):
        if options.versionFlag:
            self.__printVersion()
        elif options.cpOption:
            self.cpOption = options.cpOption
            self.className = args[0]
            self.args = ArgList(args[1:]) if args[1:] else []
            self.__printClasspath()


    def __printVersion(self):
        print("version 0.0.1")

    def __printClasspath(self):
        print("classpath:{0} class:{1} args:{2}\n".format(self.cpOption, self.className, self.args))