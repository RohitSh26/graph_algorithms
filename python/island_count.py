"""
island count

Write a function, island_count, that takes in a grid containing Ws and Ls.
W represents water and L represents land. 
The function should return the number of islands on the grid. 
An island is a vertically or horizontally connected region of land.

grid = [
  ['W', 'L', 'W', 'W', 'W'],
  ['W', 'L', 'W', 'W', 'W'],
  ['W', 'W', 'W', 'L', 'W'],
  ['W', 'W', 'L', 'L', 'W'],
  ['L', 'W', 'W', 'L', 'L'],
  ['L', 'L', 'W', 'W', 'W'],
]
"""

def island_count(grid):

    visited = set()
    count = 0

    # let's loop through all the elements of the grid
    for r in range(len(grid)):
        for c in range(len(grid[0])):
            if traverse_grid(grid, r, c, visited) == True:
              count += 1
    return count

def traverse_grid(grid, r, c, visited):
    # check if the r and c are in bounds
    if not (0 <= r < len(grid)) or not (0 <= c < len(grid[0])):
        return False

    # if you reach water return
    if grid[r][c] == 'W':
        return False

    # create a way to figure out the positions you have visited
    visited_node = str(r) + ',' + str(c)

    # check if already visited
    if visited_node in visited:
        return False

    # otherwise add the current node to visited
    visited.add(visited_node)

    # Now we can traverse in the Land area up, down, left and right
    traverse_grid(grid, r + 1, c, visited)
    traverse_grid(grid, r - 1, c, visited)
    traverse_grid(grid, r, c - 1, visited)
    traverse_grid(grid, r, c + 1, visited)

    return True

grid = [
    ['W', 'L', 'W', 'W', 'W'],
    ['W', 'L', 'W', 'W', 'W'],
    ['W', 'W', 'W', 'L', 'W'],
    ['W', 'W', 'L', 'L', 'W'],
    ['L', 'W', 'W', 'L', 'L'],
    ['L', 'L', 'W', 'W', 'W'],
]

print(island_count(grid))  # -> 3
