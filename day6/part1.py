f = open("day6/input.txt")

res = []

for line in f:
    line = line.strip()
    l = 0
    char_set = set()
    for r in range(4, len(line)):
        l = r - 4
        for c in line[l:r]:
            char_set.add(c)
        if len(char_set) == 4:
            print(line[l:r])
            res.append(r)
            break
        char_set.clear()

print(res)