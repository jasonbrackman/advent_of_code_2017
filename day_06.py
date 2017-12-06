
import itertools


def redistribute(block):
    to_move = max(block)
    index = block.index(to_move)
    block[index] = 0
    for _ in range(to_move):
        if index + 1 == len(block):
            index = 0
        else:
            index += 1
        block[index] += 1
    return block[:]


def find_loop(block):

    collection = [block[:]]

    for _ in itertools.count():
        result = redistribute(block)
        if result in collection:
            print("Part 2: ", len(collection) - collection.index(result))
            return len(collection)
        collection.append(result)


if __name__ == "__main__":
    input = [int(x.strip()) for x in "2	8 8	5 4 2 3 1 5 5 1 2 15 13 5 14".split()]
    # input = [0, 2, 7, 0]
    print("Part 1: ", find_loop(input))
