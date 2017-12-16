import string
import itertools


def spin(text, index):
    start = text[0:-(index)]
    end = text[-(index):]

    return end + start


def exchange(text, a, b):
    letters = [c for c in text]
    letters[a], letters[b] = letters[b], letters[a]
    return ''.join(letters)


def partner(text, char_a, char_b):
    collect = list()
    for c in text:
        if c == char_a:
            collect.append(char_b)
        elif c == char_b:
            collect.append(char_a)
        else:
            collect.append(c)
    return ''.join(collect)


def find_wrap_around(text, rules, repeat=1_000_000_000):
    cache = []
    compare = text
    for index in itertools.count():
        for rule in rules:
            program = rule[0]

            if program == 's':
                text = spin(text, int(rule[1:]))
            if program == 'x':
                a, b = rule[1:].split('/')

                text = exchange(text, int(a), int(b))
            if program == 'p':
                a, b = rule[1:].split('/')
                text = partner(text, a, b)

        cache.append(text[:])

        if text == compare:
            mod = repeat % (index+1)
            return cache[mod-1] # ejkflpgnamhdcboi


if __name__ == "__main__":
    letters = string.ascii_lowercase[0:16]
    rules = {letter: index for index, letter in enumerate(letters)}

    with open(r'./input/day_16.txt', 'rt') as handle:
        rules = handle.read().split(",")

        part_one = find_wrap_around(letters, rules, repeat=1)
        print("Part_One: ", part_one)  # lbdiomkhgcjanefp

        part_two = find_wrap_around(letters, rules, repeat=1_000_000_000)
        print("Part_Two: ", part_two)  # ejkflpgnamhdcboi
