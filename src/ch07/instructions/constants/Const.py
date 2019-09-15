from ch07.instructions.base.Instruction import NoOperandsInstruction

class ACONST_NULL(NoOperandsInstruction):
    def execute(self, frame):
        frame.operandStack.push_ref(None)

class DCONST_0(NoOperandsInstruction):
    def execute(self, frame):
        frame.operandStack.push_numeric(0.0)

class DCONST_1(NoOperandsInstruction):
    def execute(self, frame):
        frame.operandStack.push_numeric(1.0)

class FCONST_0(NoOperandsInstruction):
    def execute(self, frame):
        frame.operandStack.push_numeric(0.0)

class FCONST_1(NoOperandsInstruction):
    def execute(self, frame):
        frame.operandStack.push_numeric(1.0)

class FCONST_2(NoOperandsInstruction):
    def execute(self, frame):
        frame.operandStack.push_numeric(2.0)

class ICONST_M1(NoOperandsInstruction):
    def execute(self, frame):
        frame.operandStack.push_numeric(-1)

class ICONST_0(NoOperandsInstruction):
    def execute(self, frame):
        frame.operandStack.push_numeric(0)

class ICONST_1(NoOperandsInstruction):
    def execute(self, frame):
        frame.operandStack.push_numeric(1)

class ICONST_2(NoOperandsInstruction):
    def execute(self, frame):
        frame.operandStack.push_numeric(2)

class ICONST_3(NoOperandsInstruction):
    def execute(self, frame):
        frame.operandStack.push_numeric(3)

class ICONST_4(NoOperandsInstruction):
    def execute(self, frame):
        frame.operandStack.push_numeric(4)

class ICONST_5(NoOperandsInstruction):
    def execute(self, frame):
        frame.operandStack.push_numeric(5)

class LCONST_0(NoOperandsInstruction):
    def execute(self, frame):
        frame.operandStack.push_numeric(0)

class LCONST_1(NoOperandsInstruction):
    def execute(self, frame):
        frame.operandStack.push_numeric(1)