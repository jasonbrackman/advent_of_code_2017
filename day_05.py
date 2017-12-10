
import itertools


def increment(args, special=False):

    current_index = 0

    for counter in itertools.count():
        try:
            offset = args[current_index]
            args[current_index] += -1 if special and offset >= 3 else 1
            current_index += offset
        except IndexError:
            # escaped the maze
            return counter


if __name__ == "__main__":
    with open(r'./input/day_05.txt', 'rt') as handle:
        aoc_input = handle.read()
        orig = [int(x) for x in aoc_input.split('\n')]
        print("Part 01: ", increment(orig[:]))
        print("Part 02: ", increment(orig[:], special=True))
