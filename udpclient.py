#!/usr/bin/env python
# -*- coding: utf-8 -*-

import socket
import sys
import binascii

args = sys.argv

s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
data = raw_input("str:")
print'send data', data
hexdata = binascii.a2b_hex(data)
s.sendto(hexdata, ('192.168.12.114', 7002))
#s.sendto(hexdata, ('203.194.149.171', 9919))
#s.sendto(hexdata, ('203.194.149.79', 7919))
s.close()
