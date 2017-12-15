


"""--Gen. A--  --Gen. B--
       1092455   430625591
    1181022009  1233683848
     245556042  1431495498
    1744312007   137874439
    1352636452   285222916"""

def generator_a(start):
    divisor = 2147483647
    while True:
        start = start * 16807 % divisor
        if start % 4 == 0:
            yield bin(start)[-16:]


def generator_b(start):
    divisor = 2147483647
    while True:
        start = start * 48271 % divisor
        if start % 8 == 0:
            yield bin(start)[-16:]


if __name__ == "__main__":
    # test data: after 40million 588 pairs should match
    # start_a = 65
    # start_b = 8921

    # problem One data
    start_a = 277
    start_b = 349

    a = generator_a(start_a)
    b = generator_b(start_b)

    count = 0
    for _ in range(5_000_000):
        if next(a) == next(b):
            count += 1

    print("Part Two: ", count)