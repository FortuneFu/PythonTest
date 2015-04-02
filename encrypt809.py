#!/usr/bin/env python
# -*- coding: utf-8 -*-

import binascii

M1 = 10000000
IA1 = 20000000
IC1 = 30000000


def encrypt(key_pram, buffer_pram):
    idx = 0
    if key_pram == 0:
        key_pram = 1

    while idx < len(buffer_pram):
        key_pram = IA1 * (key_pram % M1) + IC1
        # 模拟C的无符号int溢出
        key_pram %= 2 ** 32
        # print(key_pram)
        buffer_pram[idx] ^= ((key_pram >> 20) & 0xFF)
        idx += 1


def remove_xor(ba):
    # ba = bytearray(binascii.a2b_hex(hex_org))
    ba_new = ba.replace(b'\x5a\x01', b'\x5b').replace(b'\x5a\x02', b'\x5a').replace(b'\x5e\x01', b'\x5d').replace(
        b'\x5e\x02', b'\x5e')
    return ba_new


if __name__ == '__main__':
    key = raw_input("key:")
    hex_str = raw_input("hex_str:")
    buffer = bytearray(binascii.a2b_hex(hex_str))
    buffer = remove_xor(buffer)
    print "rXOR:", binascii.b2a_hex(buffer)
    encrypt(int(key, 16), buffer)
    print "result:", binascii.b2a_hex(buffer)