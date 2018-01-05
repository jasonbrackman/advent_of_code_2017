import os


def get_input():
    path = os.path.dirname(__file__)
    with open(os.path.join(path, 'input', 'day_24.txt'), 'rt') as handle:
        lines = handle.readlines()

    lines = [line.strip().split('/') for line in lines]

    return lines

tChain = list()

def generate_chains(links, input_='0'):
    temp = [x for x in links if x not in tChain]
    options = [item for item in temp if input_ in item]
    return options


def test(links, input='0', index=0):
    global tChain
    chains = generate_chains(links, input_=input)

    if not chains:
        # print(f"Start again - input ({input}), index ({index}):", tChain)
        yield tChain
        tChain = tChain[0:index-1]

    temp = links[:]
    index_more = index + 1

    for chain in chains:
        temp.remove(chain)
        temp_input = chain[1] if input != chain[1] else chain[0]

        tChain = tChain[0:index_more-1]
        tChain.insert(index, chain)

        yield from test(links, input=temp_input, index=index_more)


if __name__ == "__main__":
    links = get_input()
    nested = test(links, input='0')

    lengths = list()
    sums = list()
    for nest in nested:
        flattened = [int(i) for n in nest for i in n]
        lengths.append(flattened)
        r = sum(flattened)
        # if r > 1911:        # 1911 is too low
        #     print(r, nest)
        sums.append(r)

    print("Part One:", max(sums))  # 2006
    print("Part Two:", sum(sorted(lengths, key=len)[-1]))  # 1994

