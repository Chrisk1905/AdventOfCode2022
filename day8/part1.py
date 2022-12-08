f = open("day8/input.txt")

grid = []

#how many trees are visible from outside the grid?
res = 0

for line in f:
    line = line.strip()
    grid_row = []
    for ch in line:
        grid_row.append( int(ch) )
    grid.append(grid_row)

# return True if tree is visible from path
def path_visible(path, height) -> bool:
    for tree in path:
        if tree >= height:
            return False
    return True

for row in range(len(grid)):
    for col in range( len(grid[0]) ):
        height = grid[row][col]
        if row == 0 or row == len(grid) - 1:
            res += 1
            continue
        if col == 0 or col == len(grid[0]) - 1:
            res += 1
            continue
        #check height of north south west east
        path = []
        #north 
        north_row = row - 1
        while(north_row >= 0):
            path.append( grid[north_row][col] )
            north_row -= 1
        if path_visible(path, height):
            print(row,col,height)
            res+=1
            continue
        path.clear()

        #south
        south_row = row + 1
        while(south_row < len(grid) ):
            path.append( grid[south_row][col] )
            south_row += 1
        if path_visible(path, height):
            print(row,col,height)
            res+=1
            continue
        path.clear()

        #west
        west_col = col - 1
        while(west_col >= 0):
            path.append(grid[row][west_col])
            west_col -= 1
        if path_visible(path, height):
            print(row,col,height)
            res += 1
            continue
        path.clear()
        
        #east
        east_col = col + 1
        while east_col < len(grid[0]):
            path.append(grid[row][east_col])
            east_col += 1
        if path_visible(path, height):
            print(row,col,height)
            res += 1
            continue
        path.clear()

print(res)
