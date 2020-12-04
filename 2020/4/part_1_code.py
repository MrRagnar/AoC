#!/usr/bin/python
import sys
f = open("input", "r")
input = f.read().split("\n\n")
data = []
passports = []
for line in input:
    line = line.replace('\n',' ')
    data.append(line.strip().split(' '))

for i in range(len(data)):
    p = {}
    for x in data[i]:
        key = x.split(':')[0]
        value = x.split(':')[1]
        p[key] = value
    if all (k in p for k in ("byr","iyr","eyr","hgt","hcl","ecl","pid")):
        passports.append(p)
print(len(passports))
