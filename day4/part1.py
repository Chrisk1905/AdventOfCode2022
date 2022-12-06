#In how many assignment pairs does one range fully contain the other?

f = open("input.txt", "r")

res = 0

for line in f.readlines():
    line = line.strip()
    line = line.split(",")
    elf1 = line[0].split("-")
    elf2 = line[1].split("-")
    start1, end1 = int(elf1[0]), int(elf1[1])
    start2, end2 = int(elf2[0]), int(elf2[1])
    
    if start1 <= start2 and end2 <= end1:
        res += 1
        print(elf1, elf2)
    elif start2 <= start1 and end1 <= end2:
        res += 1
        print(elf1, elf2)
    
print(res)