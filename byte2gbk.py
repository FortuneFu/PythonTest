#!/usr/bin/env python
# -*- coding: utf-8 -*-

import binascii

if __name__ == '__main__':
	hex_str = raw_input("hex:")
	print (binascii.a2b_hex(hex_str)).decode('GBK')