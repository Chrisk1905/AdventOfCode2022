f = open("day9/input.txt", "r")

H,T = [0,0], [0,0]
tailset = set([tuple(T)])

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
    for delta in down_deltas:
        dH = [0,0]
        dH[0] = H[0] + delta[0]
        dH[1] = H[1] + delta[1]
        if T == dH:
            T[0] = H[0]
            T[1] = H[1] - 1
    for delta in left_deltas:
        dH = [0,0]
        dH[0] = H[0] + delta[0]
        dH[1] = H[1] + delta[1]
        if T == dH:
            T[0] = H[0] - 1
            T[1] = H[1]
    for delta in right_detlas:
        dH = [0,0]
        dH[0] = H[0] + delta[0]
        dH[1] = H[1] + delta[1]
        if T == dH:
            T[0] = H[0] + 1
            T[1] = H[1]
    

for line in f:
    line = line.strip()
    line = line.split(" ")
    magnitude = int(line[1])
    print(line)
    print(T,H)
    if line[0] == "R":
        #direction right
        for _ in range(magnitude):
            #move the head
            H[0] = H[0] + 1
            #see if head and tail touch
            if touching(H, T):
                continue
            else:
                move_tail(H, T)
                tailset.add(tuple(T))
    elif line[0] == "L":
        # left 
        for _ in range(magnitude):
            H[0] = H[0] - 1
            if touching(H, T):
                continue
            else:
                move_tail(H, T)
                tailset.add(tuple(T))
    elif line[0] == "U":
        for _ in range(magnitude):
            H[1] = H[1] + 1
            if touching(H, T):
                continue
            else: 
                move_tail(H, T)
                tailset.add(tuple(T))
    elif line[0] == "D":
        for _ in range(magnitude):
            H[1] = H[1] - 1
            if touching(H, T):
                continue
            else:
                move_tail(H, T)
                tailset.add(tuple(T))
    
print(tailset)
print( len(tailset) )
