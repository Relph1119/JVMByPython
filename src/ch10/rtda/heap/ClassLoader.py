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
from rtda.heap import AccessFlags
from rtda.heap.Class import Class
from rtda.heap.ClassNameHelper import PrimitiveTypes
from rtda.heap.Field import Field


class ClassLoader:
    def __init__(self, class_path: Classpath, verbose_flag: bool):
        # 保存Classpath
        self.cp = class_path
        # 加载信息选项
        self.verbose_flag = verbose_flag
        # 记录已经加载的类数据
        self.class_map = dict()
        self.load_basic_classes()
        self.load_primitive_classes()

    # 把类数据加载到方法区
    def load_class(self, name):
        clazz = self.class_map.get(name)
        if clazz:
            # 类已经加载
            return clazz
        elif name[0] == '[':
            clazz = self.load_array_class(name)
        else:
            clazz = self.load_non_array_class(name)

        # 在类加载完之后，判断java.lang.Class是否已经加载。
        jl_class_class = self.class_map.get('java/lang/Class')
        if jl_class_class:
            # 如果加载，则给类关联类对象
            clazz.j_class = jl_class_class.new_object()
            clazz.j_class.extra = clazz

        return clazz

    # 数组类加载
    def load_array_class(self, name):
        clazz = Class()
        clazz.access_flags = AccessFlags.ACC_PUBLIC
        clazz.name = name
        clazz.loader = self
        # 数组类不需要初始化，把init_started字段设置成True
        clazz.init_started = True
        # 数组类的超类是java.lang.Object
        clazz.super_class = self.load_class("java/lang/Object")
        # 并实现了java.lang.Cloneable和java.io.Serializable接口
        clazz.interfaces = [self.load_class("java/lang/Cloneable"), self.load_class("java/io/Serializable")]
        self.class_map[name] = clazz
        return clazz

    # 非数组类（普通类）加载
    def load_non_array_class(self, name):
        # 把数据读取到内存中
        data, entry = self.read_class(name)
        # 解析class文件，生成虚拟机可以使用的类数据，并放入方法区
        clazz = self.define_class(data)
        # 进行链接
        self.link(clazz)
        if self.verbose_flag:
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

        class_file = ClassFile()
        cf, err = class_file.parse(data)
        if err:
            print(err)
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
        from rtda.heap.StringPool import j_string

        static_vars = clazz.static_vars
        constant_pool = clazz.constant_pool
        cp_index = field.const_value_index
        slot_id = field.slot_id

        if cp_index > 0:
            if field.descriptor in {"Z", "B", "C", "S", "I", "J"}:
                val = constant_pool.get_constant(cp_index)
                static_vars.set_numeric(slot_id, val)
            elif field.descriptor == 'D':
                val = constant_pool.get_constant(cp_index)
                static_vars.set_double(slot_id, val)
            elif field.descriptor == 'F':
                val = constant_pool.get_constant(cp_index)
                static_vars.set_float(slot_id, val)
            elif field.descriptor == "Ljava/lang/String":
                python_str = constant_pool.get_constant(cp_index)
                j_str = j_string(clazz.loader, python_str)
                static_vars.set_ref(slot_id, j_str)

    def load_basic_classes(self):
        # 先加载java.lang.Class类
        jl_class_class = self.load_class("java/lang/Class")
        # 遍历class_map，给已经加载的每个类关联类的对象。
        for _, clazz in self.class_map.items():
            if clazz.j_class is None:
                clazz.j_class = jl_class_class.new_object()
                clazz.j_class.extra = clazz

    # 加载基本类型的类
    def load_primitive_classes(self):
        for primitive_type, _ in PrimitiveTypes.items():
            # primitive_type是void、int、float等
            self.load_primitive_class(primitive_type)

    # 加载基本类型的单个类
    def load_primitive_class(self, class_name):
        """
        有3点说明：1. void和基本类型的类名就是void、int、float等。
        2. 基本类型的类没有超类，也没有实现任何接口。
        3. 非基本类型的类对象是通过ldc指令加载到操作数栈中的。
        而基本类型的类对象，虽然在Java代码中看起来是通过字面量获取的，但是编译之后的指令并不是ldc，而是getstatic。
        :param class_name:
        :return:
        """
        clazz = Class()
        clazz.access_flags = AccessFlags.ACC_PUBLIC
        clazz.name = class_name
        clazz.loader = self
        clazz.init_started = True

        clazz.j_class = self.class_map.get('java/lang/Class').new_object()
        clazz.j_class.extra = clazz
        self.class_map[class_name] = clazz
