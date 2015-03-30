#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import binascii 

M1 = 10000000
IA1 = 20000000
IC1 = 30000000

def encrypt(key,buffer):
	idx = 0
	if(key == 0):
		key = 1

	while(idx < len(buffer)):
		key = IA1 * (key % M1) + IC1
		# 模拟C的无符号int溢出
		key = key % (2 ** 32);
		# print(key)
		buffer[idx] ^= ((key >>20)&0xFF)
		idx += 1

def removeXOR(ba):
	# ba = bytearray(binascii.a2b_hex(hex_org))
	ba_new = ba.replace(b'\x5a\x01',b'\x5b').replace(b'\x5a\x02',b'\x5a').replace(b'\x5e\x01',b'\x5d').replace(b'\x5e\x02',b'\x5e')
	return ba_new

if __name__=='__main__':
	key = input("key:")
	hex_str = input("hex_str:")
	buffer = bytearray(binascii.a2b_hex(hex_str))
	buffer = removeXOR(buffer)
	print("rXOR:",binascii.b2a_hex(buffer))
	encrypt(int(key,16),buffer)
	print("result:",binascii.b2a_hex(buffer))