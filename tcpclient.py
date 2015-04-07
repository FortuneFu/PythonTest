#!/usr/bin/env python
# -*- coding: utf-8 -*-

import socket

soc = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
soc.connect(('192.168.12.127', 9978))
soc.send("test")
