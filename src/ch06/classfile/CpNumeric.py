from ch06.classfile.ConstantInfo import ConstantInfo
import ctypes

class ConstantIntgerInfo(ConstantInfo):
    def __init__(self):
        self.val = 0

    def readInfo(self, classReader):
        bytes = int.from_bytes(classReader.read_unit32(), byteorder='big')
        self.val = ctypes.c_int32(bytes).value

class ConstantFloatInfo(ConstantInfo):
    def __init__(self):
        self.val = 0.0

    def readInfo(self, classReader):
        bytes = int.from_bytes(classReader.read_unit32(), byteorder='big')
        self.val = ctypes.c_float(bytes).value

class ConstantLongInfo(ConstantInfo):
    def __init__(self):
        self.val = 0

    def readInfo(self, classReader):
        bytes = int.from_bytes(classReader.read_unit64(), byteorder='big')
        self.val = ctypes.c_int64(bytes).value

class ConstantDoubleInfo(ConstantInfo):
    def __init__(self):
        self.val = 0.0

    def readInfo(self, classReader):
        bytes = int.from_bytes(classReader.read_unit64(), byteorder='big')
        self.val = ctypes.c_float(bytes).value

