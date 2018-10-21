from ch08.instructions.base.Instruction import Index16Instruction
from ch08.instructions.base.MethodInvokeLogic import MethodInvokeLogic

class INVOKE_STATIC(Index16Instruction):
    def execute(self, frame):
        from ch08.instructions.base.ClassInitLogic import ClassInitLogic

        cp = frame.method.getClass().constantPool
        methodRef = cp.getConstant(self.index)
        resolvedMethod = methodRef.resolvedMethod()
        if not resolvedMethod.isStatic():
            raise RuntimeError("java.lang.IncompatibleClassChangeError")

        clazz = resolvedMethod.getClass()
        if not clazz.initStarted:
            frame.revertNextPC()
            ClassInitLogic.initClass(frame.thread, clazz)
            return

        MethodInvokeLogic.invokeMethod(frame, resolvedMethod)
