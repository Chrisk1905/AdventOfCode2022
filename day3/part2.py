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
    three_lines = []
    for line in f.readlines():
        line = line.strip()
        three_lines.append(line)
        if len(three_lines) == 3:
            print(three_lines)
            # search for the common char
            first_set = set()
            for ch in three_lines[0]:
                first_set.add(ch)
            second_set = set()
            for ch in three_lines[1]:
                if ch in first_set:
                    second_set.add(ch)
            
            for ch in three_lines[2]:
                if ch in second_set:
                    print(ch)
                    res += priority_map[ch]
                    break

            three_lines.clear()

print(res)
