import sys

file = open("input", "r")

lines = file.readlines()
divider = lines.index("\n")
stacks = lines[:divider - 1]
commands = lines[divider + 1:]
stack = {}
for i in range(1,10):
    stack[i] = []

for row in stacks:
    pos = 0
    for value in row[1::4]:
        pos += 1
        if value == " ":
            continue
        stack[pos].append(value)

for command in commands:
    ammount = int(command.split(" ")[1])
    from_stack = int(command.split(" ")[3])
    to_stack = int(command.split(" ")[5])
    for _ in range(ammount):
        crate = stack[from_stack].pop(0)
        stack[to_stack].insert(0, crate)

output = ""
for index in stack:
    output += stack[index][0]

print("Part 1: {}".format(output))
