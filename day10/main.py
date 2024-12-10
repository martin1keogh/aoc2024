from typing import Iterator


def parse(s: str) -> tuple[dict[tuple[int, int], int], list[tuple[int, int]]]:
    grid: dict[tuple[int, int], int] = {}
    trailheads = []
    rows = s.splitlines()
    for y, row in enumerate(rows):
        for x, cell in enumerate(row):
            coord = (int(x), int(y))
            grid[coord] = int(cell)
            if cell == "0":
                trailheads.append(coord)

    return grid, trailheads


def reachable_adjacent_coords(grid: dict[tuple[int, int], int], coord: tuple[int, int]) -> Iterator[tuple[int, int]]:
    x, y = coord
    for x_shift, y_shift in [(-1, 0), (1, 0), (0, -1), (0, 1)]:
        new_x, new_y = x + x_shift, y + y_shift
        if (height := grid.get((new_x, new_y))) and height == grid[(x, y)] + 1:
            yield new_x, new_y


def score(grid: dict[tuple[int, int], int], trailhead: tuple[int, int]) -> Iterator[tuple[int, int]]:
    def rec(coord: tuple[int, int]):
        for next_coord in reachable_adjacent_coords(grid, coord):
            if grid[next_coord] == 9:
                yield next_coord
            else:
                yield from rec(next_coord)

    return rec(trailhead)


def part1(grid: dict[tuple[int, int], int], trailheads: list[tuple[int, int]]) -> int:
    result = sum(
        len(set(paths))
        for paths
        in map(lambda trailhead: score(grid, trailhead), trailheads)
    )
    print(result)
    return result


def part2(grid: dict[tuple[int, int], int], trailheads: list[tuple[int, int]]) -> int:
    result = sum(
        len(list(paths))
        for paths
        in map(lambda trailhead: score(grid, trailhead), trailheads)
    )
    print(result)
    return result


def main(s: str):
    grid, trailheads = parse(s)
    part1(grid, trailheads)
    part2(grid, trailheads)


if __name__ == "__main__":
    main(in_)

