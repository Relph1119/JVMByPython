from optparse import OptionParser
from ch04.Cmd import Cmd
from ch04.rtda.Frame import Frame

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
   frame = Frame(100, 100)
   testLocalVars(frame.localVars)
   testOperandStack(frame.operandStack)

def testLocalVars(vars):
    vars.setNumeric(0, 100)
    vars.setNumeric(1, -100)
    vars.setNumeric(2, 2997924580)
    vars.setNumeric(3, -2997924580)
    vars.setNumeric(4, 3.1415926)
    vars.setNumeric(5, 2.71828182845)
    vars.setRef(6, None)
    print(vars.getNumeric(0))
    print(vars.getNumeric(1))
    print(vars.getNumeric(2))
    print(vars.getNumeric(3))
    print(vars.getNumeric(4))
    print(vars.getNumeric(5))
    print(vars.getRef(6))

def testOperandStack(ops):
    ops.pushNumeric(100)
    ops.pushNumeric(-100)
    ops.pushNumeric(2997924580)
    ops.pushNumeric(-2997924580)
    ops.pushNumeric(3.1415926)
    ops.pushNumeric(2.71828182845)
    ops.pushRef(None)
    print(ops.popRef())
    print(ops.popNumeric())
    print(ops.popNumeric())
    print(ops.popNumeric())
    print(ops.popNumeric())
    print(ops.popNumeric())
    print(ops.popNumeric())

main()

