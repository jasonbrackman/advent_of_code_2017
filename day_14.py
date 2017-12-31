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


if __name__ == "__main__":
    key1 = 'flqrgnkx'
    key2 = 'oundnydw'
    key = key2
    print("Part One: ", part_one(key))  # 8106

    # uncomment to spend time writing out the above work to a file.
    # write_out_input(key)







