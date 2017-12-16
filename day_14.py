import day_10
import binascii

def create_hashes(hash='oundnydw'):
    results = list()
    for index in range(128):
        instructions = '{}-{}'.format(hash, index)
        instructions = [ord(x) for x in instructions]
        output = day_10.sparse_hash(instructions, 64, suffix=[17, 31, 73, 47, 23])
        dense_hash = day_10.dense_hash(output)
        results.append(''.join('{:02x}'.format(x) for x in dense_hash))

    return results


def part_one():
    results = create_hashes()
    count = 0
    for result in results:
        count += str(bin(int(result, 16))[2:]).count('1')
    return count


def write_out_input():
    global results, result
    results = create_hashes()
    with open(r'./input/day_14.txt', 'wt') as handle:
        for result in results:
            line = ''.join([bin(int(x, 16))[2:].zfill(4) for x in result])
            #print(len(line))
            handle.write(line + '\n')


def check_horizontal(regions):
    collect = list()
    for j in range(len(regions) - 1):
        z = regions[j-1] if j > 0 else None
        a = regions[j]
        b = regions[j + 1]

        if isinstance(a, int):
            item = min(t for t in (z,a,b) if isinstance(t, int))
            collect.append(item)
        else:
            collect.append(a)

    collect.append(regions[-1])

    return collect


def rotate_and_clean(results):
    final = []
    for index in range(128):
        vertical = [line[index] for line in results]
        for _ in range(10):
            vertical = check_horizontal(vertical)
        final.append(vertical)
    final2 = []
    for index in range(128):
        horizontal = [line[index] for line in final]
        for _ in range(10):
            horizontal = check_horizontal(horizontal)
        final2.append(horizontal)
    return final2


if __name__ == "__main__":
    # print("Part One: ", part_one())  # 8106
    # write_out_input()

    with open(r'./input/day_14.txt', 'rt') as handle:
        dense_results = handle.readlines()

    results = list()
    counter = 0
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

        for _ in range(20):
            new_line = check_horizontal(new_line)

        # print('{:02}'.format(index), end=': ')
        # [print(str(x).rjust(4, '-'), end='|') for x in new_line]
        # print()
        # [print(str(x).rjust(2, ' '), end='|') for x in result.strip()]

        results.append(new_line)


    final2 = rotate_and_clean(results)
    col_correction = list()
    for col in range(128):
        line = list()
        for row in range(128):
            line.append(final2[row][col])
        col_correction.append(line[:])
        line.clear()

    # c = ','.join(str(x) for x in col_correction)
    # final_split = c.split('-')
    #
    # rebuild = list()
    # for thing in final_split:
    #     # print(thing)
    #     if len(thing) == 0 or thing == ',':
    #         rebuild.append('-')
    #     else:
    #         m = min([int(x) for x in thing.split(',') if x != ''])
    #         for item in thing:
    #             if item == ',':
    #                 pass
    #             else:
    #                 rebuild.append(m)
    #
    # for _ in range(0, 128*128, 128):
    #     print('--> ', rebuild[_:_+128])

    print("\n")
    rebuild = []
    for item in col_correction:
        print(item)
        line = []

        collector = []
        temp = []
        last = None
        for component in item:
            if component != last:
                if len(temp) > 0:
                    if temp[0] != '-':
                        x = [min(temp) for i in temp]
                        if x != temp:
                            print("PROBLEM FOUND: ", temp)
                        temp = [min(temp) for i in temp]
                    collector.append(temp[:])
                temp.clear()
                temp.append(component)
                last = component
            else:
                temp.append(component)

        smaller = (collect for collect in collector if not None)
        for small in smaller:
            print(small)


    print("\n")
    for item in final2:
        [print(str(x).rjust(4, '-'), end='|') for x in item]
        print()
    print(counter)


# Not 2072






