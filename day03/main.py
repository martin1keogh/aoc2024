import re


def part1(s):
    regex = re.compile(r"mul\((\d{1,3}),(\d{1,3})\)")
    result = sum(int(a) * int(b) for a, b in regex.findall(s))
    print(result)


def part2(s):
    s = re.sub(r"(don't\(\).*?do\(\)|don't\(\).*$)", "", s, flags=re.DOTALL)
    part1(s)


if __name__ == "__main__":
    part1(in_)
    part2(in_)

