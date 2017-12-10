"""
Implement The Knot Hash:

  4--5   pinch   4  5           4   1
 /    \  5,0,1  / \/ \  twist  / \ / \
3      0  -->  3      0  -->  3   X   0
 \    /         \ /\ /         \ / \ /
  2--1           2  1           2   5

"""


def sparse_hash(data, rounds=1, suffix=None):
    """
    Using a combination of data [and suffix] pinch and twist an array of numbers.
    :param data: any text, but if intended to go through the dense_hash all characters
                 must be represented as a byte number (0-255)
    :param rounds: int() number of pinch/twist rounds
    :param suffix: An array of numbers -- I *think* this is a salt?
    :return: 256 numbers (0, 255) mixed based off of the pinch and twist.
    """
    data = data if suffix is None else data + suffix
    hash = [x for x in range(256)]
    hash_length = len(hash)
    pos = 0
    skip = 0

    for round in range(rounds):
        for instruction in data:

            # reverse the number of hash digits from the pos
            collector = []

            new_pos = 0
            for index in range(pos, pos+instruction):
                if index < hash_length:
                    collector.append(hash[index])
                else:
                    if new_pos >= hash_length:
                        new_pos = 0
                    collector.append(hash[new_pos])
                    new_pos += 1

            to_reverse = list(reversed(collector))

            # put the numbers back
            new_pos = 0
            for index, item in enumerate(to_reverse, pos):
                new_pos = index if index is pos else (new_pos + 1)
                if new_pos >= hash_length:
                    new_pos = 0
                hash[new_pos] = item

            # step to next hash index
            pos += instruction + skip
            if pos >= hash_length:
                special = pos - hash_length
                pos = 0
                special = special % hash_length
                for item in range(special):
                    pos += 1

            skip += 1
    return hash


def dense_hash(hash):
    """
    Takes in a sparse hash and xors all numbers in groups of 16
    - a 256 length sparse hash will generate a 16 numbered array.
    :param hash:
    :return:
    """
    results = list()
    for index in range(0, len(hash), 16):
        total = 0
        list_01 = hash[index:index+16]
        for i in list_01:
            total ^= i
        results.append(total)

    return results

# will break if the hash is incorrectly calculating
assert dense_hash([65, 27, 9, 1, 4, 3, 40, 50, 91, 7, 6, 0, 2, 5, 68, 22]) == [64]
# print("hex Vaues: ", [hex(x).replace('0x', '') for x in [64, 7, 255]])


def part_one():
    instructions = [199, 0, 255, 136, 174, 254, 227, 16, 51, 85, 1, 2, 22, 17, 7, 192]
    output = sparse_hash(instructions, rounds=1)
    answer = output[0] * output[1]
    print("Part One: ", answer)
    assert answer == 3770

def tests():
    for item, expect in zip(('', 'AoC 2017', '1,2,3', '1,2,4'), ('a2582a3a0e66e6e86e3812dcb672a272',
                                                                 '33efeb34ea91902bb2f59c9920caa6cd',
                                                                 '3efbe78a8d82f29979031a4aa0b16a9d',
                                                                 '63960835bcdc130f0b66d7ff4f6a5a8e')):
        instructions = [ord(x) for x in item]
        output = sparse_hash(instructions, rounds=64, suffix=[17, 31, 73, 47, 23])
        final = ''.join('{:02x}'.format(x) for x in dense_hash(output)).strip()
        assert final == expect


if __name__ == "__main__":
    tests()

    # Part 1
    part_one()

    # Part 2
    instructions = '199,0,255,136,174,254,227,16,51,85,1,2,22,17,7,192'
    instructions = [ord(x) for x in instructions]
    output = sparse_hash(instructions, rounds=64, suffix=[17, 31, 73, 47, 23])

    # get dense hash and convert it to hex in a length of 32characters
    final_hash = ''.join('{:x}'.format(x) for x in dense_hash(output))
    print("Part Two - dense hash: ", final_hash)
