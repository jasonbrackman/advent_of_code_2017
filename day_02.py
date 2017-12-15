def min_max_dif(row):
    items = [int(n) for n in row.split()]
    return max(items) - min(items)


def get_divisible_result(row):
    items = [int(x) for x in row.split()]
    for item in items:
        for number in items:
            if item != number and item % number == 0:
                return item / number


if __name__ == "__main__":
    with open(r'./input/day_02.txt', 'rt') as handle:
        input = handle.readlines()
        print("Solution One: {}".format(sum([min_max_dif(item) for item in input if len(item.strip()) > 0])))
        print("Solution Two: {}".format(sum([get_divisible_result(item) for item in input if len(item.strip()) > 0])))
