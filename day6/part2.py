f = open("day6/input.txt")

res = []

for line in f:
    line = line.strip()
    l = 0
    char_set = set()
    for r in range(14, len(line)):
        l = r - 14
        for c in line[l:r]:
            char_set.add(c)
        if len(char_set) == 14:
            print(line[l:r])
            res.append(r)
            break
        char_set.clear()

print(res)