from ch08.classfile.ConstantInfo import ConstantInfo
import ctypes

class ConstantUtf8Info(ConstantInfo):
    def __init__(self):
        self.str = ""

    def readInfo(self, classReader):
        length = ctypes.c_uint32(int.from_bytes(classReader.read_unit16(), byteorder='big')).value
        if length == 0:
            self.str = ""
        else:
            bytes = classReader.read_bytes(length)
            self.str = self.decodeMUTF8(bytes)

    def decodeMUTF8(self, bytes):
        return bytes.decode()