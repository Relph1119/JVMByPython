#!/usr/bin/env python
# encoding: utf-8
"""
@author: HuRuiFeng
@file: System.py
@time: 2019/9/21 9:24
@desc: java.lang.System类
"""
from ch10.native.Registry import register
from ch10.rtda.Frame import Frame
from ch10.rtda.heap.Object import Object


def arraycopy(frame: Frame):
    local_vars = frame.local_vars
    # 从局部变量表中获取5个参数
    src = local_vars.get_ref(0)
    src_pos = local_vars.get_numeric(1)
    dest = local_vars.get_ref(2)
    dest_pos = local_vars.get_numeric(3)
    length = local_vars.get_numeric(4)

    # 源数据和目标数组都不能为None，否则按照System类的Javadoc应抛出NullPointerException异常
    if src is None and dest is None:
        raise RuntimeError("java.lang.NullPointerException")

    # 源数据和目标数据必须兼容才能拷贝，否则抛出ArrayStoreException异常
    if not check_array_copy(src, dest):
        raise RuntimeError("java.lang.ArrayStoreException")

    # 检查src_pos、dest_pos和length参数，有问题则抛出IndexOutOfBoundsException异常
    if src_pos < 0 or dest_pos < 0 or length < 0 \
            or src_pos + length > src.array_length() \
            or dest_pos + length > dest.array_length():
        raise RuntimeError("java.lang.IndexOutOfBoundsException")

    Object.array_copy(src, dest, src_pos, dest_pos, length)


def check_array_copy(src, dest) -> bool:
    src_class = src.get_class()
    dest_class = dest.get_class()
    # 确保src和dest都是数组
    if not src_class.is_array() or not dest_class.is_array():
        return False
    # 检查数组类型，如果两者都是引用数组，则可以拷贝，否则两者必须是相同类型的基本类型数组
    if src_class.component_class().is_primitive() or dest_class.component_class().is_primitive():
        return src_class == dest_class
    return True


register("java/lang/System", "arraycopy",
         "(Ljava/lang/Object;ILjava/lang/Object;II)V", arraycopy)
