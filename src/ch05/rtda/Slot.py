class Slot():
    def __init__(self):
        self.num = 0
        self.ref = None

    def __str__(self):
        return "num:{0} ref:{1}".format(self.num, self.ref)
