#!/usr/bin/python
import sys
c = 0
f = open("input", "r")
input = f.read().splitlines()
for line in input:
    pos = line.split(' ')[0]
    s = line.split(' ')[1][:-1]
    p = line.split(' ')[2]
    pos1 = int(pos.split('-')[0]) -1
    pos2 = int(pos.split('-')[1]) -1
    temp = p[pos1] + p[pos2]
    o = temp.count(s)
    if o == 1:
        c += 1
print(c)
