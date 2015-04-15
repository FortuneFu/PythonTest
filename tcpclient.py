#!/usr/bin/env python
# -*- coding: utf-8 -*-

import socket
import binascii

soc = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
data_hex = raw_input("hex:")
print "send:", data_hex
data_byte = binascii.a2b_hex(data_hex)

soc.connect(('192.168.12.127', 19978))
soc.send(data_byte)

buffer_hex = []
while True:
    d = soc.recv(1024)
    if d:
        buffer_hex.append(d)
    else:
        break

data_recv = "".join(buffer_hex)
print data_recv
soc.close
