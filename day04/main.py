def directions(x: int, y: int):
    yield from [
        [(x - 1, y - 1), (x - 2, y - 2), (x - 3, y - 3)],
        [(x - 1, y), (x - 2, y), (x - 3, y)],
        [(x - 1, y + 1), (x - 2, y + 2), (x - 3, y + 3)],
        [(x, y + 1), (x, y + 2), (x, y + 3)],
        [(x + 1, y + 1), (x + 2, y + 2), (x + 3, y + 3)],
        [(x + 1, y), (x + 2, y), (x + 3, y)],
        [(x + 1, y - 1), (x + 2, y - 2), (x + 3, y - 3)],
        [(x, y - 1), (x, y - 2), (x, y - 3)],
    ]


def part1(grid):
    count = 0
    for y in range(len(grid)):
        for x in range(len(grid[0])):
            if grid[y][x] == "X":
                for (x1, y1), (x2, y2), (x3, y3) in directions(x, y):
                    if x3 < 0 or y3 < 0 or x3 >= len(grid[0]) or y3 >= len(grid):
                        continue
                    if grid[y1][x1] == "M" and grid[y2][x2] == "A" and grid[y3][x3] == "S":
                        count += 1
    print(count)


def part2(grid):
    count = 0
    for y in range(1, len(grid) - 1):
        for x in range(1, len(grid[0]) - 1):
            if grid[y][x] == "A":
                mas1 = (grid[y - 1][x - 1] == "M" and grid[y + 1][x + 1] == "S") or (grid[y - 1][x - 1] == "S" and grid[y + 1][x + 1] == "M")
                mas2 = (grid[y + 1][x - 1] == "M" and grid[y - 1][x + 1] == "S") or (grid[y + 1][x - 1] == "S" and grid[y - 1][x + 1] == "M")
                if mas1 and mas2:
                    count += 1
    print(count)


if __name__ == "__main__":
    m = [list(line) for line in in_.splitlines()]

    part1(m)
    part2(m)

