import re
from typing import Optional


Group = tuple[tuple[int, int], tuple[int, int], tuple[int, int]]


def parse(s: str) -> list[Group]:
    result = []
    regexp = re.compile(r"X[+=](\d+), Y[+=](\d+)")
    for group in s.split("\n\n"):
        [a, b, p] = group.splitlines()
        [(a_x, a_y)] = re.findall(regexp, a)
        [(b_x, b_y)] = re.findall(regexp, b)
        [(p_x, p_y)] = re.findall(regexp, p)
        result.append(((int(a_x), int(a_y)), (int(b_x), int(b_y)), (int(p_x), int(p_y))))

    return result


def solve(group: Group) -> Optional[int]:
    ((a_x, a_y), (b_x, b_y), (p_x, p_y)) = group
    max_iter = 2 ** 63
    max_b = min(p_x // b_x, p_y // b_y, max_iter)
    current_a, current_b = 0, max_b
    while (current_a * a_x + current_b * b_x) != p_x or (current_a * a_y + current_b * b_y) != p_y:
        # Can't use the walrus operator (for current_y) since the `or` would shortcut the check
        current_x = current_a * a_x + current_b * b_x
        current_y = current_a * a_y + current_b * b_y

        if current_x >= p_x or current_y >= p_y:
            dec = min(abs((current_x - p_x) // b_x), abs((current_y - p_y) // b_y))
            current_b -= dec or 1
        else:
            inc = max((p_x - current_x) // a_x, (p_y - current_y) // a_y, 1)
            current_a += inc or 1

        if current_a * a_x >= p_x or current_a * a_y >= p_y:
            return None

    return current_a * 3 + current_b


def part1(groups: list[Group]):
    print(sum(filter(None, map(solve, groups))))


def part2(groups: list[Group]):
    shifted = []
    shift = 10_000_000_000_000
    for a, b, (p_x, p_y) in groups:
        shifted.append((a, b, (p_x + shift, p_y + shift)))

    print(sum(filter(None, map(solve, shifted))))


def main(s: str):
    groups = parse(s)
    part1(groups)
    part2(groups)


if __name__ == "__main__":
    main(in_)

