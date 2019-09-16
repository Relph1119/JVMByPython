#!/usr/bin/env python
# encoding: utf-8
"""
@author: HuRuiFeng
@file: AccessFlags.py
@time: 2019/9/16 16:13
@desc: 访问标志
"""

# 公共访问标志，适用于class、field、method
ACC_PUBLIC = 0x0001
# 私有访问标志，适用于field、method
ACC_PRIVATE = 0x0002
# 保护访问标志，适用于field、method
ACC_PROTECTED = 0x0004
# 静态访问标志，适用于field、method
ACC_STATIC = 0x0008
# final访问标志，适用于class、field、method
ACC_FINAL = 0x0010
# super访问标志，适用于class
ACC_SUPER = 0x0020
# synchronized访问标志，适用于method
ACC_SYNCHRONIZED = 0x0020
# volatile访问标志，适用于field
ACC_VOLATILE = 0x0040
# bridge访问标志，适用于method
ACC_BRIDGE = 0x0040
# transient访问标志，适用于field
ACC_TRANSIENT = 0x0080
# varargs访问标志，适用于method
ACC_VARARGS = 0x0080
# native访问标志，适用于method
ACC_NATIVE = 0x0100
# interface访问标志，适用于class
ACC_INTERFACE = 0x0200
# abstract访问标志，适用于class、method
ACC_ABSTRACT = 0x0400
# strict访问标志，适用于method
ACC_STRICT = 0x0800
# synthetic访问标志，适用于class、field、method
ACC_SYNTHETIC = 0x1000
# annotation访问标志，适用于class
ACC_ANNOTATION = 0x2000
# enum访问标志，适用于class、field
ACC_ENUM = 0x4000
