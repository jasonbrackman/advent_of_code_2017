from collections import defaultdict


def get_input():
    with open(r'./input/day_23.txt', 'rt') as handle:
        lines = handle.readlines()

    commands = [line.split() for line in lines]
    return commands


def is_digit(n):
    try:
        int(n)
        return True
    except:
        return False


def optimized():
    h = 0
    b = 109300
    c = 109300 + 17_000

    while b <= c:
        g = 1
        f = 1
        d = 2

        while g != 0:
            if b % d == 0:
                f = 0
            d -= -1
            g = d - b

        if f == 0:
            h += 1
            # print(f'Round {index}: b={b}, c={c}, d={d}, h={h}')

        b += 17

    return h


if __name__ == "__main__":
    result = optimized()   # 109298 too high
                           # 909 is too low

    print('Part Two: ', result)  # 911

    debug_mode = True  # Set to True for Part One

    mul_invoked_count = 0
    registers = defaultdict(int)
    registers['a'] = 1 if debug_mode is False else 0
    current_instruction = 0
    commands = get_input()
    while True:

        cmd, *vars = commands[current_instruction]

        arg2 = int(vars[1]) if is_digit(vars[1]) else registers[vars[1]]

        if cmd == 'set':
            registers[vars[0]] = arg2
            current_instruction += 1
        elif cmd == 'sub':
            registers[vars[0]] -= arg2
            current_instruction += 1
        elif cmd == 'mul':
            mul_invoked_count += 1
            registers[vars[0]] *= arg2
            current_instruction += 1
        elif cmd == 'jnz':
            arg1 = int(vars[0]) if is_digit(vars[0]) else registers[vars[0]]
            if arg1 != 0:
                current_instruction += arg2
            else:
                current_instruction += 1

        print(registers, mul_invoked_count, current_instruction)  # part one 8281