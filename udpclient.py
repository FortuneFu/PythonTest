#!/usr/bin/env python
# -*- coding: utf-8 -*-

import socket
import sys
import binascii

args = sys.argv

s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
<<<<<<< HEAD
data = input("hex:")
print('send data', data)
hexdata = binascii.a2b_hex(data)
s.sendto(hexdata, ('127.0.0.1', 7002))
=======
data = raw_input("hex:")
print'send data', data
hexdata = binascii.a2b_hex(data)
s.sendto(hexdata, ('127.0.0.1', 9999))
>>>>>>> fca1cbfea3071028becfac9593321112c371f7a9
s.close()
