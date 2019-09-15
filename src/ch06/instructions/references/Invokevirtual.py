from ch06.instructions.base.Instruction import Index16Instruction

class INVOKE_VIRTURL(Index16Instruction):
    def execute(self, frame):
        cp = frame.method.getClass().constantPool
        methodRef = cp.getConstant(self.index)
        if methodRef.name == "println":
            stack = frame.operandStack
            descriptor = methodRef.descriptor
            if descriptor == "(Z)V":
                print("{0}".format(stack.pop_numeric() != 0))
            elif descriptor in {"(C)V", "(B)V", "(S)V", "(I)V", "(J)V", "(F)V", "(D)V"}:
                print("{0}".format(stack.pop_numeric()))
            else:
                raise RuntimeError("println: " + methodRef.descriptor)
            stack.pop_ref()
