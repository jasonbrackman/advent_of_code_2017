# coding=utf-8
#
# 1122 produces a sum of 3 (1 + 2) because the first digit (1) matches the second digit and the third digit (2) matches the fourth digit.
# 1111 produces 4 because each digit (all 1) matches the next.
# 1234 produces 0 because no digit matches the next.
# 91212129 produces 9 because the only digit that matches the next one is the last digit, 9.
#
# Puzzle input:
# ??
# Creation Date: 12/1/2017
#
# --------------------------------------------------------------------------------------

from itertools import cycle


def captcha(number):
    characters = [character for character in str(number)]
    if len(characters) == 1 or len(characters) == len(set(characters)):
        return 0
    else:
        offset = characters[1:] + [characters[0]]
        keepers = list()

        for a, b in zip(characters, offset):
            if a == b:
                keepers.append(int(a))

        return sum(keepers)


def captcha_halfway_round(number):

    characters = [character for character in str(number)]
    sentinal = int(len(characters) / 2)

    offsets = [get_nth_cycled_item(characters, index+sentinal) for index, _ in enumerate(characters)]
    # print(characters)
    # print(offsets)
    keepers = list()
    for a, b in zip(characters, offsets):
        if a == b:
            keepers.append(int(a))

    return sum(keepers)


def get_nth_cycled_item(characters, sentinal):
    library = cycle(characters)
    for _ in range(sentinal):
        next(library)
    return next(library)


if __name__ == "__main__":
    with open(r'./input/day_01.txt', 'rt') as handle:
        adventofcode = int(handle.readline())
        print("Part One: {}".format(captcha(adventofcode)))
        print("Part Two: {}".format(captcha_halfway_round(adventofcode)))
