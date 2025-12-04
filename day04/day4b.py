f = open("input")

raw = f.readlines()

grid = [list(l.strip()) for l in raw]

def get_neighbours(x, y, grid):
    neighbours = set()
    for dx, dy in [(1, 0), (-1, 0), (0, 1), (0, -1), (1, 1), (1, -1), (-1, 1), (-1, -1)]:
        x1, y1 = x+dx, y+dy
        if 0 <= x1 and x1 < len(grid[0]) and 0 <= y1 and y1 < len(grid):
            neighbours.add((x1, y1))
    return neighbours

num_accessible = 0
while True:
    num_removed = 0
    for y in range(len(grid)):
        for x in range(len(grid[y])):
            if grid[y][x] == '@':
                neighbours = get_neighbours(x, y, grid)
                num_rolls = 0
                for nx, ny in neighbours:
                    if grid[ny][nx] == '@':
                        num_rolls += 1
                if num_rolls < 4:
                    num_removed += 1 
                    grid[y][x] = '_'
    if num_removed == 0:
        break
    num_accessible += num_removed

print(num_accessible)