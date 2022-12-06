priority_map = {}
priority = 1
for i in range(97, 123):
    priority_map[chr(i)] = priority
    priority += 1

for i in range(65, 91):
    priority_map[chr(i)] = priority
    priority += 1

res = 0
with open('./input.txt') as f:
    for line in f.readlines():
        line.strip()
        mid = len(line) // 2
        first_compartment = line[ : mid]
        first_set = set()
        for c in first_compartment:
            first_set.add(c)
        
        

        second_compartment = line[mid:]
        for c in second_compartment:
            if c in first_set:
                res += priority_map[c]
                break

print(res)
