import sys

file = open("input", "r")

overlaps_fully = 0
overlaps = 0
for line in file:
    elf_1 = line.strip().split(",")[0]
    elf_2 = line.strip().split(",")[1]
    elf_1_start = int(elf_1.split("-")[0])
    elf_1_end = int(elf_1.split("-")[1])
    elf_2_start = int(elf_2.split("-")[0])
    elf_2_end = int(elf_2.split("-")[1])

    if elf_1_start >= elf_2_start and elf_1_end <= elf_2_end:
        overlaps_fully += 1
    elif elf_1_start <= elf_2_start and elf_1_end >= elf_2_end:
        overlaps_fully += 1

    elf1_list = list(range(elf_1_start, elf_1_end + 1))
    elf2_list = list(range(elf_2_start, elf_2_end + 1))

    if elf_1_end in elf2_list or elf_1_start in elf2_list:
        overlaps += 1
    elif elf_2_end in elf1_list or elf_2_start in elf1_list:
        overlaps += 1

print("Part 1: {}".format(overlaps_fully))
print("Part 2: {}".format(overlaps))
