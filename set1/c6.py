#!/usr/bin/python

import base64
import codecs

with open("6.txt") as fp:
    S = [bytes.decode(codecs.encode(base64.b64decode(i),'hex'))
            for i in fp.readlines()]
    S = "".join(S)
print(S)
