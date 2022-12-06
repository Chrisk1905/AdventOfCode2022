sum = 0
max_sum = 0
with open('./input.txt') as f:
    for line in f.readlines():
        if line == "\n":
            max_sum = max(max_sum, sum)
            sum = 0
            continue
        n = int(line[:-1])
        sum += n

    print(max_sum)
