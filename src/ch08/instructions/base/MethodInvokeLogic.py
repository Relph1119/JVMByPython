class MethodInvokeLogic():

    @staticmethod
    def invokeMethod(invokerFrame, method):
        thread = invokerFrame.thread
        newFrame = thread.newFrame(method)
        thread.push_frame(newFrame)

        argSlotSlot = method.argSlotCount
        if argSlotSlot > 0:
            for i in range(argSlotSlot-1, -1, -1):
                slot = invokerFrame.operandStack.pop_slot()
                newFrame.localVars.set_slot(i, slot)

        if method.is_native():
            if method.name == "registerNatives":
                thread.pop_frame()
            else:
                raise RuntimeError("native method: {0}.{1}{2}".format(method.get_class().name, method.name, method.descriptor))
