import sys

file = open("input", "r")
stream = file.read().strip()
buffer = []
for pos in range(len(stream)):
    buffer.append(stream[pos])
    buffer = buffer[-4:]
    if len(set(buffer)) == 4:
        print("Part 1: {}".format(pos + 1))
        break
buffer = []

for pos in range(len(stream)):
    buffer.append(stream[pos])
    buffer = buffer[-14:]
    if len(set(buffer)) == 14:
        print("Part 2: {}".format(pos + 1))
        break
