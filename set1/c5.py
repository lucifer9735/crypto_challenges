#!/usr/bin/python3

import codecs

m = "Burning 'em, if you ain't quick and nimble I go crazy when I hear a cymbal"
key = "ICE"*100
def xor_str(s,t):
    return "".join(chr(ord(a)^ord(b)) for a,b in zip(s,t))
x = xor_str(m,key[:len(m)])

print(codecs.encode(str.encode(x),'hex'))
