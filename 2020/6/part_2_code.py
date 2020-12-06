#!/usr/bin/python
import sys
f = open("input", "r")
input = f.read().split('\n\n')
sum = 0
for i in input:
    answers = []
    for x in i.splitlines():
        answers.append(list(x))
    sum += len(set(answers[0]).intersection(*answers))
print(sum)
