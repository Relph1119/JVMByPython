from ch08.rtda.heap.MethodDescriptor import MethodDescriptor
import copy

class MethodDescriptorParser():
    def __init__(self):
        self.raw = ""
        self.offset = 0
        self.parsed = None

    def parseMethodDescriptor(descriptor):
        parser = MethodDescriptorParser()
        return parser.parse(descriptor)

    def parse(self, descriptor):
        self.raw = descriptor
        self.parsed = MethodDescriptor()
        self.startParams()
        self.parseParamTypes()
        self.endParams()
        self.parseReturnType()
        self.finish()
        return self.parsed

    def startParams(self):
        if self.readUint8() != '(':
            self.causePanic()

    def endParams(self):
        if self.readUint8() != ')':
            self.causePanic()

    def finish(self):
        if self.offset != len(self.raw):
            self.causePanic()

    def causePanic(self):
        raise RuntimeError("BAD descriptor: {0}".format(self.raw))

    def readUint8(self):
        b = self.raw[self.offset]
        self.offset += 1
        return b

    def unreadUint8(self):
        self.offset -= 1

    def parseParamTypes(self):
        while True:
            t = self.parseFieldType()
            if t:
                self.parsed.addParameterType(t)
            else:
                break

    def parseReturnType(self):
        if self.readUint8() == 'V':
            self.parsed.returnType = "V"
            return

        self.unreadUint8()
        t = self.parseFieldType()
        if t:
            self.parsed.returnType = t
            return

        self.causePanic()

    def parseFieldType(self):
        type = self.readUint8()
        if type == 'B':
            return 'B'
        elif type == 'C':
            return 'C'
        elif type == 'D':
            return 'D'
        elif type == 'F':
            return 'F'
        elif type == 'I':
            return 'I'
        elif type == 'J':
            return 'J'
        elif type == 'S':
            return 'S'
        elif type == 'Z':
            return 'Z'
        elif type == 'L':
            return self.parseObjectType()
        elif type == '[':
            return self.parseArrayType()
        else:
            self.unreadUint8()
            return ""

    def parseObjectType(self):
        unread = self.raw[self.offset:]
        semicolonIndex = unread.find(";")
        if semicolonIndex == -1:
            self.causePanic()
            return ""
        else:
            objStart = self.offset - 1
            objEnd = self.offset + semicolonIndex + 1
            self.offset = objEnd
            descriptor = copy.deepcopy(self.raw[objStart:objEnd])
            return descriptor

    def parseArrayType(self):
        arrStart = self.offset - 1
        self.parseFieldType()
        arrEnd = self.offset
        descriptor = copy.deepcopy(self.raw[arrStart:arrEnd])
        return descriptor
