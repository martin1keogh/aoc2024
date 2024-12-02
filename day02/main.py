from copy import copy


def is_safe(numbers: list[int]) -> bool:
    sorted_ = sorted(numbers)

    if not (sorted_ == numbers or sorted_ == list(reversed(numbers))):
        return False

    for i in range(len(numbers) - 1):
        if not 1 <= abs(sorted_[i] - sorted_[i + 1]) <= 3:
            return False

    return True


def part1():
    result = 0
    for line in in_.splitlines():
        numbers = list(map(int, line.split()))
        if is_safe(numbers):
            result += 1

    print(result)


def part2():
    result = 0
    for line in in_.splitlines():
        numbers = list(map(int, line.split()))
        if is_safe(numbers):
            result += 1
        else:
            for i in range(len(numbers)):
                # too lazy to be smart, plus this is still fast enough
                numbers_copy = copy(numbers)
                numbers_copy.pop(i)
                if is_safe(numbers_copy):
                    result += 1
                    break

    print(result)


def main():
    part1()
    part2()


if __name__ == '__main__':
    main()

