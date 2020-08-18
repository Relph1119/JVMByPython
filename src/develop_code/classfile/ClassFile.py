#!/usr/bin/env python
# encoding: utf-8
"""
@author: HuRuiFeng
@file: ClassFile.py
@time: 2019/9/12 15:05
@desc: 解析class文件
"""
from classfile.AttrSourceFile import SourceFileAttribute
from classfile.AttributeInfo import AttributeInfo
from classfile.ClassReader import ClassReader
from classfile.ConstantPool import ConstantPool
from classfile.MemberInfo import MemberInfo


class ClassFile:
    def __init__(self):
        # 小版本号
        self.minor_version = ""
        # 主版本号
        self.major_version = ""
        # 常量池
        self.constant_pool = None
        # 类访问标志，用于指出class文件定义的是类还是接口，访问级别是public还是private
        self.access_flags = ""
        # 类索引
        self.this_class = ""
        # 超类索引
        self.super_class = ""
        # 接口索引表
        self.interfaces = []
        # 变量
        self.fields = []
        # 方法
        self.methods = []
        # 属性
        self.attributes = []

    def parse(self, class_data):
        try:
            class_reader = ClassReader(class_data)
            self.read(class_reader)
            return self, None
        except Exception as err:
            return self, err

    def read(self, class_reader):
        self.read_and_check_magic(class_reader)
        self.read_and_check_version(class_reader)

        self.constant_pool = ConstantPool()
        self.constant_pool.read_constant_pool(class_reader)

        self.access_flags = int.from_bytes(class_reader.read_unit16(), byteorder="big")
        self.this_class = int.from_bytes(class_reader.read_unit16(), byteorder="big")
        self.super_class = int.from_bytes(class_reader.read_unit16(), byteorder="big")
        self.interfaces = class_reader.read_unit16s()

        member_info = MemberInfo(self.constant_pool)
        self.fields = member_info.read_members(class_reader, self.constant_pool)
        self.methods = member_info.read_members(class_reader, self.constant_pool)
        self.attributes = AttributeInfo.read_attributes(class_reader, self.constant_pool)

    # 读取并检查Class文件的起始字节，必须以0xCAFEBABE固定字节开头
    @staticmethod
    def read_and_check_magic(class_reader):
        magic = class_reader.read_unit32()
        if magic != b'\xca\xfe\xba\xbe':
            raise RuntimeError("java.lang.ClassFormatError: magic!")

    # 读取并检查版本号，由于采用java1.8的编译器，故支持版本号为45.0~52.0的class文件
    def read_and_check_version(self, class_reader):
        self.minor_version = int.from_bytes(class_reader.read_unit16(), byteorder='big')
        self.major_version = int.from_bytes(class_reader.read_unit16(), byteorder='big')

        if self.major_version == 45:
            return
        elif self.major_version in {46, 47, 48, 49, 50, 51, 52}:
            if self.minor_version == 0:
                return
        raise RuntimeError("java.lang.UnsupportedClassVersionError!")

    # 从常量池中查找类名
    @property
    def class_name(self):
        return self.constant_pool.get_class_name(self.this_class)

    # 从常量池中查找超类类名
    @property
    def super_class_name(self):
        if self.super_class > 0:
            return self.constant_pool.get_class_name(self.super_class)
        # 只有java.lang.Object没有超类
        return ""

    # 从常量池中查找接口名
    @property
    def interface_names(self):
        return [self.constant_pool.get_class_name(cpName) for cpName in self.interfaces]

    def fields(self):
        return self.fields

    def source_file_attribute(self):
        for _, attr_info in enumerate(self.attributes):
            if isinstance(attr_info, SourceFileAttribute):
                return attr_info

        return None
