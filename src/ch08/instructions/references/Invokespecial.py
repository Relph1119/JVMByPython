from ch08.instructions.base.Instruction import Index16Instruction

class INVOKE_SPECIAL(Index16Instruction):
    def execute(self, frame):

        from ch08.rtda.heap.MethodLookup import MethodLookup
        from ch08.instructions.base.MethodInvokeLogic import MethodInvokeLogic


        currentClass = frame.method.get_class()
        cp = currentClass.constantPool
        methodRef = cp.get_constant(self.index)
        resolvedClass = methodRef.resolvedClass()
        resolvedMethod = methodRef.resolvedMethod()

        if resolvedMethod.name == "<init>" and resolvedMethod.get_class() != resolvedClass:
            raise RuntimeError("java.lang.NoSuchMethodError")
        if resolvedMethod.is_static():
            raise RuntimeError("java.lang.IncompatibleClassChangeError")

        ref = frame.operandStack.getRefFromTop(resolvedMethod.argSlotCount - 1)
        if not ref:
            raise RuntimeError("java.lang.NullPointerException")

        if resolvedMethod.is_protected() and resolvedMethod.get_class().isSuperClassOf(currentClass) \
                and resolvedMethod.get_class().get_package_name() != currentClass.get_package_name() \
                and ref.get_class() != currentClass and not ref.get_class().is_sub_class_of(currentClass):
            raise RuntimeError("java.lang.IllegalAccessError")

        methodToBeInvoked = resolvedMethod
        if currentClass.is_super() and resolvedClass.isSuperClassOf(currentClass) \
            and resolvedMethod.name != "<init>":
            methodToBeInvoked = MethodLookup.lookupMethodInClass(
                currentClass.superClass, methodRef.name, methodRef.descriptor)

        if not methodToBeInvoked or methodToBeInvoked.is_abstract():
            raise RuntimeError("java.lang.AbstractMethodError")

        MethodInvokeLogic.invokeMethod(frame, methodToBeInvoked)
    