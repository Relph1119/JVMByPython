from ch08.instructions.base.Instruction import Index16Instruction
from ch08.rtda.heap.StringPool import StringPool

def _println(stack, descriptor):
    if descriptor == "(Z)V":
        print("{0}".format(stack.popNumeric() != 0))
    elif descriptor in {"(C)V", "(B)V", "(S)V", "(I)V", "(J)V", "(F)V", "(D)V"}:
        print("{0}".format(stack.popNumeric()))
    elif descriptor == "(Ljava/lang/String;)V":
        jStr = stack.popRef()
        goStr = StringPool.goString(jStr)
        print("{0}".format(goStr))
    else:
        raise RuntimeError("println: " + descriptor)
    stack.popRef()

class INVOKE_VIRTURL(Index16Instruction):
    def execute(self, frame):
        from ch08.rtda.heap.MethodLookup import MethodLookup
        from ch08.instructions.base.MethodInvokeLogic import MethodInvokeLogic

        currentClass = frame.method.getClass()
        cp = currentClass.constantPool
        methodRef = cp.getConstant(self.index)
        resolvedMethod = methodRef.resolvedMethod()
        if resolvedMethod.isStatic():
            raise RuntimeError("java.lang.IncompatibleClassChangeError")

        ref = frame.operandStack.getRefFromTop(resolvedMethod.argSlotCount - 1)
        if not ref:
            if methodRef.name == "println":
                _println(frame.operandStack, methodRef.descriptor)
                return
            raise RuntimeError("java.lang.NullPointerException")

        if resolvedMethod.isProtected() \
                and resolvedMethod.getClass().isSuperClassOf(currentClass) \
                and resolvedMethod.getClass().getPackageName() != currentClass.getPackageName() \
                and ref.getClass() != currentClass \
                and not ref.getClass().isSubClassOf(currentClass):
            raise RuntimeError("java.lang.IllegalAccessError")

        methodToBeInvoked = MethodLookup.lookupMethodInClass(
            ref.getClass(), methodRef.name, methodRef.descriptor)
        if not methodToBeInvoked or methodToBeInvoked.isAbstract():
            raise RuntimeError("java.lang.AbstractMethodError")

        MethodInvokeLogic.invokeMethod(frame, methodToBeInvoked)





