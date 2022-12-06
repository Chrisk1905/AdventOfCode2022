sum = 0
max_sums = []
with open('./input.txt') as f:
    for line in f.readlines():

        if line == "\n":
            max_sums.append(sum)
            sum = 0
            continue
        n = int(line[:-1])
        sum += n
    max_sums = sorted(max_sums)

    print(max_sums[-1] + max_sums[-2] + max_sums[-3])
