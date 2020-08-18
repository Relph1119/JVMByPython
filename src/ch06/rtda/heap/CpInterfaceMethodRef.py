#!/usr/bin/env python
# encoding: utf-8
"""
@author: HuRuiFeng
@file: CpInterfaceMethodRef.py
@time: 2019/9/16 18:13
@desc: 接口方法符号引用
"""
from ch06.classfile.ConstantMemberRefInfo import ConstantInterfaceMethodRefInfo
from ch06.rtda.heap.ConstantPool import ConstantPool
from ch06.rtda.heap.CpMemberRef import MemberRef


class InterfaceMethodRef(MemberRef):
    def __init__(self, constantPool: ConstantPool, refInfo: ConstantInterfaceMethodRefInfo):
        super().__init__()
        self.method = None
        self.cp = constantPool
        self.copy_member_ref_info(refInfo)
