from collections import defaultdict
import random


def parse(s: str):
    rules, recipes = s.split("\n\n")

    requirements = defaultdict(list)
    for rule in rules.splitlines():
        from_, to_ = rule.split("|")
        requirements[int(to_)].append(int(from_))

    updates = []
    for recipe in recipes.splitlines():
        updates.append([int(page) for page in recipe.split(",")])

    return requirements, updates


def error_index(update: list[int], requirements: dict[int, list[int]]) -> int | None:
    for i in range(len(update)):
        for page in update[(i + 1):]:
            if update[i] not in requirements[page]:
                return i

    return None


def is_valid(update, requirements):
    return error_index(update, requirements) is None


def part1(requirements: dict[int, list[int]], updates: list[list[int]]):
    result = 0
    for update in updates:
        if is_valid(update, requirements):
            result += update[len(update) // 2]

    print(result)


def part2(requirements: dict[int, list[int]], updates: list[list[int]]):
    result = 0
    for update in updates:
        if is_valid(update, requirements):
            continue

        invalid_fixes = {"".join(str(i) for i in update)}
        while (i := error_index(update, requirements)) is not None:
            update[i], update[i + 1] = update[i + 1], update[i]
            # Too lazy to think of what to do when there's a cycle, so let's leave of all this to chance
            if (as_str := "".join(str(i) for i in update)) in invalid_fixes:
                rand = random.randint(i, len(update) - 1)
                update[i], update[rand] = update[rand], update[i]
            invalid_fixes.add(as_str)

        result += update[len(update) // 2]

    print(result)


def main():
    requirements, updates = parse(in_)
    part1(requirements, updates)
    part2(requirements, updates)


if __name__ == "__main__":
    main()
