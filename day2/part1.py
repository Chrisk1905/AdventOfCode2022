with open('./input2.txt') as f:

    score = 0

    for line in f.readlines():
        opp = line[0]
        me = line [2]
        # A Rock B Paper C Siccors
        # X Rock Y Paper C Siccors
        if opp == "A":
            if me == "X":
                score += 1 + 3
            if me == "Y":
                score += 2 + 6
            if me == "Z":
                score += 3
        if opp == "B":
            if me == "X":
                score += 1 
            if me == "Y":
                score += 2 + 3
            if me == "Z":
                score += 3 + 6
        if opp == "C":
            if me == "X":
                score += 1 + 6
            if me == "Y":
                score += 2 
            if me == "Z":
                score += 3 + 3

    print(score)

