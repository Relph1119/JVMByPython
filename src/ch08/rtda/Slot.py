class Slot:
    def __init__(self, num=0, ref=None):
        self.num = num
        self.ref = ref

    def __str__(self):
        return "num:{0} ref:{1}".format(self.num, self.ref)
