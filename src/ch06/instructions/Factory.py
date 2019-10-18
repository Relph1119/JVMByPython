#!/usr/bin/env python
# encoding: utf-8
"""
@author: HuRuiFeng
@file: Factory.py
@time: 2019/9/15 22:28
@desc: 根据操作码创建具体的指令
"""

from instructions.comparisons.Dcmp import *
from instructions.comparisons.Fcmp import *
from instructions.comparisons.Ifacmp import *
from instructions.comparisons.Ifcond import *
from instructions.comparisons.Ificmp import *
from instructions.comparisons.Lcmp import *
from instructions.constants.Const import *
from instructions.constants.Ipush import *
from instructions.constants.Ldc import *
from instructions.constants.Nop import *
from instructions.control.Goto import *
from instructions.control.Lookupswitch import *
from instructions.control.Tableswitch import *
from instructions.conversions.D2x import *
from instructions.conversions.F2x import *
from instructions.conversions.I2x import *
from instructions.conversions.L2x import *
from instructions.extended.Gotow import *
from instructions.extended.Ifnull import *
from instructions.extended.Wide import *
from instructions.loads.Aload import *
from instructions.loads.Dload import *
from instructions.loads.Fload import *
from instructions.loads.Iload import *
from instructions.loads.Lload import *
from instructions.math.Add import *
from instructions.math.And import *
from instructions.math.Div import *
from instructions.math.Mul import *
from instructions.math.Neg import *
from instructions.math.Or import *
from instructions.math.Rem import *
from instructions.math.Sh import *
from instructions.math.Sub import *
from instructions.math.Xor import *
from instructions.references.Checkcast import CHECK_CAST
from instructions.references.Getfield import GET_FIELD
from instructions.references.Getstatic import GET_STATIC
from instructions.references.Instanceof import INSTANCE_OF
from instructions.references.Invokespecial import INVOKE_SPECIAL
from instructions.references.Invokevirtual import INVOKE_VIRTURL
from instructions.references.New import NEW
from instructions.references.Putfield import PUT_FIELD
from instructions.references.Putstatic import PUT_STATIC
from instructions.stack.Dup import *
from instructions.stack.Pop import *
from instructions.stack.Swap import *
from instructions.stores.Astore import *
from instructions.stores.Dstore import *
from instructions.stores.Fstore import *
from instructions.stores.Istore import *
from instructions.stores.Lstore import *


class Factory:

    @staticmethod
    def new_instruction(opcode):
        if opcode == 0x00:
            return NOP()
        elif opcode == 0x01:
            return ACONST_NULL()
        elif opcode == 0x02:
            return ICONST_M1()
        elif opcode == 0x03:
            return ICONST_0()
        elif opcode == 0x04:
            return ICONST_1()
        elif opcode == 0x05:
            return ICONST_2()
        elif opcode == 0x06:
            return ICONST_3()
        elif opcode == 0x07:
            return ICONST_4()
        elif opcode == 0x08:
            return ICONST_5()
        elif opcode == 0x09:
            return LCONST_0()
        elif opcode == 0x0a:
            return LCONST_1()
        elif opcode == 0x0b:
            return FCONST_0()
        elif opcode == 0x0c:
            return FCONST_1()
        elif opcode == 0x0d:
            return FCONST_2()
        elif opcode == 0x0e:
            return DCONST_0()
        elif opcode == 0x0f:
            return DCONST_1()
        elif opcode == 0x10:
            return BIPUSH()
        elif opcode == 0x11:
            return SIPUSH()
        elif opcode == 0x12:
            return LDC()
        elif opcode == 0x13:
            return LDC_W()
        elif opcode == 0x14:
            return LDC2_W()
        elif opcode == 0x15:
            return ILOAD()
        elif opcode == 0x16:
            return LLOAD()
        elif opcode == 0x17:
            return FLOAD()
        elif opcode == 0x18:
            return DLOAD()
        elif opcode == 0x19:
            return ALOAD()
        elif opcode == 0x1a:
            return ILOAD_0()
        elif opcode == 0x1b:
            return ILOAD_1()
        elif opcode == 0x1c:
            return ILOAD_2()
        elif opcode == 0x1d:
            return ILOAD_3()
        elif opcode == 0x1e:
            return LLOAD_0()
        elif opcode == 0x1f:
            return LLOAD_1()
        elif opcode == 0x20:
            return LLOAD_2()
        elif opcode == 0x21:
            return LLOAD_3()
        elif opcode == 0x22:
            return FLOAD_0()
        elif opcode == 0x23:
            return FLOAD_1()
        elif opcode == 0x24:
            return FLOAD_2()
        elif opcode == 0x25:
            return FLOAD_3()
        elif opcode == 0x26:
            return DLOAD_0()
        elif opcode == 0x27:
            return DLOAD_1()
        elif opcode == 0x28:
            return DLOAD_2()
        elif opcode == 0x29:
            return DLOAD_3()
        elif opcode == 0x2a:
            return ALOAD_0()
        elif opcode == 0x2b:
            return ALOAD_1()
        elif opcode == 0x2c:
            return ALOAD_2()
        elif opcode == 0x2d:
            return ALOAD_3()

        elif opcode == 0x36:
            return ISTORE()
        elif opcode == 0x37:
            return LSTORE()
        elif opcode == 0x38:
            return FSTORE()
        elif opcode == 0x39:
            return DSTORE()
        elif opcode == 0x3a:
            return ASTORE()
        elif opcode == 0x3b:
            return ISTORE_0()
        elif opcode == 0x3c:
            return ISTORE_1()
        elif opcode == 0x3d:
            return ISTORE_2()
        elif opcode == 0x3e:
            return ISTORE_3()
        elif opcode == 0x3f:
            return LSTORE_0()
        elif opcode == 0x40:
            return LSTORE_1()
        elif opcode == 0x41:
            return LSTORE_2()
        elif opcode == 0x42:
            return LSTORE_3()
        elif opcode == 0x43:
            return FSTORE_0()
        elif opcode == 0x44:
            return FSTORE_1()
        elif opcode == 0x45:
            return FSTORE_2()
        elif opcode == 0x46:
            return FSTORE_3()
        elif opcode == 0x47:
            return DSTORE_0()
        elif opcode == 0x48:
            return DSTORE_1()
        elif opcode == 0x49:
            return DSTORE_2()
        elif opcode == 0x4a:
            return DSTORE_3()
        elif opcode == 0x4b:
            return ASTORE_0()
        elif opcode == 0x4c:
            return ASTORE_1()
        elif opcode == 0x4d:
            return ASTORE_2()
        elif opcode == 0x4e:
            return ASTORE_3()

        elif opcode == 0x57:
            return POP()
        elif opcode == 0x58:
            return POP2()
        elif opcode == 0x59:
            return DUP()
        elif opcode == 0x5a:
            return DUP_X1()
        elif opcode == 0x5b:
            return DUP_X2()
        elif opcode == 0x5c:
            return DUP2()
        elif opcode == 0x5d:
            return DUP2_X1()
        elif opcode == 0x5e:
            return DUP2_X2()
        elif opcode == 0x5f:
            return SWAP()
        elif opcode == 0x60:
            return IADD()
        elif opcode == 0x61:
            return LADD()
        elif opcode == 0x62:
            return FADD()
        elif opcode == 0x63:
            return DADD()
        elif opcode == 0x64:
            return ISUB()
        elif opcode == 0x65:
            return LSUB()
        elif opcode == 0x66:
            return FSUB()
        elif opcode == 0x67:
            return DSUB()
        elif opcode == 0x68:
            return IMUL()
        elif opcode == 0x69:
            return LMUL()
        elif opcode == 0x6a:
            return FMUL()
        elif opcode == 0x6b:
            return DMUL()
        elif opcode == 0x6c:
            return IDIV()
        elif opcode == 0x6d:
            return LDIV()
        elif opcode == 0x6e:
            return FDIV()
        elif opcode == 0x6f:
            return DDIV()
        elif opcode == 0x70:
            return IREM()
        elif opcode == 0x71:
            return LREM()
        elif opcode == 0x72:
            return FREM()
        elif opcode == 0x73:
            return DREM()
        elif opcode == 0x74:
            return INEG()
        elif opcode == 0x75:
            return LNEG()
        elif opcode == 0x76:
            return FNEG()
        elif opcode == 0x77:
            return DNEG()
        elif opcode == 0x78:
            return ISHL()
        elif opcode == 0x79:
            return LSHL()
        elif opcode == 0x7a:
            return ISHR()
        elif opcode == 0x7b:
            return LSHR()
        elif opcode == 0x7c:
            return IUSHR()
        elif opcode == 0x7d:
            return LUSHR()
        elif opcode == 0x7e:
            return IAND()
        elif opcode == 0x7f:
            return LAND()
        elif opcode == 0x80:
            return IOR()
        elif opcode == 0x81:
            return LOR()
        elif opcode == 0x82:
            return IXOR()
        elif opcode == 0x83:
            return LXOR()
        elif opcode == 0x84:
            return IINC()
        elif opcode == 0x85:
            return I2L()
        elif opcode == 0x86:
            return I2F()
        elif opcode == 0x87:
            return I2D()
        elif opcode == 0x88:
            return L2I()
        elif opcode == 0x89:
            return L2F()
        elif opcode == 0x8a:
            return L2D()
        elif opcode == 0x8b:
            return F2I()
        elif opcode == 0x8c:
            return F2L()
        elif opcode == 0x8d:
            return F2D()
        elif opcode == 0x8e:
            return D2I()
        elif opcode == 0x8f:
            return D2L()
        elif opcode == 0x90:
            return D2F()
        elif opcode == 0x91:
            return I2B()
        elif opcode == 0x92:
            return I2C()
        elif opcode == 0x93:
            return I2S()
        elif opcode == 0x94:
            return LCMP()
        elif opcode == 0x95:
            return FCMPL()
        elif opcode == 0x96:
            return FCMPG()
        elif opcode == 0x97:
            return DCMPL()
        elif opcode == 0x98:
            return DCMPG()
        elif opcode == 0x99:
            return IFEQ()
        elif opcode == 0x9a:
            return IFNE()
        elif opcode == 0x9b:
            return IFLT()
        elif opcode == 0x9c:
            return IFGE()
        elif opcode == 0x9d:
            return IFGT()
        elif opcode == 0x9e:
            return IFLE()
        elif opcode == 0x9f:
            return IF_ICMPEQ()
        elif opcode == 0xa0:
            return IF_ICMPNE()
        elif opcode == 0xa1:
            return IF_ICMPLT()
        elif opcode == 0xa2:
            return IF_ICMPGE()
        elif opcode == 0xa3:
            return IF_ICMPGT()
        elif opcode == 0xa4:
            return IF_ICMPLE()
        elif opcode == 0xa5:
            return IF_ACMPEQ()
        elif opcode == 0xa6:
            return IF_ACMPNE()
        elif opcode == 0xa7:
            return GOTO()

        elif opcode == 0xaa:
            return TABLE_SWITCH()
        elif opcode == 0xab:
            return LOOKUP_SWITCH()

        elif opcode == 0xb2:
            return GET_STATIC()
        elif opcode == 0xb3:
            return PUT_STATIC()
        elif opcode == 0xb4:
            return GET_FIELD()
        elif opcode == 0xb5:
            return PUT_FIELD()
        elif opcode == 0xb6:
            return INVOKE_VIRTURL()
        elif opcode == 0xb7:
            return INVOKE_SPECIAL()

        elif opcode == 0xbb:
            return NEW()

        elif opcode == 0xc0:
            return CHECK_CAST()
        elif opcode == 0xc1:
            return INSTANCE_OF()

        elif opcode == 0xc4:
            return WIDE()

        elif opcode == 0xc6:
            return IFNULL()
        elif opcode == 0xc7:
            return IFNONNULL()
        elif opcode == 0xc8:
            return GOTO_W()
        else:
            raise RuntimeError("Unsupported opcode: {0}!".format(hex(opcode)))
