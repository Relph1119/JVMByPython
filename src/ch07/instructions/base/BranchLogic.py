class BranchLogic():

    @staticmethod
    def branch(frame, offset):
        pc = frame.thread.pc
        nextPC = pc + offset
        frame.nextPC = nextPC