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

def convert_hex_to_bin(hash):
    return binascii.unhexlify(hash)


def part_one():
    results = create_hashes()
    count = 0
    for result in results:
        count += str(bin(int(result, 16))[2:]).count('1')
    print(count)


def write_out_input():
    global results, result
    results = create_hashes()
    with open(r'./input/day_14.txt', 'wt') as handle:
        for result in results:
            line = ''.join([bin(int(x, 16))[2:].zfill(4) for x in result])
            #print(len(line))
            handle.write(line + '\n')


if __name__ == "__main__":
    # part_one()
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

        print('{:02}'.format(index), end=': ')
        [print(str(x).rjust(4, '-'), end='|') for x in new_line]
        print()
        # [print(str(x).rjust(2, ' '), end='|') for x in result.strip()]
        results.append(new_line)

    for line in results:
        print(line)
    print(counter)

# Not 2072






