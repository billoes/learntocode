def count_neighbord(grid, row, col):
    count = 0
    if row-1 >= 0:
        count = count + grid[row-1][col]
    if (row-1 >= 0) and (col-1 >=0):
        count = count + grid[row-1][col-1]
    if (row-1 >= 0) and (col+1 > width):
        count = count + grid[row-1][col+1]
    if col-1 >= 0:
        count = count + grid[row][col-1]
    if col + 1 < width:
        count = count + grid[row][col+1]
    if row + 1 < height:
        count = count + grid[row+1][col]
    if (row + 1 < height) and (col-1 >= 0):
        count = count + grid[row+1][col-1]
    if (row + 1 < height) and (col+1 < width):
        count = count + grid[row+1][col+1]
    return count

    


    