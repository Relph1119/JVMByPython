from ch07.instructions.base.Instruction import Index16Instruction

def _println(stack, descriptor):
    if descriptor == "(Z)V":
        print("{0}".format(stack.pop_numeric() != 0))
    elif descriptor in {"(C)V", "(B)V", "(S)V", "(I)V", "(J)V", "(F)V", "(D)V"}:
        print("{0}".format(stack.pop_numeric()))
    else:
        raise RuntimeError("println: " + descriptor)
    stack.pop_ref()

class INVOKE_VIRTURL(Index16Instruction):
    def execute(self, frame):
        from ch07.rtda.heap.MethodLookup import MethodLookup
        from ch07.instructions.base.MethodInvokeLogic import MethodInvokeLogic

        currentClass = frame.method.get_class()
        cp = currentClass.constantPool
        methodRef = cp.get_constant(self.index)
        resolvedMethod = methodRef.resolvedMethod()
        if resolvedMethod.is_static():
            raise RuntimeError("java.lang.IncompatibleClassChangeError")

        ref = frame.operandStack.getRefFromTop(resolvedMethod.argSlotCount - 1)
        if not ref:
            if methodRef.name == "println":
                _println(frame.operandStack, methodRef.descriptor)
                return
            raise RuntimeError("java.lang.NullPointerException")

        if resolvedMethod.is_protected() \
                and resolvedMethod.get_class().isSuperClassOf(currentClass) \
                and resolvedMethod.get_class().get_package_name() != currentClass.get_package_name() \
                and ref.get_class() != currentClass \
                and not ref.get_class().is_sub_class_of(currentClass):
            raise RuntimeError("java.lang.IllegalAccessError")

        methodToBeInvoked = MethodLookup.lookupMethodInClass(
            ref.get_class(), methodRef.name, methodRef.descriptor)
        if not methodToBeInvoked or methodToBeInvoked.is_abstract():
            raise RuntimeError("java.lang.AbstractMethodError")

        MethodInvokeLogic.invokeMethod(frame, methodToBeInvoked)





