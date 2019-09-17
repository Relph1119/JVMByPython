from optparse import OptionParser
from ch08.Cmd import Cmd
from ch08.classpath.Classpath import Classpath
from ch08.Interpreter import Interpreter

def main():
    parser = OptionParser(usage="%prog [-options] class [args...]")

    parser.add_option("-v", "--version", action="store_true", default=False, dest="version_flag", help="print version and exit.")
    parser.add_option("--verbose", action="store_true", default=False, dest="verbose_class_flag", help="enable verbose output")
    parser.add_option("--verbose:class", action="store_true", default=False, dest="verbose_class_flag", help="enable verbose output")
    parser.add_option("--verbose:inst", action="store_true", default=False, dest="verbose_inst_flag", help="enable verbose output")
    parser.add_option("--cp", action="store", type="string", dest="cpOption", help="classpath")
    parser.add_option("--classpath", action="store", type="string", dest="cpOption", help="classpath")
    parser.add_option("--Xjre", action="store", type="string", dest="XjreOption", help="path to jre")

    (options, args) = parser.parse_args()
    if options:
        cmd = Cmd(options, args)
        startJVM(cmd)

def startJVM(cmd):
    from ch08.rtda.heap.ClassLoader import ClassLoader

    cp = Classpath().parse(cmd.XjreOption, cmd.cpOption)
    print("classpath:{0} class:{1} args:{2}".format(cp, cmd.class_name, cmd.args))

    classLoader = ClassLoader.newClassLoader(cp, cmd.verboseClassFlag)

    className = cmd.class_name.replace(".", "/")
    mainClass = classLoader.load_class(className)
    mainMethod = mainClass.get_main_method()

    if mainMethod:
        Interpreter.interpret(mainMethod, cmd.verboseInstFlag, cmd.args)
    else:
        print("Main method not found in class {0}".format(cmd.class_name))

def getMainMethod(classFile):
    for m in classFile.methods:
        if m.name() == "main" and m.descriptor() == "([Ljava/lang/String;)V":
            return m
    return None

main()

