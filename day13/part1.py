with open("day13/input.in") as fin:
    parts = fin.read().strip().split("\n\n")

res = []

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

for i, packet_pair in enumerate(parts):
    packet_pair = packet_pair.split("\n")
    p1, p2 = map(eval, packet_pair)
    if compare(p1, p2) == 1:
        res.append( i + 1 )

print(res, sum(res))