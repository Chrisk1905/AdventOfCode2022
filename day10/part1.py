from collections import deque

#Singal Strength the cycle number multiplied by the value of the X register
#return the sum of the signal strength during the 20th, 60th, 100th, 140th, 180th, and 220th cycles
f = open("day10/input.txt", "r")

res = []
check_cycles = deque([20,60,100,140,180,220,0])
cycle = 0
register = 1
check = check_cycles.popleft()
for line in f:
    line = line.strip()
    line = line.split(" ")
    
    if line[0] == "noop":
        cycle += 1
        if cycle == check:
            res.append( check * register )
            check = check_cycles.popleft()
    elif line[0] == "addx":
        for _ in range(2):
            cycle += 1
            if cycle == check:
                res.append(check * register)
                check = check_cycles.popleft()
        register += int(line[1])
    
print(sum(res))
