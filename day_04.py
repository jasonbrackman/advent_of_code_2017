
def anagram(words):
    words_c = words[:]
    valid = True
    for word in words:
        words_c.remove(word)
        for word_c in words_c:
            if sorted(word) == sorted(word_c):
                valid = False
    return valid


def do_work(input, ag=False):
    counter = 0
    for item in input.split('\n'):
        x = [i.strip() for i in item.split()]
        if ag:
            if anagram(x):
                counter += 1
        else:
            if len(x) == len(set(x)):
                counter += 1

    return counter


if __name__ == "__main__":
    with open(r'./input/day_04.txt', 'rt') as handle:
        aoc_input = handle.read()
    print("Part One: ", do_work(aoc_input))
    print("Part Two: ", do_work(aoc_input, ag=True))


