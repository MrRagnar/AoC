#!/usr/bin/python
import sys
import itertools
f = open("input", "r")
input = f.read().splitlines()
input = list(map(int, input))
for (i,j,k) in itertools.product(input, repeat=3):
  if (i+j+k) == 2020:
      print(i*j*k)
      break
