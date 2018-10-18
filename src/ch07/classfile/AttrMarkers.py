from ch07.classfile.AttributeInfo import AttributeInfo

class MarkerAttribute(AttributeInfo):
    def __init__(self):
        pass

    def readInfo(self, classReader):
        pass

class DeprecatedAttribute(MarkerAttribute):
    def __init__(self):
        pass

class SyntheticAttribute(MarkerAttribute):
    def __init__(self):
        pass
