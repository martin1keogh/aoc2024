import re
from collections import defaultdict
from dataclasses import dataclass


@dataclass(frozen=True)
class Robot:
    x: int
    y: int
    dx: int
    dy: int

    def move(self, nx, ny):
        return Robot(nx, ny, self.dx, self.dy)


@dataclass
class Grid:
    x_max: int
    y_max: int
    robots: set[Robot]

    def __str__(self):
        grid = []
        for y in range(self.y_max):
            row = [0] * self.x_max
            grid.append(row)

        for r in self.robots:
            grid[r.y][r.x] += 1

        grid_str = ["".join(str(c or ".") for c in row) for row in grid]
        return "\n".join(grid_str)

    def step(self):
        new_robots = set()
        for robot in self.robots:
            nx = (robot.x + robot.dx) % self.x_max
            ny = (robot.y + robot.dy) % self.y_max
            robot = robot.move(nx, ny)
            if robot in new_robots:
                raise
            new_robots.add(robot)

        self.robots = new_robots

    def score(self):
        quadrants = defaultdict(int)
        for robot in self.robots:
            x_threshold = self.x_max // 2
            y_threshold = self.y_max // 2
            if robot.x == x_threshold or robot.y == y_threshold:
                continue
            quadrants[(robot.x < x_threshold, robot.y < y_threshold)] += 1

        res = 1
        for q in quadrants.values():
            if q:
                res *= q

        return res


def parse(s: str) -> set[Robot]:
    r = re.compile(r"p=(-?\d+),(-?\d+) v=(-?\d+),(-?\d+)")
    robots: set[Robot] = set()
    for line in s.splitlines():
        match = re.match(r, line)
        x, y, dx, dy = match.groups()
        robot = Robot(int(x), int(y), int(dx), int(dy))
        if robot in robots:
            print("dup robot found, change set to list or something")
        robots.add(robot)
    return robots


def main(s: str):
    robots = parse(s)
    grid = Grid(101, 103, robots)
    for _ in range(100):
        grid.step()

    print(grid.score())


if __name__ == "__main__":
    main(in_)
