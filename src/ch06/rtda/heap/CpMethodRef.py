#!/usr/bin/env python
# encoding: utf-8
"""
@author: HuRuiFeng
@file: CpMethodRef.py
@time: 2019/9/16 18:11
@desc: 方法符号引用
"""
from ch06.classfile.ConstantMemberRefInfo import ConstantMethodRefInfo
from ch06.rtda.heap.ConstantPool import ConstantPool
from ch06.rtda.heap.CpMemberRef import MemberRef


class MethodRef(MemberRef):
    def __init__(self, constant_pool: ConstantPool, ref_info: ConstantMethodRefInfo):
        super(MethodRef, self).__init__()
        self.method = None
        self.cp = constant_pool
        self.copy_member_ref_info(ref_info)
