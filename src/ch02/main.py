from optparse import OptionParser
from ch02.Cmd import Cmd
from ch02.classpath.Classpath import Classpath

def main():
    parser = OptionParser(usage="%prog [-options] class [args...]")

    parser.add_option("-v", "--version", action="store_true", default=False, dest="versionFlag", help="print version and exit.")
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
    classData, _ = cp.readClass(className)

    print("class data:{0}".format([int(hex(data), 16) for data in classData]))

main()

