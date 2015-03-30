#!/usr/bin/env python3

import binascii

hex_org = "5a01fffe5a020203"
ba = bytearray(binascii.a2b_hex(hex_org))
print(hex_org)
ba_new = ba.replace(b'\x5a\x01',b'\x5b').replace(b'\x5a\x02',b'\x5a').replace(b'\x5e\x01',b'\x5d').replace(b'\x5e\x02',b'\x5e')
print(binascii.b2a_hex(ba_new))