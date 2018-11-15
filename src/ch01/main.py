from optparse import OptionParser
from ch01.Cmd import Cmd

def main():
    parser = OptionParser(usage="%prog [-options] class [args...]")

    parser.add_option("-v", "--version", action="store_true", default=False, dest="versionFlag", help="print version and exit.")
    parser.add_option("--cp", action="store", type="string", dest="cpOption", help="classpath")
    parser.add_option("--classpath", action="store", type="string", dest="cpOption", help="classpath")
    (options, args) = parser.parse_args()
    if options:
        cmd = Cmd(options, args)
        cmd.printClasspath()

main()



