#!/usr/bin/env python
# encoding: utf-8
"""
@author: HuRuiFeng
@file: ClassLoader.py
@time: 2019/9/16 18:16
@desc: 类加载器
"""
from classpath.Classpath import Classpath
from rtda.Slot import Slots
from rtda.heap.Class import Class
from rtda.heap.Field import Field


class ClassLoader:
    def __init__(self, class_path: Classpath):
        # 保存Classpath
        self.cp = class_path
        # 记录已经加载的类数据
        self.class_map = dict()

    # 把类数据加载到方法区
    def load_class(self, name):
        clazz = self.class_map.get(name)
        if clazz:
            # 类已经加载
            return clazz
        else:
            return self.load_non_array_class(name)

    # 非数组类（普通类）加载
    def load_non_array_class(self, name):
        # 把数据读取到内存中
        data, entry = self.read_class(name)
        # 解析class文件，生成虚拟机可以使用的类数据，并放入方法区
        clazz = self.define_class(data)
        # 进行链接
        self.link(clazz)
        print("[Loaded {0} from {1}]".format(name, entry))
        return clazz

    # 读取class文件，将数据读取到内存中
    def read_class(self, name):
        data, entry, error = self.cp.read_class(name)
        if error:
            raise RuntimeError("java.lang.ClassNotFoundException: " + name)
        # entry: 为了打印类加载信息，把最终加载class文件的类路径项也返回给调用者
        return data, entry

    # 生成类数据
    def define_class(self, data):
        # 解析class文件
        clazz = self.parse_class(data)
        clazz.loader = self
        self.resolve_super_class(clazz)
        self.resolve_interfaces(clazz)
        self.class_map[clazz.name] = clazz
        return clazz

    # 把class文件数据转换成Class对象
    @staticmethod
    def parse_class(data):
        from classfile.ClassFile import ClassFile

        class_file = ClassFile(data)
        cf, err = class_file.parse()
        if err:
            raise RuntimeError("java.lang.ClassFormatError!")
        else:
            return Class.new_class(cf)

    # 解析超类的符号引用
    @staticmethod
    def resolve_super_class(clazz: Class):
        if clazz.name != "java/lang/object" and clazz.super_class_name:
            clazz.super_class = clazz.loader.load_class(clazz.super_class_name)

    # 解析接口的符号引用
    @staticmethod
    def resolve_interfaces(clazz: Class):
        interface_count = len(clazz.interface_names)
        if interface_count > 0:
            for interfaceName in clazz.interface_names:
                clazz.interfaces.append(clazz.loader.load_class(interfaceName))

    # 类的链接
    @staticmethod
    def link(clazz: Class):
        ClassLoader.verify(clazz)
        ClassLoader.prepare(clazz)

    @staticmethod
    def verify(clazz):
        pass

    @staticmethod
    def prepare(clazz: Class):
        # 计算实例字段的个数，同时给它们编号
        ClassLoader.calc_instantce_field_slot_ids(clazz)
        # 计算静态字段的个数，同时给它们编号
        ClassLoader.calc_static_field_slot_ids(clazz)
        # 给类变量分配空间，给它们赋予初始值
        ClassLoader.alloc_and_init_static_vars(clazz)

    # 计算实例字段的个数，同时给它们编号
    @staticmethod
    def calc_instantce_field_slot_ids(clazz: Class):
        slot_id = 0
        if clazz.super_class:
            slot_id = clazz.super_class.instance_slot_count
        for field in clazz.fields:
            if not field.is_static():
                field.slot_id = slot_id
                slot_id += 1
                # 不需要判断long和double，每一个slot可设置为一个对象

        clazz.instance_slot_count = slot_id

    # 计算静态字段的个数，同时给它们编号
    @staticmethod
    def calc_static_field_slot_ids(clazz: Class):
        slot_id = 0
        for field in clazz.fields:
            if field.is_static():
                field.slot_id = slot_id
                slot_id += 1

        clazz.static_slot_count = slot_id

    # 给类变量分配空间，给它们赋予初始值
    @staticmethod
    def alloc_and_init_static_vars(clazz: Class):
        clazz.static_vars = Slots(clazz.static_slot_count)
        for field in clazz.fields:
            if field.is_static() and field.is_final():
                ClassLoader.init_static_final_var(clazz, field)

    # 从常量池中加载常量值，然后给静态变量赋值
    @staticmethod
    def init_static_final_var(clazz: Class, field: Field):
        static_vars = clazz.static_vars
        constant_pool = clazz.constant_pool
        cp_index = field.const_value_index
        slot_id = field.slot_id

        if cp_index > 0:
            if field.descriptor in {"Z", "B", "C", "S", "I", "J", "F", "D"}:
                val = constant_pool.get_constant(cp_index)
                static_vars.set_numeric(slot_id, val)
            elif field.descriptor == "Ljava/lang/String":
                raise RuntimeError("todo")
