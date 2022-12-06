import sys

file = open("input", "r")

points = {"A": 1, "B": 2, "C": 3, "X": 1, "Y": 2, "Z": 3}
my_points = 0

for line in file:
    opponent = points[line.split()[0]]
    me = points[line.split()[1]]
    result = (me - opponent) % 3
    match result:
        case 0:
            my_points += me + 3
        case 1:
            my_points += me + 6
        case 2:
            my_points += me

print("Part 2: {}".format(my_points))
