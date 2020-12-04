#!/usr/bin/python
import sys
import itertools
f = open("input", "r")
input = f.read().splitlines()
input = list(map(int, input))
for (i,j) in itertools.product(input, repeat=2):
  if (i+j) == 2020:
      print(i*j)
      break
