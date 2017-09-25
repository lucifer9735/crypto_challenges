#!/usr/bin/python3

import re
with open("4.txt") as fp:
    S = fp.readlines()

score = 0

for s in S:
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
