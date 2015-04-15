#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import socket
import sys
import binascii

args = sys.argv

s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
data = input("hex:")
print('send data', data)
hexdata = binascii.a2b_hex(data)
s.sendto(hexdata, ('127.0.0.1', 7002))
s.close()
