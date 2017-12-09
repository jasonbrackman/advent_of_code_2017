"""{}, score of 1.
{{{}}}, score of 1 + 2 + 3 = 6.
{{} ,{}}, score of 1 + 2 + 2 = 5.
{{{} ,{} ,{{}}}}, score of 1 + 2 + 3 + 3 + 3 + 4 = 16.
{< a >, < a >, < a >, < a >}, score of 1.
{{ < ab >}, { < ab >}, { < ab >}, { < ab >}}, score of 1 + 2 + 2 + 2 + 2 = 9.
{{ <!! >}, { <!! >}, { <!! >}, { <!! >}}, score of 1 + 2 + 2 + 2 + 2 = 9.
{{ < a! >}, { < a! >}, { < a! >}, { < ab >}}, score of 1 + 2 = 3."""

import re


def count_braces(input):
    score = 0
    depth = 0
    for item in input:
        if item == "{":
            depth += 1
        if item == "}":
            score += depth
            depth -= 1
    return score


def get_bracketed_value(input):
    baddies = 0

    # clean input up a bit
    input = input.replace('!!', '')
    input = input.replace("!>", '')

    # Find garbage
    pattern = re.compile(r'(\<.*?\>)')
    for item in pattern.findall(input):
        # Calculate amount of garbage
        extra_baddies = item.count("!")
        baddies += len(item) - 2 - (extra_baddies * 2)

    # Remove Garbage
    input = re.sub(pattern, '', input)

    print("Part Two: ", baddies)

    # Return clean data
    return input


if __name__ == "__main__":
    with open(r'./input/day_09.txt', 'rt') as handle:
        input = handle.readline()

    input = get_bracketed_value(input)

    # not 2768, 2212
    print("Part One: ", count_braces(input))


