#读取字节的类
class ClassReader():
    def __init__(self, classData):
        self.data = classData

    def readUnit8(self):
        val = self.data[:1]
        self.data = self.data[1:]
        return val

    def readUnit16(self):
        val = self.data[:2]
        self.data = self.data[2:]
        return val

    def readUnit32(self):
        val = self.data[:4]
        self.data = self.data[4:]
        return val

    def readUnit64(self):
        val = self.data[:8]
        self.data = self.data[8:]
        return val

    def readUnit16s(self):
        n = int.from_bytes(self.readUnit16(), byteorder = 'big')
        s = []
        for i in range(n):
            s.append(int.from_bytes(self.readUnit16(), byteorder = 'big'))
        return s

    def readBytes(self, n):
        bytes = self.data[:n]
        self.data = self.data[n:]
        return bytearray(bytes)