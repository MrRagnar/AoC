#!/usr/bin/python
import sys
import numpy as np
f = open("input", "r")
input = f.read().splitlines()

trees = 0
steps_right = 3
steps_down = 1
matrix = []
for line in input:
    matrix.append(list(line))
for i in range(len(input) - 1):
    matrix = np.roll(matrix, steps_down * -1, axis=0)
    matrix = np.roll(matrix, steps_right * -1, axis=1)
    if matrix[0][0] == "#":
        trees += 1
print(trees)
