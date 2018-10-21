class ClassNameHelper():

    primitiveTypes = {
        "void" : "V",
        "boolean" : "Z",
        "byte" : "B",
        "short" : "S",
        "int" : "I",
        "long" : "J",
        "char" : "C",
        "float" : "F",
        "double" : "D"
    }

    @staticmethod
    def getArrayClassName(className):
        return "[" + ClassNameHelper.toDescriptor(className)

    @staticmethod
    def toDescriptor(className):
        if className[0] == '[':
            return className

        d = ClassNameHelper.primitiveTypes.get(className)
        if d:
            return d

        return "L" + className + ";"

    @staticmethod
    def toClassName(descriptor):
        if descriptor[0] == '[':
            return descriptor
        if descriptor[0] == 'L':
            return descriptor[1 : len(descriptor) - 1]
        for className, d in ClassNameHelper.primitiveTypes:
            if d == descriptor:
                return className

        raise RuntimeError("Invalid descriptor: " + descriptor)