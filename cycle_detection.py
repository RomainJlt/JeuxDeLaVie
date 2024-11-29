def detect_cycle(grid, history):
    grid_tuple = tuple(tuple(row) for row in grid)
    if grid_tuple in history:
        return True, history.index(grid_tuple)
    history.append(grid_tuple)
    return False, -1
