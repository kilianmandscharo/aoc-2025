from copy import deepcopy

with open("./04.txt", "r") as f:
    grid = list(map(lambda l: [c for c in l.strip()], f.readlines()))

height = len(grid)
width = len(grid[0])


def is_accessible(y, x, grid):
    if grid[y][x] != "@":
        return False
    neighbors = 0
    for i in range(-1, 2):
        for j in range(-1, 2):
            if i == 0 and j == 0:
                continue
            row = y + i
            col = x + j
            if row < 0 or row >= height or col < 0 or col >= width:
                continue
            if grid[row][col] == "@":
                neighbors += 1
    return neighbors < 4


def get_accessible_rolls(grid):
    rolls = []
    for y in range(0, height):
        for x in range(0, width):
            if is_accessible(y, x, grid):
                rolls.append((y, x))
    return rolls


def a():
    grid_a = deepcopy(grid)
    return len(get_accessible_rolls(grid_a))


def b():
    grid_b = deepcopy(grid)
    count = 0
    while True:
        rolls = get_accessible_rolls(grid_b)
        if len(rolls) == 0:
            break
        count += len(rolls)
        for y, x in rolls:
            grid_b[y][x] = "."
    return count


print("a:", a())
print("a:", b())
