from functools import cache


def parse(s):
    return list(map(int, s.split(" ")))


@cache
def steps(stone: int, count: int) -> int:
    if count == 0:
        return 1

    if stone == 0:
        return steps(1, count - 1)
    elif (as_str := str(stone)) and (l := len(as_str)) % 2 == 0:
        return steps(int(as_str[:l // 2]), count - 1) + steps(int(as_str[l // 2:]), count - 1)
    else:
        return steps(stone * 2024, count - 1)


def solve(stones: list[int], count: int) -> int:
    result = 0
    for stone in stones:
        result += steps(stone, count)
    return result


def part1(stones: list[int]):
    print(solve(stones, 25))


def part2(stones: list[int]):
    print(solve(stones, 75))


def main(s):
    stones = parse(s)
    part1(stones)
    (part2(stones))


if __name__ == "__main__":
    main(in_)

