from typing import Any


def parse(s: str) -> dict[tuple[int, int], str]:
    grid: dict[tuple[int, int], str] = {}
    rows = s.splitlines()
    for y, row in enumerate(rows):
        for x, cell in enumerate(row):
            coord = (int(x), int(y))
            grid[coord] = cell

    return grid


def adjacent_coords(coord: tuple[int, int]) -> list[tuple[int, int]]:
    x, y = coord
    result = []
    for x_shift, y_shift in [(-1, 0), (0, -1), (1, 0), (0, 1)]:
        new_x, new_y = x + x_shift, y + y_shift
        result.append((new_x, new_y))

    return result


def reachable_coords(grid: dict[tuple[int, int], Any], coord: tuple[int, int]) -> list[tuple[int, int]]:
    return [(x, y) for x, y in adjacent_coords(coord) if (x, y) in grid]


def build_plots(grid: dict[tuple[int, int], str]) -> list[tuple[int, int, int]]:
    seen: set[tuple[int, int]] = set()
    plots: list[tuple[int, int, int]] = []
    for coord, value in grid.items():
        if coord in seen:
            continue

        area, perimeter, corners = 0, 0, 0
        to_process: list[tuple[int, int]] = [coord]
        while to_process and (current_coord := to_process.pop(0)):
            if current_coord in seen:
                continue
            seen.add(current_coord)

            adjacent = adjacent_coords(current_coord)
            reachable = reachable_coords(grid, current_coord)
            adjacent_same_plant = [c for c in reachable if grid[c] == value]
            to_process.extend(adjacent_same_plant)

            oob_perimeter = 4 - len(reachable)
            plot_change_perimeter = 4 - len(adjacent_same_plant) - oob_perimeter

            # well that's not pretty...
            cell_corners = 0
            for i in range(-1, 3):
                c1, c2 = adjacent[i], adjacent[i + 1]
                diag_x = c1[0] + c2[0] - current_coord[0]
                diag_y = c1[1] + c2[1] - current_coord[1]
                diag: str = grid.get((diag_x, diag_y))
                if grid.get(c1) != value and grid.get(c2) != value:
                    cell_corners += 1
                elif grid.get(c1) == value and grid.get(c2) == value and diag != value:
                    cell_corners += 1

            area += 1
            perimeter += oob_perimeter + plot_change_perimeter
            corners += cell_corners

        plots.append((area, perimeter, corners))

    return plots


def part1(plots: list[tuple[int, int, int]]) -> int:
    result = sum(area * perimeter for area, perimeter, _ in plots)
    print(result)
    return result


def part2(plots: list[tuple[int, int, int]]) -> int:
    result = sum(area * corners for area, _, corners in plots)
    print(result)
    return result


def main(s):
    grid = parse(s)
    plots = build_plots(grid)
    part1(plots)
    part2(plots)


if __name__ == "__main__":
    main(in_)

