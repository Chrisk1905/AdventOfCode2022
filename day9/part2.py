f = open("day9/test2.txt", "r")
out = open("day9/out.txt", "w")

rope = [[0,0] for _ in range(10)]
tailset = set([tuple(rope[9])])

touching_deltas = [(1,0), (-1,0), (0,1), (0,-1), (1,1), (-1,1), (1,-1), (-1,-1)]
up_deltas = [(-1,2),(0,2),(1,2)]
down_deltas = [(-1,-2),(0,-2),(1,-2)]
left_deltas = [(-2,1),(-2,0),(-2,-1)]
right_detlas = [(2,1),(2,0),(2,-1)]

#returns true if touching
def touching(H: list[int], T: list[int])->bool:
    if T[0] == H[0] and T[1] == H[1]:
        return True

    for delta in touching_deltas:
        dH = [0,0]
        dH[0] = H[0] + delta[0]
        dH[1] = H[1] + delta[1]
        if T == dH:
            return True

    return False

#transforms Tail
def move_tail(H: list[int], T: list[int])->None:
    for delta in up_deltas:
        dH = [0,0]
        dH[0] = H[0] + delta[0]
        dH[1] = H[1] + delta[1]
        if T == dH:
            T[0] = H[0]
            T[1] = H[1] + 1
            return
    for delta in down_deltas:
        dH = [0,0]
        dH[0] = H[0] + delta[0]
        dH[1] = H[1] + delta[1]
        if T == dH:
            T[0] = H[0]
            T[1] = H[1] - 1
            return
    for delta in left_deltas:
        dH = [0,0]
        dH[0] = H[0] + delta[0]
        dH[1] = H[1] + delta[1]
        if T == dH:
            T[0] = H[0] - 1
            T[1] = H[1]
            return
    for delta in right_detlas:
        dH = [0,0]
        dH[0] = H[0] + delta[0]
        dH[1] = H[1] + delta[1]
        if T == dH:
            T[0] = H[0] + 1
            T[1] = H[1]
            return
    #top left (-2,2)
    dH = [0,0]
    dH[0] = H[0] - 2 
    dH[1] = H[1] + 2
    if T == dH:
        T[0] = H[0] - 1
        T[1] = H[1] + 1
        return
    #top right
    dH[0] = H[0] + 2 
    dH[1] = H[1] + 2
    if T == dH:
        T[0] = H[0] + 1
        T[1] = H[1] + 1
        return
    #bottom left
    dH[0] = H[0] - 2 
    dH[1] = H[1] - 2
    if T == dH:
        T[0] = H[0] - 1
        T[1] = H[1] - 1
        return
    #bottom right
    dH[0] = H[0] + 2 
    dH[1] = H[1] - 2
    if T == dH:
        T[0] = H[0] + 1
        T[1] = H[1] - 1
        return
    
for line in f:
    line = line.strip()
    line = line.split(" ")
    magnitude = int(line[1])
    print(rope, file=out)
    if line[0] == "R":
        for _ in range(magnitude):
            #move the head
            rope[0][0] = rope[0][0] + 1
            
            #see if head and tail touch
            for i in range(9):
                if not touching(rope[i], rope[i + 1]):
                    move_tail(rope[i], rope[i + 1])
            tailset.add(tuple(rope[9]))
    elif line[0] == "L":
        for _ in range(magnitude):
            rope[0][0] = rope[0][0] - 1

            for i in range(9):
                if not touching(rope[i], rope[i + 1]):
                    move_tail(rope[i], rope[i + 1])
            tailset.add(tuple(rope[9]))
    elif line[0] == "U":
        for _ in range(magnitude):
            rope[0][1] = rope[0][1] + 1

            for i in range(9):
                if not touching(rope[i], rope[i + 1]):
                    move_tail(rope[i], rope[i + 1])
            tailset.add(tuple(rope[9]))
    elif line[0] == "D":
        for _ in range(magnitude):
            rope[0][1] = rope[0][1] - 1

            for i in range(9):
                if not touching(rope[i], rope[i + 1]):
                    move_tail(rope[i], rope[i + 1])
            tailset.add(tuple(rope[9]))
    print(line, file=out)


print( len(tailset) )
