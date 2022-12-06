import sys

file = open("input", "r")

match_sum = 0
loop = 0
group = []
for line in file:
    group.append(line.strip())
    loop += 1
    if loop == 3:
        loop = 0
        match = list(set.intersection(*map(set, group)))[0]
        match match.isupper():
            case False:
                match_sum += ord(match) - 96
            case True:
                match_sum += ord(match.lower()) - 70
        group = []

print("Part 2: {}".format(match_sum))
