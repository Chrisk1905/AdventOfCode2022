from collections import deque

#Singal Strength the cycle number multiplied by the value of the X register
#return the sum of the signal strength during the 20th, 60th, 100th, 140th, 180th, and 220th cycles
f = open("day10/input.txt", "r")
out = open("day10/out.txt", "w")


def drawCRT(crt_line: list[str] , col, reg):
    for i in range(reg - 1, reg + 2):
        if col == i:
            crt_line[col] = "#"

cycle = 0
row = 0
crt = [['.' for _ in range(40)] for _ in range(6)]
register = 1

for line in f:
    line = line.strip()
    line = line.split(" ")
    
    if line[0] == "noop":
        row = cycle // 40
        drawCRT( crt[row], cycle % 40, register)
        cycle += 1
    elif line[0] == "addx":
        for _ in range(2):
            row = cycle // 40
            drawCRT(crt[row], cycle % 40, register)
            cycle += 1
        register += int(line[1])

for i in range(len(crt)):
    for j in range(len(crt[0])):
        out.write(str(crt[i][j]))
    out.write("\n")