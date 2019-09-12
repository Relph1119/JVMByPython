from optparse import OptionParser
from ch05.Cmd import Cmd
from ch05.classpath.Classpath import Classpath
from ch05.classfile.ClassFile import ClassFile
from ch05.Interpreter import Interpreter

def main():
    parser = OptionParser(usage="%prog [-options] class [args...]")

    parser.add_option("-v", "--version", action="store_true", default=False, dest="version_flag", help="print version and exit.")
    parser.add_option("--cp", action="store", type="string", dest="cpOption", help="classpath")
    parser.add_option("--classpath", action="store", type="string", dest="cpOption", help="classpath")
    parser.add_option("--Xjre", action="store", type="string", dest="XjreOption", help="path to jre")
    (options, args) = parser.parse_args()
    if options:
        cmd = Cmd(options, args)

    startJVM(cmd)

def startJVM(cmd):
    cp = Classpath().parse(cmd.XjreOption, cmd.cpOption)
    print("classpath:{0} class:{1} args:{2}".format(cp, cmd.className, cmd.args))

    className = cmd.className.replace(".", "/")
    cf = loadClass(className, cp)
    mainMethod = getMainMethod(cf)
    if mainMethod:
        Interpreter.interpret(mainMethod)
    else:
        print("Main method not found in class {0}".format(cmd.className))

def loadClass(className, classPath):
    classData, _ = classPath.read_class(className)

    classfile = ClassFile(classData)
    cf = classfile.parse()
    return cf

def getMainMethod(classFile):
    for m in classFile.methods:
        if m.name() == "main" and m.descriptor() == "([Ljava/lang/String;)V":
            return m
    return None

main()

