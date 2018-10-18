from abc import ABCMeta, abstractstaticmethod

class Constant(metaclass=ABCMeta):
    def __init__(self):
        pass

class ConstantPool():
    def __init__(self, clazz, consts):
        self._class = clazz
        self.consts = consts

    @staticmethod
    def newConstantPool(clazz, cfConstantPool):
        from ch07.classfile.CpNumeric import ConstantDoubleInfo, ConstantLongInfo, ConstantFloatInfo, ConstantIntgerInfo
        from ch07.classfile.ConstantStringInfo import ConstantStringInfo
        from ch07.classfile.ConstantClassInfo import ConstantClassInfo
        from ch07.classfile.ConstantMemberrefInfo import ConstantFieldrefInfo, ConstantMethodrefInfo, ConstantInterfaceMethodrefInfo
        from ch07.rtda.heap.CpClassRef import ClassRef
        from ch07.rtda.heap.CpFieldref import FieldRef
        from ch07.rtda.heap.CpMethodref import MethodRef
        from ch07.rtda.heap.CpInterfaceMethodref import InterfaceMethodRef

        cpCount = len(cfConstantPool.cp)
        consts = [None for i in range(cpCount)]
        rtCp = ConstantPool(clazz, consts)

        for i in range(1, cpCount):
            cpInfo = cfConstantPool.cp[i]
            if isinstance(cpInfo, ConstantIntgerInfo):
                consts[i] = cpInfo.val
            elif isinstance(cpInfo, ConstantFloatInfo):
                consts[i] = cpInfo.val
            elif isinstance(cpInfo, ConstantLongInfo):
                consts[i] = cpInfo.val
            elif isinstance(cpInfo, ConstantDoubleInfo):
                consts[i] = cpInfo.val
            elif isinstance(cpInfo, ConstantStringInfo):
                consts[i] = cpInfo.String()
            elif isinstance(cpInfo, ConstantClassInfo):
                consts[i] = ClassRef.newClassRef(rtCp, cpInfo)
            elif isinstance(cpInfo, ConstantFieldrefInfo):
                consts[i] = FieldRef.newFieldRef(rtCp, cpInfo)
            elif isinstance(cpInfo, ConstantMethodrefInfo):
                consts[i] = MethodRef.newMethodRef(rtCp, cpInfo)
            elif isinstance(cpInfo, ConstantInterfaceMethodrefInfo):
                consts[i] = InterfaceMethodRef.newInterfaceMethodRef(rtCp, cpInfo)

        #rtCp.consts = consts
        return rtCp

    def getClass(self):
        return self._class


    def getConstant(self, index):
        c = self.consts[index]
        if c:
            return c
        else:
            raise RuntimeError("No constants at index {0}".format(index))

