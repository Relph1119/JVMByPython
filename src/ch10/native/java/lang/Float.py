#!/usr/bin/env python
# encoding: utf-8
"""
@author: HuRuiFeng
@file: Float.py
@time: 2019/9/21 10:24
@desc: java.lang.Float类
"""
import ctypes
import struct

from ch10.native.Registry import register
from ch10.rtda.Frame import Frame


def floatToRawIntBits(frame: Frame):
    """
    public static native int floatToRawIntBits(float value);
    (F)I
    :param frame:
    :return:
    """
    value = frame.local_vars.get_float(0)
    s = struct.pack('>f', value)
    bits = struct.unpack('>l', s)[0]
    frame.operand_stack.push_numeric(ctypes.c_int32(bits).value)


def intBitsToFloat(frame: Frame):
    """
    public static native float intBitsToFloat(int bits);
    (I)F
    :param frame:
    :return:
    """
    bits = frame.local_vars.get_numeric(0)
    s = struct.pack('>l', ctypes.c_uint32(bits).value)
    value = struct.unpack('>f', s)[0]
    frame.operand_stack.push_float(value)


jlFloat = "java/lang/Float"
register(jlFloat, "floatToRawIntBits", "(F)I", floatToRawIntBits)
register(jlFloat, "intBitsToFloat", "(I)F", intBitsToFloat)
