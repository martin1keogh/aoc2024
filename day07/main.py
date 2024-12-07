import re
from itertools import product
from typing import Callable


def parse(s: str):
    result = {}
    for row in s.splitlines():
        target, *values = re.split(r"[: ]+", row)
        result[int(target)] = [int(v) for v in values]

    return result


def _solve(equations: dict[int, list[int]], ops: list[Callable[[int, int], int]]) -> int:
    result = 0
    for target, values in equations.items():
        for op_choices in product(ops, repeat=len(values) - 1):
            # 50% slower than using the for-loop below
            # score = reduce(lambda x, y: next(op_choices)(x, y), values)
            score = values[0]
            for op, value in zip(op_choices, values[1:]):
                score = op(score, value)
            if score == target:
                result += target
                break

    return result


def part1(equations: dict[int, list[int]]) -> int:
    ops = [int.__add__, int.__mul__]
    result = _solve(equations, ops)
    print(result)
    return result


def part2(equations: dict[int, list[int]]) -> int:
    ops = [int.__add__, int.__mul__, lambda x, y: int(str(x) + str(y))]
    result = _solve(equations, ops)
    print(result)
    return result


def main(s: str):
    parsed = parse(s)
    part1(parsed)
    part2(parsed)


if __name__ == "__main__":
    main(in_)
