from collections import OrderedDict
from itertools import cycle, repeat, count
import copy

SCAN = ['s']


def picosecond(stuff, preroll=0):
    for k, v in stuff.items():
        result = preroll + k % (2 * (len(v) - 1)) == 0

        if result:
            v[0] = SCAN
        else:
            v[0].clear()

        # x = v.index(SCAN)
        # v[x] = []
        # dir = direction.get(k, 1)
        #
        # if dir == 1:  # forward
        #     v[x+1] = SCAN
        #     if v[-1] == SCAN:
        #         direction[k] = 0
        # else:
        #     v[x-1] = SCAN
        #     if v[0] == SCAN:
        #         direction[k] = 1

    return stuff


def get_caught_number(stuff, preroll=0):
    if preroll > 0:
        stuff = picosecond(stuff, preroll=preroll)

    caught = 0
    for key in range(max(stuff.keys()) + 1):
        if key in stuff.keys():
            if stuff[key][0] == SCAN:
                print(stuff[key])
                caught += key * len(stuff[key])
                if preroll > 0:
                    return 100
        # print(stuff)
        stuff = picosecond(stuff, preroll=0)

    return caught


def setup_buckets(test):
    buckets = dict()
    for item in test.split("\n"):
        vars = item.split(':')
        key = int(vars[0].strip())
        values = [[] for _ in range(int(vars[1].strip('\n ')))]
        buckets[key] = values
    for k, v in buckets.items():
        v[0] = SCAN
    return buckets


def revamp_counter(d):
    delay = 0
    keep_going = 999
    while keep_going > 1:
        keep_going = 1
        for tick in range(max(d.keys()) + 1):
            if tick in d.keys():
                offset = (tick + delay) % (2 * (len(d[tick]) - 1))
                if offset == 0:  # top of stack
                    if offset % 5000 == 0:
                        print("STILL WORKING: ", delay)
                    # print('Key [{}] in step [{}] got hit'.format(tick, delay))
                    keep_going += 1
        if keep_going == 1:
            break
        delay += 1

    return delay


if __name__ == "__main__":

    test = """0: 3
    1: 2
    4: 4
    6: 4"""
    with open(r'./input/day_13.txt', 'rt') as handle:
        test = handle.read()
    buckets = setup_buckets(test)

    print("Part One: ", get_caught_number(copy.deepcopy(buckets)))
    print("Part Two: ", revamp_counter(copy.deepcopy(buckets)))
    # increase = 1  # 6000
    # while True:
    #     result = get_caught_number(copy.deepcopy(buckets), preroll=increase)
    #     if result == 0:
    #         print("Part Two: ", increase)
    #         break
    #     else:
    #         if increase % 500 == 0:
    #             pass
    #             # print(increase)
    #         increase += 1
    #         break
    #
    #
    #
    #
