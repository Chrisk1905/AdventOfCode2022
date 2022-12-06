# In how many assignment pairs do the ranges overlap?
f = open("input.txt", "r")

res = 0

for line in f.readlines():
    line = line.strip()
    line = line.split(",")
    elf1 = line[0].split("-")
    elf2 = line[1].split("-")
    start1, end1 = int(elf1[0]), int(elf1[1])
    start2, end2 = int(elf2[0]), int(elf2[1])
    
    if start1 <= start2 and start2 <= end1:
        res += 1
    elif start1 <= end2 and end2 <= end1:
        res += 1
    elif start2 <= start1 and start1 <= end2:
        res += 1
    elif start2 <= end1 and end1 <= end2:
        res += 1

    
print(res)