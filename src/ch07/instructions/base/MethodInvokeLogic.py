class MethodInvokeLogic():

    @staticmethod
    def invokeMethod(invokerFrame, method):
        thread = invokerFrame.thread
        newFrame = thread.newFrame(method)
        thread.pushFrame(newFrame)

        argSlotSlot = method.argSlotCount
        if argSlotSlot > 0:
            for i in range(argSlotSlot-1, -1, -1):
                slot = invokerFrame.operandStack.popSlot()
                newFrame.localVars.setSlot(i, slot)

        if method.isNative():
            if method.name == "registerNatives":
                thread.popFrame()
            else:
                raise RuntimeError("native method: {0}.{1}{2}".format(method.getClass().name, method.name, method.descriptor))
