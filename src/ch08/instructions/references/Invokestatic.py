from ch08.instructions.base.Instruction import Index16Instruction
from ch08.instructions.base.MethodInvokeLogic import MethodInvokeLogic

class INVOKE_STATIC(Index16Instruction):
    def execute(self, frame):
        from ch08.instructions.base.ClassInitLogic import ClassInitLogic

        cp = frame.method.get_class().constantPool
        methodRef = cp.get_constant(self.index)
        resolvedMethod = methodRef.resolved_method()
        if not resolvedMethod.is_static():
            raise RuntimeError("java.lang.IncompatibleClassChangeError")

        clazz = resolvedMethod.get_class()
        if not clazz.initStarted:
            frame.revert_next_pc()
            ClassInitLogic.initClass(frame.thread, clazz)
            return

        MethodInvokeLogic.invokeMethod(frame, resolvedMethod)
