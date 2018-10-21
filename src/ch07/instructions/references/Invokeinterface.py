from ch07.instructions.base.Instruction import Instruction
import ctypes

class INVOKE_INTERFACE(Instruction):
    def __init__(self):
        self.index = 0

    def fetchOperands(self, bytecodeReader):
        self.index = ctypes.c_uint(bytecodeReader.readUint16()).value
        bytecodeReader.readUint8()
        bytecodeReader.readUint8()

    def execute(self, frame):
        from ch07.rtda.heap.MethodLookup import MethodLookup
        from ch07.instructions.base.MethodInvokeLogic import MethodInvokeLogic

        cp = frame.method.getClass().constantPool
        methodRef = cp.getConstant(self.index)
        resolveMethod = methodRef.resolvedInterfaceMethod()
        if resolveMethod.isStatic() or resolveMethod.isPrivate():
            raise RuntimeError("java.lang.IncompatibleClassChangeError")

        ref = frame.operandStack.getRefFromTop(resolveMethod.argSlotCount - 1)
        if not ref:
            raise RuntimeError("java.lang.NullPointerException")

        if not ref.getClass().isImplements(methodRef.resolvedClass()):
            raise RuntimeError("java.lang.IncompatibleClassChangeError")

        methodToBeInvoked = MethodLookup.lookupMethodInClass(
            ref.getClass(), methodRef.name, methodRef.descriptor)
        if not methodToBeInvoked or methodToBeInvoked.isAbstract():
            raise RuntimeError("java.lang.abstractMethodError")
        if not methodToBeInvoked.isPublic():
            raise RuntimeError("java.lang.IllegalAccessError")

        MethodInvokeLogic.invokeMethod(frame, methodToBeInvoked)


