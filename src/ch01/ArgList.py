class ArgList:
    def __init__(self, args):
        self.args = args

    def __str__(self):
        buf = ""
        for i in range(len(self.args)):
            buf += self.args[i]
            if i < len(self.args):
                buf += " "
        return buf
