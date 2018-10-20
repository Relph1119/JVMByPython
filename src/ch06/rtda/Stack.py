class Stack():
    def __init__(self, maxSize):
        self.maxSize = maxSize
        self.size = 0
        self._top = 0

    def push(self, frame):
        if self.size >= self.maxSize:
            raise RuntimeError("java.lang.StackOverflowError")
        if self._top:
            frame.lower = self._top
        self._top = frame
        self.size += 1

    def pop(self):
        if not self._top:
            raise RuntimeError("jvm stack is empty!")

        top = self._top
        self._top = top.lower
        top.lower = None
        self.size -= 1

        return top

    def top(self):
        if not self._top:
            raise RuntimeError("jvm stack is empty!")
        return self._top