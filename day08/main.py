from collections import defaultdict
from itertools import permutations


def parse(s: str):
    result: dict[str, list[(int, int)]] = defaultdict(list)
    rows = s.splitlines()
    max_y = len(rows)
    max_x = len(rows[0])
    for y, row in enumerate(rows):
        for x, cell in enumerate(row):
            if cell != ".":
                result[cell].append((x, y))

    return result, (max_x, max_y)


def _solve(antennas: dict[str, list[(int, int)]], max_dim: (int, int), p2: bool):
    antinodes = set()
    max_x, max_y = max_dim
    for antenna_type, positions in antennas.items():
        print(f"processing {antenna_type=}")
        for (x1, y1), (x2, y2) in permutations(positions, 2):
            # No need to find both antinodes created by ant1/ant2 in one go,
            # since we'll have to process the ant2/ant1 permutation too
            (anti_x, anti_y) = (x1 - (x2 - x1), y1 - (y2 - y1))
            while 0 <= anti_x < max_x and 0 <= anti_y < max_y:
                print(f"found ({anti_x}, {anti_y})")
                antinodes.add((anti_x, anti_y))
                if not p2:
                    break
                (anti_x, anti_y) = (anti_x - (x2 - x1), anti_y - (y2 - y1))

    return antinodes


def part1(antennas: dict[str, list[(int, int)]], max_dim: (int, int)):
    antinodes = _solve(antennas, max_dim, False)
    print(len(antinodes))


def part2(antennas: dict[str, list[(int, int)]], max_dim: (int, int)):
    antinodes = _solve(antennas, max_dim, True)
    antinodes |= {antenna for antenna_group in antennas.values() for antenna in antenna_group}
    print(len(antinodes))


def main(s: str):
    antennas, max_dim = parse(s)
    part1(antennas, max_dim)
    part2(antennas, max_dim)


if __name__ == "__main__":
    main(in_)
