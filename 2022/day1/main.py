import sys

file = open("input", "r")

elfs={}
elf=0
cal=0
for line in file:
    if line == '\n':
        elfs[elf]=cal
        elf += 1
        cal=0
    else:
        cal += int(line.strip())

elfs_sorted = sorted(elfs, key=elfs.get, reverse=True)

print("Part 1: {}".format(elfs[elfs_sorted[0]]))

top3 = elfs[elfs_sorted[0]] + elfs[elfs_sorted[1]] + elfs[elfs_sorted[2]]
print("Part 2: {}".format(top3))
