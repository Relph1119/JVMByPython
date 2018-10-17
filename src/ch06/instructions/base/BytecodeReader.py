import struct
import ctypes

class BytecodeReader():
    def __init__(self):
        self.code = []
        self.pc = 0

    def reset(self, code, pc):
        self.code = code
        self.pc = pc

    def readUint8(self):
        i = self.code[self.pc]
        self.pc += 1
        return ctypes.c_uint8(i).value

    def readInt8(self):
        i = self.code[self.pc]
        self.pc += 1
        return ctypes.c_int8(i).value

    def readUint16(self):
        byte1 = self.readUint8()
        byte2 = self.readUint8()
        return (byte1 << 8) | byte2

    def readInt16(self):
        return ctypes.c_int16(self.readUint16()).value

    def readInt32(self):
        byte1 = self.readUint8()
        byte2 = self.readUint8()
        byte3 = self.readUint8()
        byte4 = self.readUint8()
        return ctypes.c_int32((byte1 << 24) | (byte2 << 16) | (byte3 << 8) | byte4).value

    def skipPadding(self):
        while self.pc % 4 != 0:
            self.readUint8()

    def readInt32s(self, n):
        ints = []
        for i in range(n):
            ints.append(self.readInt32())
        return ints


