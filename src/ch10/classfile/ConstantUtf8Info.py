#!/usr/bin/env python
# encoding: utf-8
"""
@author: HuRuiFeng
@file: ConstantUtf8Info.py
@time: 2019/9/15 00:14
@desc: MUTF-9编码的字符串类
"""

import ctypes

from .ConstantInfo import ConstantInfo


class ConstantUtf8Info(ConstantInfo):
    def __init__(self):
        self.str = ""

    # 先读取出byte[]，然后调用decode_mutf8()函数把它解码成字符串
    def read_info(self, class_reader):
        length = ctypes.c_uint32(int.from_bytes(class_reader.read_unit16(), byteorder='big')).value
        if length == 0:
            self.str = ""
        else:
            bytes_data = class_reader.read_bytes(length)
            self.str = self.decode_mutf8(bytes_data)

    @staticmethod
    def decode_mutf8(bytes_data):
        # return bytes_data.decode('utf-8')
        utf_len = len(bytes_data)

        count = 0
        chararr_count = 0
        char_arr = [0 for _ in range(utf_len)]

        while count < utf_len:
            c = int(bytes_data[count])
            if c > 127:
                break

            count += 1
            char_arr[chararr_count] = c
            chararr_count += 1

        while count < utf_len:
            c = int(bytes_data[count])
            temp = c >> 4
            if temp in {0, 1, 2, 3, 4, 5, 6, 7}:
                # 0xxxxxxx
                count += 1
                char_arr[chararr_count] = c
                chararr_count += 1
            elif temp in {12, 13}:
                # 110x xxxx   10xx xxxx
                count += 2
                if count > utf_len:
                    raise RuntimeError("malformed input: partial character at end")
                char2 = int(bytes_data[count - 1])
                if (char2 & 0xC0) != 0x80:
                    raise RuntimeError("malformed input around byte {0}".format(count))
                char_arr[chararr_count] = (c & 0x1F) << 6 | (char2 & 0x3F)
                chararr_count += 1
            elif temp == 14:
                # 1110 xxxx  10xx xxxx  10xx xxxx
                count += 3
                if count > utf_len:
                    raise RuntimeError("malformed input: partial character at end")
                char2 = int(bytes_data[count - 2])
                char3 = int(bytes_data[count - 1])
                if (char2 & 0xC0) != 0x80 or (char3 & 0xC0) != 0x80:
                    raise RuntimeError("malformed input around byte {0}".format(count - 1))
                char_arr[chararr_count] = (c & 0x0F) << 12 | (char2 & 0x3F) << 6 | (char3 & 0x3F) << 0
                chararr_count += 1
            else:
                raise RuntimeError("malformed input around byte {0}".format(count))

        char_arr = char_arr[:chararr_count]
        return "".join([chr(d) for d in char_arr])
