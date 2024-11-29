def count_live_neighbors(grid, x, y):
    directions = [(-1, -1), (-1, 0), (-1, 1),
                  (0, -1),           (0, 1),
                  (1, -1),  (1, 0),  (1, 1)]
    size = len(grid)
    count = 0
    for dx, dy in directions:
        nx, ny = x + dx, y + dy
        if 0 <= nx < size and 0 <= ny < size and grid[nx][ny] == 1:
            count += 1
    return count

def next_generation(grid):
    size = len(grid)
    new_grid = [[0] * size for _ in range(size)]
    for x in range(size):
        for y in range(size):
            live_neighbors = count_live_neighbors(grid, x, y)
            if grid[x][y] == 1 and live_neighbors in (2, 3):
                new_grid[x][y] = 1
            elif grid[x][y] == 0 and live_neighbors == 3:
                new_grid[x][y] = 1
    return new_grid
