#!/usr/bin/env python
# encoding: utf-8
"""
@author: HuRuiFeng
@file: ConstantInfo.py
@time: 2019/9/14 22:56
@desc: 常量类
"""

from abc import ABCMeta, abstractmethod


class ConstantInfo(metaclass=ABCMeta):
    # tag 常量值定义
    CONSTANT_Class = 7
    CONSTANT_FieldRef = 9
    CONSTANT_MethodRef = 10
    CONSTANT_InterfaceMethodRef = 11
    CONSTANT_String = 8
    CONSTANT_Integer = 3
    CONSTANT_Float = 4
    CONSTANT_Long = 5
    CONSTANT_Double = 6
    CONSTANT_NameAndType = 12
    CONSTANT_Utf8 = 1
    CONSTANT_MethodHandler = 15
    CONSTANT_MethodType = 16
    CONSTANT_InvokeDynamic = 18

    @abstractmethod
    def read_info(self, class_reader):
        pass

    @staticmethod
    def read_constant_info(class_reader, constant_pool):
        tag = int.from_bytes(class_reader.read_unit8(), byteorder="big")
        c = ConstantInfo.new_constant_info(tag, constant_pool)
        c.read_info(class_reader)
        return c

    @staticmethod
    def new_constant_info(tag, constant_pool):
        from .CpNumeric import ConstantDoubleInfo, ConstantLongInfo, ConstantFloatInfo, ConstantIntegerInfo
        from .ConstantUtf8Info import ConstantUtf8Info
        from .ConstantStringInfo import ConstantStringInfo
        from .ConstantMemberRefInfo import ConstantFieldRefInfo, ConstantInterfaceMethodRefInfo, \
            ConstantMethodRefInfo
        from .ConstantNameAndTypeInfo import ConstantNameAndTypeInfo
        from .ConstantClassInfo import ConstantClassInfo
        from .CpInvokeDynamic import ConstantInvokeDynamicInfo, ConstantMethodHandleInfo, \
            ConstantMethodTypeInfo

        if tag == ConstantInfo.CONSTANT_Integer:
            return ConstantIntegerInfo()
        elif tag == ConstantInfo.CONSTANT_Float:
            return ConstantFloatInfo()
        elif tag == ConstantInfo.CONSTANT_Long:
            return ConstantLongInfo()
        elif tag == ConstantInfo.CONSTANT_Double:
            return ConstantDoubleInfo()
        elif tag == ConstantInfo.CONSTANT_Utf8:
            return ConstantUtf8Info()
        elif tag == ConstantInfo.CONSTANT_String:
            return ConstantStringInfo(constant_pool)
        elif tag == ConstantInfo.CONSTANT_Class:
            return ConstantClassInfo(constant_pool)
        elif tag == ConstantInfo.CONSTANT_FieldRef:
            return ConstantFieldRefInfo(constant_pool)
        elif tag == ConstantInfo.CONSTANT_MethodRef:
            return ConstantMethodRefInfo(constant_pool)
        elif tag == ConstantInfo.CONSTANT_InterfaceMethodRef:
            return ConstantInterfaceMethodRefInfo(constant_pool)
        elif tag == ConstantInfo.CONSTANT_NameAndType:
            return ConstantNameAndTypeInfo()
        elif tag == ConstantInfo.CONSTANT_MethodHandler:
            return ConstantMethodHandleInfo()
        elif tag == ConstantInfo.CONSTANT_MethodType:
            return ConstantMethodTypeInfo()
        elif tag == ConstantInfo.CONSTANT_InvokeDynamic:
            return ConstantInvokeDynamicInfo()
        else:
            raise RuntimeError("java.lang.ClassFormatError: constant pool tag!")
