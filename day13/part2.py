from functools import cmp_to_key

with open("day13/input.in") as fin:
    parts = fin.read().strip().split("\n\n")

res = 1

def compare(p1, p2):
    if isinstance(p1, int) and isinstance(p2, int):
        if p1 < p2:
            return 1
        if p1 == p2:
            return 0
        return -1

    if isinstance(p1, list) and isinstance(p2, int):
        p2 = [p2]
    if isinstance(p1, int) and isinstance(p2, list):
        p1 = [p1]

    i = 0
    while i < len(p1) and i < len(p2):
        compare_res = compare(p1[i], p2[i])
        if compare_res == 1:
            return 1
        elif compare_res == -1:
            return -1
        i += 1
    
    if i == len(p1):
        if len(p1) == len(p2):
            return 0
        if len(p1) < len(p2):
            return 1
    return -1

packets = [[[2]],[[6]]]

for packet_pair in parts:
    packet_pair = packet_pair.split("\n")
    for p in map(eval, packet_pair):
        packets.append(p)

packets.sort(key=cmp_to_key(compare), reverse=True)

for i, p in enumerate(packets):
    if p == [[2]] or p == [[6]]:
        res *= i + 1

print(res)