from ch06.rtda.Thread import Thread

class Interpreter():

    @staticmethod
    def interpret(method):
        thread = Thread()
        frame = thread.newFrame(method)
        thread.pushFrame(frame)
        try:
            Interpreter.loop(thread, method.code)
        except RuntimeError as e:
            print("LocalVars: {0}".format(frame.localVars))
            print("OperandStack: {0}".format(frame.operandStack))
            print(e)


    @staticmethod
    def loop(thread, bytecode):
        from ch06.instructions.base.BytecodeReader import BytecodeReader
        from ch06.instructions.Factory import Factory

        frame = thread.popFrame()
        reader = BytecodeReader()

        while True:
            pc = frame.nextPC
            thread.pc = pc

            reader.reset(bytecode, pc)
            opcode = reader.readUint8()
            inst = Factory.newInstruction(opcode)
            inst.fetchOperands(reader)
            frame.nextPC = reader.pc

            print("pc:{0} opcode:{1} inst:{2} [{3}]".format(pc, hex(opcode), inst.__class__.__name__ ,Interpreter.prn_obj(inst)))
            inst.execute(frame)

    @staticmethod
    def prn_obj(obj):
        return ' '.join(['%s:%s' % item for item in obj.__dict__.items()])
