import heapq
from enum import Enum, auto


class Cell(Enum):
    Wall = auto()
    Path = auto()


Coord = tuple[int, int]
Grid = dict[Coord, Cell]


class Direction(Enum):
    East = auto()
    South = auto()
    West = auto()
    North = auto()

    def __lt__(self, other):
        if not isinstance(other, Direction):
            raise RuntimeError
        return self.value.__lt__(other.value)

    def rotate_right(self):
        return Direction(self.value % 4 + 1)

    def rotate_left(self):
        return Direction((self.value - 2) % 4 + 1)

    def move(self, coord: Coord) -> Coord:
        x, y = coord
        match self:
            case Direction.East:
                return x + 1, y
            case Direction.South:
                return x, y + 1
            case Direction.West:
                return x - 1, y
            case Direction.North:
                return x, y - 1


def parse(s: str) -> tuple[Grid, Coord, Coord]:
    grid: Grid = dict()
    for y, row in enumerate(s.splitlines()):
        for x, cell in enumerate(row):
            coord = (x, y)
            if cell == "#":
                grid[coord] = Cell.Wall
            else:
                grid[coord] = Cell.Path

            if cell == "S":
                start = coord
            elif cell == "E":
                end = coord

    return grid, start, end


def solve(grid: Grid, start: Coord, end: Coord) -> int:
    to_visit: list[tuple[int, Coord, Direction]] = []
    scores: dict[tuple[Coord, Direction], int] = dict()
    heapq.heappush(to_visit, (0, start, Direction.East))
    scores[(start, Direction.East)] = 0

    try:
        while current := heapq.heappop(to_visit):
            score, coord, direction = current
            forward_coord = direction.move(coord)

            if grid[forward_coord] != Cell.Wall:
                previous_score = scores.get((forward_coord, direction))
                if not previous_score or previous_score > score + 1:
                    heapq.heappush(to_visit, (score + 1, forward_coord, direction))
                    scores[(forward_coord, direction)] = score + 1

            for new_dir in [direction.rotate_left(), direction.rotate_right()]:
                previous_score = scores.get((coord, new_dir))
                if not previous_score or previous_score > score + 1000:
                    heapq.heappush(to_visit, (score + 1000, coord, new_dir))
                    scores[(coord, new_dir)] = score + 1000


    except IndexError:
        paths_to_end = []
        for (coord, _), score in scores.items():
            if coord == end:
                paths_to_end.append(score)

        return min(paths_to_end)


def main(s: str):
    grid, start, end = parse(s)
    print(solve(grid, start, end))


if __name__ == "__main__":
    main(in_)
