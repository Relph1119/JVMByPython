from optparse import OptionParser
from ch03.Cmd import Cmd
from ch03.classpath.Classpath import Classpath
from ch03.classfile.ClassFile import ClassFile

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
    print(cmd.className)
    printClassInfo(cf)

def loadClass(className, classPath):
    classData, _ = classPath.read_class(className)

    classfile = ClassFile(classData)
    cf = classfile.parse()
    return cf

def printClassInfo(cf):
    print("version: {0}.{1}".format(cf.majorVersion, cf.minorVersion))
    print("constants count: {0}".format(len(cf.constantPool.cp)))
    print("access flags: {0}".format(hex(int.from_bytes(cf.accessFlags, byteorder="big"))))
    print("this class: {0}".format(cf.className()))
    print("super class: {0}".format(cf.superClassName()))
    print("interfaces: {0}".format(cf.interfaceNames()))
    print("fields count: {0}".format(len(cf.fields)))
    for f in cf.fields:
        print("   {0}".format(f.name()))
    print("methods count: {0}".format(len(cf.methods)))
    for m in cf.methods:
        print("   {0}".format(m.name()))

main()

