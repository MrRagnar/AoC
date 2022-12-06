import sys

file = open("input", "r")

match_sum = 0
for line in file:
    length = int(len(line)/2)
    first_compartment = line[:length]
    second_compartment = line[length:]
    matches = list(set(list(first_compartment)).intersection(second_compartment))[0]
    match matches.isupper():
        case False:
            match_sum += ord(matches) - 96
        case True:
            match_sum += ord(matches.lower()) - 70


print("Part 1: {}".format(match_sum))
