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

from collections import deque


def captcha(number, rotate=-1):
    characters = deque([character for character in str(number)])
    if len(characters) == 1:
        return 0

    offset = characters.copy()
    offset.rotate(rotate)
    keepers = [int(a) for a, b in zip(characters, offset) if a == b]

    return sum(keepers)


if __name__ == "__main__":
    with open(r'./input/day_01.txt', 'rt') as handle:
        text_ = handle.readline()
        int_ = int(text_)
        halfway = len(text_) // 2
        print("Part One: {}".format(captcha(int_)))  # 1182
        print("Part Two: {}".format(captcha(int_, rotate=halfway)))  # 1152
