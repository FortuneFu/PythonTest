#!/user/bin/env python
# -*- coding: utf-8 -*-

import binascii
array_alpha = [ 133, 53, 234, 241 ]
rs = binascii.hexlify(bytearray(array_alpha))
print(rs)