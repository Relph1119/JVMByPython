#!/usr/bin/env python
# encoding: utf-8
"""
@author: HuRuiFeng
@file: Double.py
@time: 2019/9/21 10:45
@desc: java.lang.Double类
"""
import struct

from ch10.native.Registry import register
from ch10.rtda.Frame import Frame


def doubleToRawLongBits(frame: Frame):
    """
    public static native long doubleToRawLongBits(double value);
    (D)J
    :param frame:
    :return:
    """
    value = frame.local_vars.get_double(0)
    s = struct.pack('>d', value)
    bits = struct.unpack('>q', s)[0]
    frame.operand_stack.push_numeric(bits)


def longBitsToDouble(frame: Frame):
    """
    public static native double longBitsToDouble(long bits);
    (J)D
    :param frame:
    :return:
    """
    bits = frame.local_vars.get_numeric(0)
    s = struct.pack('>q', bits)
    value = struct.unpack('>d', s)[0]
    frame.operand_stack.push_double(value)


jlDouble = "java/lang/Double"
register(jlDouble, "doubleToRawLongBits", "(D)J", doubleToRawLongBits)
register(jlDouble, "longBitsToDouble", "(J)D", longBitsToDouble)
