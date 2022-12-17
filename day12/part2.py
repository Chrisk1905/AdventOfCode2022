from collections import deque

f = open("day12/input.txt", "r")
out = open("day12/out.txt", "w")

char_map = {'S':0 ,'E':25 }
for i in range(97, 123):
    char_map[chr(i)] = i - 97

grid = []
start = [0,0]
end = [0,0]

row, col = 0 ,0
for line in f:
    line = line.strip()
    elavation = []
    for c in line:
        elavation.append(c)
        if c == "S":
            start[0], start[1] = row, col
        if c == "E":
            end[0], end[1] = row, col
        col += 1
    grid.append(elavation)
    col = 0
    row += 1

#shortest path from start to end
num_rows, num_cols = len(grid), len(grid[0])

def get_neighbors(root : tuple[int,int]):
    row, col = root
    root_elavation = char_map[grid[row][col]]
    delta_row = [-1, 0, 1, 0]
    delta_col = [0, 1, 0, -1]
    res = []
    for i in range(len(delta_row)):
        neighbor_row = row + delta_row[i]
        neighbor_col = col + delta_col[i]
        
        if 0 <= neighbor_row < num_rows and 0 <= neighbor_col < num_cols:
            neighbor_elevation = char_map[grid[neighbor_row][neighbor_col]]
            if neighbor_elevation <= root_elavation+1:
                res.append((neighbor_row, neighbor_col))
    return res

def bfs(starting_node, end):
    queue = deque([starting_node])
    visited = set([starting_node])
    level = 0
    while len(queue) > 0:
        n = len(queue)
        for i in range(n):
            node = queue.popleft()
            out.write(str(node) + "\n")
            if(node == end):
                return level
            for neighbor in get_neighbors(node):
                if neighbor in visited:
                    continue                
                queue.append(neighbor)
                visited.add(neighbor)
        level += 1
    return -1

start = (start[0],start[1])
end = (end[0], end[1])

starting_points = [start]

for i in range(num_rows):
    for j in range(num_cols):
        if grid[i][j] == "a":
            starting_points.append((i,j))

min_path = num_cols * num_rows

for s in starting_points:
    path_len = bfs(s, end)
    if path_len > 0:
        min_path = min(path_len, min_path)

print(min_path)
