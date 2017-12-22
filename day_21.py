import os

def get_rules(filename='day_21.txt'):
    root = os.path.dirname(__file__)
    with open(os.path.join(root, 'input', filename), 'rt') as handle:
        lines = handle.readlines()
    lines = [line.replace(" => ", "\n") for line in lines]
    lines = {line.split()[0]: line.split()[1] for line in lines}
    return lines


def is_matched_against_rule_permutation(key: str, pattern: str):
    if key == pattern:
        return True

    for _ in range(5):
        key_mirror = '/'.join([k[::-1] for k in key.split('/')])
        key_flip = '/'.join([k for k in reversed(key.split('/'))])
        key = rotate_grid(key)

        if key_mirror == pattern:
            return True
        if key_flip == pattern:
            return True
        if key == pattern:
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


def apply_enhancement_rules(pattern, rules):
    parsed = parse_pattern(pattern)
    result = list()
    for pattern in yield_swizzle_pattern(parsed):
        result.append(get_new_pattern(pattern, rules))
    return '/'.join(result)


def get_new_pattern(pattern, rules):
    new_pattern = None
    for k, v in rules.items():
        if k.count('/') == pattern.count('/'):
            result = is_matched_against_rule_permutation(k, pattern)
            if result is True:
                new_pattern = v
                break
    return new_pattern


def parse_pattern(key):
    collect = list()
    # grid_type = 2 if (len(key)-key.count('/')) % 2 == 0 else 3

    items = key.split('/')

    for item in items:
        # get length of the row
        item_length = len(item)
        grid_type = 2 if len(item) % 2 == 0 else 3
        if item_length == grid_type:  # already setup for rules
            collect.append(item)

        elif item_length > grid_type:   # not well formed
            for index in range(0, item_length, grid_type):
                collect.append(item[index: index+grid_type])
        else:
            print(f'Something has gone wrong: {item}')

    key = '/'.join(collect)
    return key


def yield_swizzle_pattern(parsed):
    sections = parsed.split('/')
    grid = 2 if len(sections[0]) % 2 == 0 else 3
    # print("GRID: ", grid)
    hold = list()
    collection = list()
    for i in range(len(sections)):
        if i % grid == 0:
            collection.append(sections[i])
            while len(hold) > 0:
                collection.append(hold.pop())
        else:
            hold.append(sections[i])
    collection += hold
    for index in range(0, len(collection), grid):
        yield '/'.join(collection[index:index+grid])


if __name__ == "__main__":
    pattern = ".#./..#/###"
    rules = get_rules(filename='day_21.txt')
    print(f'[0] {pattern} Count: {pattern.count("#")}')
    for _ in range(6):

        pattern = apply_enhancement_rules(pattern, rules)
        print(f'[{_+1}] Count: {pattern.count("#")}:  {pattern}')

# 176 is too low
# not 306

