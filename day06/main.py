from dataclasses import dataclass
from enum import Enum
from typing import Self


@dataclass(frozen=True)
class Coord:
    x: int
    y: int

    def __add__(self, other: (int, int)) -> Self:
        (other_x, other_y) = other
        return Coord(self.x + other_x, self.y + other_y)


Grid = dict[Coord, str]


class Direction(Enum):
    Up = 1
    Right = 2
    Down = 3
    Left = 4

    def turn_right(self):
        return Direction(self.value % 4 + 1)

    def movement(self):
        match self:
            case Direction.Up:
                return 0, -1
            case Direction.Right:
                return 1, 0
            case Direction.Down:
                return 0, 1
            case Direction.Left:
                return -1, 0


def parse(s) -> Grid:
    as_2d_array: list[list[str]] = [list(row) for row in s.splitlines()]
    as_dict: Grid = {}
    for y in range(len(as_2d_array)):
        for x in range(len(as_2d_array[0])):
            as_dict[Coord(x, y)] = as_2d_array[y][x]

    return as_dict


def find_initial_position(grid: Grid) -> Coord:
    for coord, cell in grid.items():
        if cell == "^":
            return coord


def trace_path(grid: Grid, initial_position: Coord):
    path = {(initial_position, Direction.Up)}
    position = initial_position
    direction = Direction.Up
    is_cycle = False
    while True:
        try:
            next_position = position + direction.movement()
            next_cell = grid[next_position]

            if (next_position, direction) in path:
                is_cycle = True
                break

            if next_cell == ".":
                position = next_position
                path.add((position, direction))

            elif next_cell == "#":
                direction = direction.turn_right()

        except KeyError:
            break

    return path, is_cycle


def part1(grid: Grid, initial_position: Coord) -> int:
    path, _ = trace_path(grid, initial_position)
    return len(set(pos for pos, _ in path))


def part2(grid: Grid, initial_position: Coord):
    original_path, _ = trace_path(grid, initial_position)
    original_path_coord = set(coord for coord, _ in original_path)
    original_path_coord.remove(initial_position)
    result = 0
    for coord in original_path_coord:
        if grid[coord] == ".":
            grid_ = grid.copy()
            grid_[coord] = "#"
            _, is_cycle = trace_path(grid_, initial_position)
            if is_cycle:
                result += 1

    return result


def main(s):
    grid = parse(s)
    initial_position = find_initial_position(grid)
    grid[initial_position] = "."
    print(part1(grid, initial_position))
    print(part2(grid, initial_position))


if __name__ == "__main__":
    main(in_)

