#!/usr/bin/python
import sys
f = open("input", "r")
input = f.read().split('\n\n')

sum = 0
for i in input:
    group = ""
    for x in i.splitlines():
        group += x
    uniq = set(list(group))
    sum += len(uniq)
print(sum)
