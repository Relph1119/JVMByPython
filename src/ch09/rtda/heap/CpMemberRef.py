#!/usr/bin/env python
# encoding: utf-8
"""
@author: HuRuiFeng
@file: CpMemberRef.py
@time: 2019/9/16 18:02
@desc: 符号引用信息，用于存放字段和方法符号引用共有的信息
"""
from ch09.classfile.ConstantMemberRefInfo import ConstantMemberRefInfo
from ch09.rtda.heap.CpSymRef import SymRef


class MemberRef(SymRef):
    def __init__(self):
        super(MemberRef, self).__init__()
        self.name = ""
        self.descriptor = ""

    # 从class文件内存储的字段或方法常量中提取数据
    def copy_member_ref_info(self, ref_info: ConstantMemberRefInfo):
        self.class_name = ref_info.class_name
        self.name, self.descriptor = ref_info.name_and_descriptor
