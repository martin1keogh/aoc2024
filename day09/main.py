# Please don't 

def expand(s):
    expanded = []
    for i, block_size in enumerate(s):
        block_size = int(block_size)
        if i % 2 == 0:
            e = i // 2
        else:
            e = "."

        expanded.append([e] * block_size)

    return expanded


def part1(s):
    expanded = expand(s)

    current_empty_block_index = 0
    for (i, b) in reversed(list(enumerate(expanded))):
        while expanded[current_empty_block_index] != ".":
            current_empty_block_index += 1

        if current_empty_block_index > i:
            break

        expanded[current_empty_block_index] = b
        expanded[i] = "."

    result = 0
    for (i, b) in enumerate(expanded):
        if b == ".":
            break
        result += i * int(b)

    print(result)


def part2(s):
    expanded = expand(s)

    blocks_to_move = []
    current_block_value = None
    current_size = 0
    for i, b in reversed(list(enumerate(expanded))):
        if current_block_value and current_block_value != b:
            blocks_to_move.append((current_block_value, current_size, i + 1))
            current_block_value = None

        if not current_block_value and b != ".":
            current_block_value = b
            current_size = 1
            continue

        if current_block_value == b:
            current_size += 1
            continue

    current_empty_block_start_index = 0
    for (value, size, start_index) in blocks_to_move:
        while True:
            try:
                while expanded[current_empty_block_start_index] != ".":
                    current_empty_block_start_index += 1
                current_empty_block_end_index = current_empty_block_start_index
                while expanded[current_empty_block_end_index] == ".":
                    current_empty_block_end_index += 1
            except IndexError:
                current_empty_block_start_index = 0
                break

            empty_block_size = current_empty_block_end_index - current_empty_block_start_index

            if empty_block_size >= size and current_empty_block_start_index < start_index:
                expanded[current_empty_block_start_index:(current_empty_block_start_index + size)] = [value] * size
                expanded[start_index:(start_index + size)] = ["."] * size
                current_empty_block_start_index = 0
                break
            else:
                current_empty_block_start_index = current_empty_block_end_index

    result = 0
    for (i, b) in enumerate(expanded):
        if b == ".":
            continue
        result += i * int(b)

    print(result)



def main(s):
    part1(s)
    part2(s)


if __name__ == "__main__":
    main(in_)

