#scenic score is found by multiplying together its viewing distance in each of the four directions
#What is the highest scenic score possible for any tree?
f = open("day8/test.txt")
res = 0

grid = [] 
for line in f:
    line = line.strip()
    grid_row = []
    for ch in line:
        grid_row.append( int(ch) )
    grid.append(grid_row)

# number of tree visible
def path_scenic_score(path, height) -> int:
    trees_visible = 0
    for tree in path:
        if tree >= height:
            trees_visible += 1
            return trees_visible
        else:
            trees_visible += 1
    return trees_visible

for row in range(len(grid)):
    for col in range( len(grid[0]) ):
        height = grid[row][col]
        if row == 0 or row == len(grid) - 1:
            continue
        if col == 0 or col == len(grid[0]) - 1:
            continue

        #check height of north south east west
        path_scenic_scores = [0,0,0,0]
        path = []
        #north 
        north_row = row - 1
        while(north_row >= 0):
            path.append( grid[north_row][col] )
            north_row -= 1
        path_scenic_scores[0] = path_scenic_score(path, height)
        path.clear()

        #south
        south_row = row + 1
        while(south_row < len(grid) ):
            path.append( grid[south_row][col] )
            south_row += 1
        path_scenic_scores[1] = path_scenic_score(path, height)
        path.clear()

        #west
        west_col = col - 1
        while(west_col >= 0):
            path.append(grid[row][west_col])
            west_col -= 1
        path_scenic_scores[2] = path_scenic_score(path, height)
        path.clear()
        
        #east
        east_col = col + 1
        while east_col < len(grid[0]):
            path.append(grid[row][east_col])
            east_col += 1
        path_scenic_scores[3] = path_scenic_score(path, height)
        path.clear()

        tree_scenic_score = path_scenic_scores[0]
        for i in range(1, len(path_scenic_scores)):
            tree_scenic_score *= path_scenic_scores[i]
        
        res = max(tree_scenic_score, res)
        

print(res)
