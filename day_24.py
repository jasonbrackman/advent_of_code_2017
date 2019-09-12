import os


def get_input():
    path = os.path.dirname(__file__)
    with open(os.path.join(path, 'input', 'day_24.txt'), 'rt') as handle:
        lines = handle.readlines()

    lines = [line.strip().split('/') for line in lines]

    return lines


tChain = list()


def generate_chains(links, input_='0'):
    return [x for x in links if input_ in x and x not in tChain]


def test(links, input='0', index=0):
    global tChain
    chains = generate_chains(links, input_=input)

    if not chains:
        # print(f"Start again - input ({input}), index ({index}):", tChain)
        yield tChain
        tChain = tChain[0:index-1]

    index_more = index + 1

    for chain in chains:
        temp_input = chain[1] if input != chain[1] else chain[0]

        tChain = tChain[0:index_more-1]
        tChain.insert(index, chain)

        yield from test(links, input=temp_input, index=index_more)


def main():
    links = get_input()
    nested = test(links, input='0')
    lengths = list()
    sums = list()
    for nest in nested:
        flattened = [int(i) for n in nest for i in n]
        lengths.append(flattened)
        r = sum(flattened)
        sums.append(r)
    print("Part One:", max(sums))  # 2006
    print("Part Two:", sum(sorted(lengths, key=len)[-1]))  # 1994


if __name__ == "__main__":
    # import cProfile
    # cProfile.run("main()")

    main()

    # import timeit
    # print(timeit.timeit(lambda: main(), number=2))