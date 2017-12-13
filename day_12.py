# Not mine but so .... much ... cleaner:
#
# def create_connections_(lines, looking_for):
#     connections = get_connections(lines)
#
#     queue = [looking_for]
#     pipes = set()
#     while queue:
#         a = queue.pop()
#         for b in connections[a]:
#             if b not in pipes:
#                 pipes.add(b)
#                 queue.append(b)
#
#     return pipes


def get_connections(lines):
    graphs = dict()
    for line in lines:
        pipe, _, *array = line.split(' ')
        array = [int(item.strip(', ')) for item in array]
        graphs[int(pipe)] = array
    return graphs


def create_connections(lines, looking_for):
    connections = get_connections(lines)

    pipes = {looking_for: []}
    results = set()
    # ugly hack ...
    for repeat in range(100):
        # Shortcut the repeat if possible
        if len(results) != repeat:
            break

        for k, v in connections.items():

            if k in pipes[looking_for]:
                pipes[looking_for] += v
                continue

            if looking_for == k:
                pipes[looking_for].append(k)

            if looking_for in v:
                pipes[looking_for].append(k)
                pipes[looking_for] += v
                for index in v:
                    pipes[looking_for] += connections[index]
                continue

            in_database = [item for item in pipes[looking_for] if item in v]
            if in_database:
                pipes[looking_for] += v

        results.add(len(set(pipes[looking_for])))

    return set(pipes[looking_for])


if __name__ == "__main__":

    with open(r'./input/day_12.txt', 'rt') as handle:
        lines = handle.readlines()
        x = create_connections(lines, 0)
        print("Part One: ", len(x))  # 239

        groups = 0
        for index in range(len(lines)):
            if index not in x:
                groups += 1
                new = create_connections(lines, index)
                for item in new:
                    x.add(item)

        print("Part Two: ", groups)  # 215
