#!/usr/bin/python
import sys
c = 0
f = open("input", "r")
input = f.read().splitlines()
for line in input:
    r = line.split(' ')[0]
    s = line.split(' ')[1][:-1]
    p = line.split(' ')[2]
    r_min = int(r.split('-')[0])
    r_max = int(r.split('-')[1])
    o = p.count(s)
    if r_min <= o <= r_max:
        c += 1
print(c)
