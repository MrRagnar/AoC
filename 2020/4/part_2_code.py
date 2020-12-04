#!/usr/bin/python
import sys
import re
f = open("input", "r")
input = f.read().split("\n\n")
ex_hgt = re.compile('(^(1[5-8][0-9]|19[0-3])cm$)|(^(59|6[0-9]|7[0-6])in$)')
ex_hcl = re.compile('^#[0-9a-z]{6}$')
ex_pid = re.compile('^[0-9]{9}$')
data = []
passports = []
for line in input:
    line = line.replace('\n',' ').lower()
    data.append(line.strip().split(' '))
for i in range(len(data)):
    p = {}
    for x in data[i]:
        key = x.split(':')[0]
        value = x.split(':')[1]
        p[key] = value
    if all (k in p for k in ("byr","iyr","eyr","hgt","hcl","ecl","pid")):
        try:
            if int(p['byr']) not in range(1920,2003):
                raise ValueError
            if int(p['iyr']) not in range(2010,2021):
                raise ValueError
            if int(p['eyr']) not in range(2020,2031):
                raise ValueError
            if not ex_hgt.match(p['hgt']):
                raise ValueError
            if not ex_hcl.match(p['hcl']):
                raise ValueError
            if not ex_pid.match(p['pid']):
                raise ValueError
            if p['ecl'] not in ("amb","blu","brn","gry","grn","hzl","oth"):
                raise ValueError
        except:
            continue
        passports.append(p)
print(len(passports))
