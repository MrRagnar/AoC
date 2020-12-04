#!/usr/bin/python
import sys
import numpy as np
f = open("input", "r")
input = f.read().splitlines()

steps = [{1:1}, {3:1}, {5:1}, {7:1}, {1:2}]
paths = []

for step in steps:
    for right, down in step.items():
        matrix = []
        for line in input:
            matrix.append(list(line))
        trees = 0
        row = 0
        while row < len(input) - 1:
            matrix = np.roll(matrix, down * -1, axis=0)
            matrix = np.roll(matrix, right * -1, axis=1)
            if matrix[0][0] == "#":
                trees += 1
            row += down
        paths.append(trees)
print(np.prod(paths))
