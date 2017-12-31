from collections import defaultdict

import time


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


if __name__ == "__main__":
    debug_mode = True

    mul_invoked_count = 0
    registers = defaultdict(int)
    registers['a'] = 1 if debug_mode is False else 0
    current_instruction = 0
    commands = get_input()
    while True:

        cmd, *vars = commands[current_instruction]

        arg2 = int(vars[1]) if is_digit(vars[1]) else registers[vars[1]]

        # print(cmd, vars[0], arg2)

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



        print(mul_invoked_count, current_instruction)  # part one 8281
        print(registers)
        # time.sleep(0.5)