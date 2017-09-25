#!/usr/bin/python2

import re

with open("8.txt") as fp:
    C = [i for i in fp.readlines()]
for ECB in C:
    block = re.findall('.{16}',ECB)
    if len(block) - len(set(block)):
        print ECB
        print block
        print len(block)
        print set(block)
        print len(set(block))
        print len(block) - len(set(block))
