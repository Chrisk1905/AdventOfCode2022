from collections import deque

f = open("day5/input.txt", "r")

res = []
stacks = []

#create stacks
for line in f:
    line = line.strip()
    if line == "Instruction":
        break
    line = line.split(":")
    line = line[1].split(",")
    q = deque(line)
    stacks.append(q)


#do instructions
for line in f:
    line = line.strip()
    line = line.split(" ")
    move = int(line[1])
    frm = int(line[3])
    to = int(line[5])

    temp_stack = deque()
    for _ in range(move):
        crate = stacks[frm-1].pop()
        temp_stack.append(crate)
    for _ in range(len(temp_stack)):
        crate = temp_stack.pop()
        stacks[to-1].append(crate)

for stack in stacks:
    if len(stack) == 0:
        res.append("_")
    else:
        crate = stack.pop()
        res.append(crate)

for c in res:
    print(c, end="")
print("\n")
