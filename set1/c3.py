#!/usr/bin/python3

import re

s = "1b37373331363f78151b7f2b783431333d78397828372d363c78373e783a393b3736"
score = 0

for i in range(0,255):
    m = []
    for j in re.findall(".{2}",s):
        m += [chr(i^int(j,16))]
    mm = "".join(m)
    num = len(re.findall("[a-z]",mm))
    if num > score:
        score = num
        M = mm
        key = chr(i)
print(key)
print(M)
