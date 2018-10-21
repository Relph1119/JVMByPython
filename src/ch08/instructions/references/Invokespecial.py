from ch08.instructions.base.Instruction import Index16Instruction

class INVOKE_SPECIAL(Index16Instruction):
    def execute(self, frame):

        from ch08.rtda.heap.MethodLookup import MethodLookup
        from ch08.instructions.base.MethodInvokeLogic import MethodInvokeLogic


        currentClass = frame.method.getClass()
        cp = currentClass.constantPool
        methodRef = cp.getConstant(self.index)
        resolvedClass = methodRef.resolvedClass()
        resolvedMethod = methodRef.resolvedMethod()

        if resolvedMethod.name == "<init>" and resolvedMethod.getClass() != resolvedClass:
            raise RuntimeError("java.lang.NoSuchMethodError")
        if resolvedMethod.isStatic():
            raise RuntimeError("java.lang.IncompatibleClassChangeError")

        ref = frame.operandStack.getRefFromTop(resolvedMethod.argSlotCount - 1)
        if not ref:
            raise RuntimeError("java.lang.NullPointerException")

        if resolvedMethod.isProtected() and resolvedMethod.getClass().isSuperClassOf(currentClass) \
                and resolvedMethod.getClass().getPackageName() != currentClass.getPackageName() \
                and ref.getClass() != currentClass and not ref.getClass().isSubClassOf(currentClass):
            raise RuntimeError("java.lang.IllegalAccessError")

        methodToBeInvoked = resolvedMethod
        if currentClass.isSuper() and resolvedClass.isSuperClassOf(currentClass) \
            and resolvedMethod.name != "<init>":
            methodToBeInvoked = MethodLookup.lookupMethodInClass(
                currentClass.superClass, methodRef.name, methodRef.descriptor)

        if not methodToBeInvoked or methodToBeInvoked.isAbstract():
            raise RuntimeError("java.lang.AbstractMethodError")

        MethodInvokeLogic.invokeMethod(frame, methodToBeInvoked)
    