from ch08.instructions.base.Instruction import NoOperandsInstruction

class ACONST_NULL(NoOperandsInstruction):
    def execute(self, frame):
        frame.operandStack.pushRef(None)

class DCONST_0(NoOperandsInstruction):
    def execute(self, frame):
        frame.operandStack.pushNumeric(0.0)

class DCONST_1(NoOperandsInstruction):
    def execute(self, frame):
        frame.operandStack.pushNumeric(1.0)

class FCONST_0(NoOperandsInstruction):
    def execute(self, frame):
        frame.operandStack.pushNumeric(0.0)

class FCONST_1(NoOperandsInstruction):
    def execute(self, frame):
        frame.operandStack.pushNumeric(1.0)

class FCONST_2(NoOperandsInstruction):
    def execute(self, frame):
        frame.operandStack.pushNumeric(2.0)

class ICONST_M1(NoOperandsInstruction):
    def execute(self, frame):
        frame.operandStack.pushNumeric(-1)

class ICONST_0(NoOperandsInstruction):
    def execute(self, frame):
        frame.operandStack.pushNumeric(0)

class ICONST_1(NoOperandsInstruction):
    def execute(self, frame):
        frame.operandStack.pushNumeric(1)

class ICONST_2(NoOperandsInstruction):
    def execute(self, frame):
        frame.operandStack.pushNumeric(2)

class ICONST_3(NoOperandsInstruction):
    def execute(self, frame):
        frame.operandStack.pushNumeric(3)

class ICONST_4(NoOperandsInstruction):
    def execute(self, frame):
        frame.operandStack.pushNumeric(4)

class ICONST_5(NoOperandsInstruction):
    def execute(self, frame):
        frame.operandStack.pushNumeric(5)

class LCONST_0(NoOperandsInstruction):
    def execute(self, frame):
        frame.operandStack.pushNumeric(0)

class LCONST_1(NoOperandsInstruction):
    def execute(self, frame):
        frame.operandStack.pushNumeric(1)