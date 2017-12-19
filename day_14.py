import itertools

import day_10


def create_hashes(hash_):
    results = list()
    for index in range(128):
        instructions = [ord(x) for x in '{}-{}'.format(hash_, index)]
        output = day_10.sparse_hash(instructions, 64, suffix=[17, 31, 73, 47, 23])
        dense_hash = day_10.dense_hash(output, block_size=16)
        results.append(''.join('{:02x}'.format(x) for x in dense_hash))
    return results


def part_one(hash_):
    results = create_hashes(hash_)
    count = sum(bin(int(result, 16))[2:].count('1') for result in results)
    return count


def write_out_input(hash_):
    results = create_hashes(hash_)
    with open(r'./input/day_14.txt', 'wt') as handle:
        for result in results:
            line = ''.join([bin(int(x, 16))[2:].zfill(4) for x in result])
            handle.write(line + '\n')


def check_horizontal(regions):
    collect = list()
    text = ','.join(str(x) for x in regions)
    items = text.split("-")
    for item in items:
        if len(item) == 0 or item == ',':
            collect.append('-')
        else:
            nums = [int(x) for x in item.split(',') if len(x) > 0]
            # if min(nums) != max(nums):
            #     print("problem ... ")
            for _ in nums:
                collect.append(min(nums))
            collect.append('-')
    return collect


def rotate_and_reduce(lines):
    new_lines = list()
    for col in range(128):
        line = list()
        for row in range(128):
            line.append(lines[row][col])
        new_lines.append(check_horizontal(line))
        line.clear()
    return new_lines


if __name__ == "__main__":
    key1 = 'flqrgnkx'
    key2 = 'oundnydw'
    key = key2
    print("Part One: ", part_one(key))  # 8106
    write_out_input(key)

    with open(r'./input/day_14.txt', 'rt') as handle:
        dense_results = handle.readlines()

    results = list()
    counter = 1
    go = True

    # from line 1 to 128
    for index, result in enumerate(dense_results):
        new_line = []

        for i, character in enumerate(result.strip()):

            if go is False:
                if character != '0':
                    if index > 0 and results[index-1][i] != '-':
                        new_line.append(results[index-1][i])

                    elif i > 0 and new_line[i-1] != '-':
                        new_line.append(new_line[i-1])

                    else:
                        counter += 1
                        new_line.append(counter)

                    go = True
                else:
                    new_line.append('-')
                    go = False

            else:
                if character != '0':
                    if index > 0 and results[index-1][i] != '-':
                        new_line.append(results[index-1][i])
                    elif i > 0 and new_line[i-1] != '-':
                        new_line.append(new_line[i-1])
                    else:
                        new_line.append(counter)
                    go = True
                else:
                    new_line.append('-')
                    go = False

        results.append(new_line)


    test = sum(len(set(x)) for x in results)
    for _ in itertools.count():
        # print(_)
        results = rotate_and_reduce(results)
        # results = rotate_and_reduce(results)
        new_test = sum(len(set(x)) for x in results)
        if new_test == test:
            print("likely the same? ", new_test, a)
            break


    print("\n")
    for item, item2 in zip(results, dense_results):
        [print(str(x).rjust(4, '-'), end='|') for x in item]
        print()
        # [print(str(x).replace('0', '-').rjust(4, '-'), end='|') for x in item2]
        # print()
    final = list()
    for item in results:
        final += list(set(item))
    print(len(set(final)) - 1)  # account for the '-'




# Not 2072
# Not 1271
# 1247?
# 1241?
# 1232?
# not 1159
# not 1167







