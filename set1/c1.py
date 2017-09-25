#!/usr/bin/python3

import codecs
import base64

s_hex = '49276d206b696c6c696e6720796f757220627261696e206c696b65206120706f69736f6e6f7573206d757368726f6f6d'
s = codecs.decode(s_hex,'hex')
s_base64 = base64.b64encode(s)

print(s_base64)
