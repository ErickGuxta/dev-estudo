def count_neighbors(grid, row, col, n):
    count = 0
    for i in range(-1, 2):
        for j in range(-1, 2):
            if i == 0 and j == 0:
                continue
            new_row, new_col = row + i, col + j
            if 0 <= new_row < n and 0 <= new_col < n:
                count += int(grid[new_row][new_col])
    return count

def next_state(grid, n):
    new_grid = [['0' for _ in range(n)] for _ in range(n)]
    
    for i in range(n):
        for j in range(n):
            neighbors = count_neighbors(grid, i, j, n)
            current = grid[i][j]
            
            if current == '0':  # Dead cell
                if neighbors == 3:
                    new_grid[i][j] = '1'
            else:  # Live cell
                if neighbors == 2 or neighbors == 3:
                    new_grid[i][j] = '1'
    
    return new_grid

# Read input
n, q = map(int, input().split())
grid = [list(input()) for _ in range(n)]

# Simulate Q steps
for _ in range(q):
    grid = next_state(grid, n)

# Print final state
for row in grid:
    print(''.join(row))
