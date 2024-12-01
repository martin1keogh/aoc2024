def read_input():
    left, right = [], []
    for row in in_.splitlines():
        [l, r] = row.split()
        left.append(int(l))
        right.append(int(r))

    return left, right


def part1(left, right):
    zipped = zip(left, right)
    diff = 0
    for l, r in zipped:
        diff += abs(l - r)

    print(diff)


def part2(left, right):
    result = 0
    current_r_index = 0
    for l in left:
        occurrences = 0
        for r in right[current_r_index:]:
            if r > l:
                result += l * occurrences
                break
            if r < l:
                current_r_index += 1
                continue
            occurrences += 1

    print(result)


def main():
    left, right = read_input()
    left, right = sorted(left), sorted(right)
    part1(left, right)
    part2(left, right)


if __name__ == '__main__':
    main()
