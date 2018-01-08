import os

import math


def get_rules(filename='day_21.txt'):
    root = os.path.dirname(__file__)
    with open(os.path.join(root, 'input', filename), 'rt') as handle:
        lines = handle.readlines()
    lines = [line.replace(" => ", "\n") for line in lines]
    lines = {line.split()[0]: line.split()[1] for line in lines}
    return lines


RULES = get_rules()


def _get_size(pattern):
    pattern = pattern.replace('/', '')
    return 2 if len(pattern) % 2 == 0 else 3


def is_matched_against_rule_permutation(key: str, pattern: str):

    # might be able to exit early
    # key_mirror = '/'.join([k[::-1] for k in key.split('/')])
    key_flip = '/'.join([k for k in reversed(key.split('/'))])
    if pattern in (key, key_flip):
        return True

    for _ in range(4):  # (4) four rotations

        key = rotate_grid(key)
        key_mirror = '/'.join([k[::-1] for k in key.split('/')])
        key_flip = '/'.join([k for k in reversed(key.split('/'))])
        if pattern in (key, key_mirror, key_flip):
            return True
    return False


def rotate_grid(key):
    # print('Enter Rotate:')
    key_rotate = []
    key_split = key.split("/")
    for row in range(len(key_split)):
        l = []
        for col in range(len(key_split)):
            l.append(key_split[col][row])
        key_rotate.append(''.join(reversed(l)))
    key_rotate = '/'.join(k for k in key_rotate)
    # [print(k) for k in key_rotate.split('/')]
    # [print(k) for k in key.split('/')]
    # print("Leave Rotate.")
    return key_rotate


def get_new_pattern(pattern):
    new_pattern = None
    for k, v in RULES.items():
        if k.count('/') == pattern.count('/'):
            result = is_matched_against_rule_permutation(k, pattern)
            if result is True:
                new_pattern = v
                break
    # print(f"From {pattern} ==> {new_pattern}")
    return new_pattern


if __name__ == "__main__":
    pattern = ".#./..#/###"

    for _ in range(3):
        pattern = pattern.replace("/", '')
        size = _get_size(pattern)

        divisor = 4 if size == 2 else 3
        parts = int(len(pattern) / size)

        # split_by = int(parts * size / divisor)
        split_by = int(math.sqrt(len(pattern)))
        # print(split_by, len(pattern))
        print(f'Parts: {parts}, Size: {size}, Divisor: {divisor}, Split_by: {split_by}, Pattern: {pattern}')

        # understand the rows in the grid to be able to break them down

        grid = [pattern[i:i + split_by] for i in range(0, len(pattern), split_by)]
        print("  Grid:", grid, len(grid[0]), 'by', len(grid))
        # for g in grid:
        #     print(g)

        # breaks down the grid into smaller portions
        grid_length = len(grid)
        grid_width = len(grid[0])
        # grid = ''.join(grid)
        groups = list()
        for row in range(0, grid_length, size):
            for col in range(0, grid_width, size):
                group = [g[col:col + size] for g in grid[row:row+size]]
                # print(f'Col: {col} to {col+size}, Row: {row} to {row+size}, Group: {group}, Grid: {grid}')
                groups.append(group)
        print("Groups:", groups)

        # get new patterns
        patterns = list()
        for group in groups:
            new = get_new_pattern('/'.join(group))
            assert new is not None, ("Expected a pattern, but instead got None when passing in: ", group)

            new = new.split('/')
            patterns.append(new)

        # print('p', patterns, len(patterns))
        # print("patter:", patterns)

        # This is where it falls apart for odd numbers!!
        if (len(patterns[0]) * len(patterns)) % 2 == 0:
            # recombine grid from smaller portions
            new_grid = [[], [], [], []]
            print(f'Divisor: {divisor}, Patterns: {patterns}')
            for index in range(0, len(patterns[0])):

                for c, pattern in enumerate(patterns):
                    print("pattern:", pattern)
                    print(f'[{_}] [Row: {index} - Corner:{c}] {pattern[index]}')
                    new_grid[c].append(pattern[index])

            if len(new_grid[0]) == len(new_grid[-1]):
                temp = list()
                for x in zip(new_grid[0], new_grid[1]):
                    temp.append('/'.join(x))
                for y in zip(new_grid[2], new_grid[3]):
                    temp.append('/'.join(y))
                pattern = '/'.join(temp)
            else:
                pattern = '/'.join(new_grid[0])
        else:
            new_grid = [[], [], []]
            print(f'Patterns: {patterns}')
            for index in range(0, len(patterns[0])):
                for c, pattern in enumerate(patterns):
                    print(pattern[index])
                    # print("pattern:", pattern)
                    # print(f'[{_}] [Row: {index} - Section:{c}] {pattern[index]}')
                    # new_grid[index].append(pattern[index])

            pattern = []
        # pattern = '/'.join('/'.join(pattern) for pattern in patterns)
        print('F', pattern, pattern.count('#'))

        print("----------")


    """
    Collect & Redistribute:
    ##.#/#.##/##../#.##
    
    ##.#
    #.##
    ##..
    #.##
    
    ###./.###/###./..##
    """

    """
    Rotation Output Example:
    .#.   .#.   #..   ###
    ..#   #..   #.#   ..#
    ###   ###   ##.   .#."""