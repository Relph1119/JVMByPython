class MethodDescriptor():
    def __init__(self):
        self.parameterTypes = []
        self.returnType = ""

    def addParameterType(self, t):
        self.parameterTypes.append(t)