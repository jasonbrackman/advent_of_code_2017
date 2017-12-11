input = """pbga (66)
xhth (57)
ebii (61)
havc (66)
ktlj (57)
fwft (72) -> ktlj, cntj, xhth
qoyq (66)
padx (45) -> pbga, havc, qoyq
tknk (41) -> ugml, padx, fwft
jptl (61)
ugml (68) -> gyxo, ebii, jptl
gyxo (61)
cntj (57)"""


def parse(line):
    args = line.split('->')
    return args


def get_organized_data(content):
    kv = dict()
    for line in content:
        result = parse(line)
        if len(result) == 1:
            code, value = result[0].split()
            children = []
        else:
            code, value = result[0].split()

            children = result[1].split()

        value = int(value.strip("()"))

        children = [child.strip(',') for child in children]
        kv[code] = {value: children}

    return kv


def print_tree_from_root(root, kvalues, level=0):
    results = list()
    for num, children in kvalues[root].items():
        print("{} Node value for {} -> {}".format(level, root, num))
        for child in children:
            collected = get_cost_of_child(child, kvalues)
            results.append((collected, child))
            # print("{} Child [{}] ({}) costs {}".format(root, child, kvalues[child].items(), collected))
    results = sorted(results)
    if len(results) > 1 and results[0][0] != results[-1][0]:
        print("Unbalanced: If highest problem in the chain reduce the next node by: {}".format(results[-1][0]-results[0][0]))
    if len(results) > 0:
        print_tree_from_root(max(results)[1], kvalues, level=level+1)


def get_cost_of_child(child, kvalues, level=0):
    cost = 0

    for name, values in kvalues.items():
        if name == child:
            for k, v in values.items():
                cost += k
                for kid in v:
                    cost += get_cost_of_child(kid, kvalues, level=level+1)

    return cost


if __name__ == "__main__":
    with open(r'./input/day_07.txt', 'rt') as handle:
        puzzle = handle.readlines()
        tree = []
        values = get_organized_data(puzzle)

        crumb = None
        for name in values.keys():
            found = False
            crumb = name
            for k, v in values.items():
                if k != name:
                    for _, children in v.items():
                        if name in children:
                            found = True
                            crumb = name
            if not found:
                print("Part One: ", crumb)  # expecting eugwuhl
                break

        print_tree_from_root(crumb, values)
