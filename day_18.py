import string
from itertools import cycle, islice
from collections import defaultdict

import itertools

import time


def get_input():
    with open(r'./input/day_18.txt', 'rt') as handle:
        lines = handle.readlines()

    return lines


"""
    snd X plays a sound with a frequency equal to the value of X.
    set X Y sets register X to the value of Y.
    add X Y increases register X by the value of Y.
    mul X Y sets register X to the result of multiplying the value contained in register X by the value of Y.
    mod X Y sets register X to the remainder of dividing the value contained in register X by the value of Y (that is, it sets X to the result of X modulo Y).
    rcv X recovers the frequency of the last sound played, but only when the value of X is not zero. (If it is zero, the command does nothing.)
    jgz X Y jumps with an offset of the value of Y, but only if the value of X is greater than zero. (An offset of 2 skips the next instruction, an offset of -1 jumps to the previous instruction, and so on.)

"""
program0 = []
program1 = []

prog0 = dict()
prog1 = dict()


def is_digit(n):
    try:
        int(n)
        return True
    except:
        return False


def do_instructions(input, from_=0):
    sound = 0
    registers = defaultdict(int)
    current_instruction = from_
    for _ in itertools.count():
        # print(registers)
        cmd, *vars = input[current_instruction].split()
        print(cmd, vars)

        if cmd == 'add':
            arg2 = int(vars[1]) if is_digit(vars[1]) else registers[vars[1]]
            registers[vars[0]] += arg2
        elif cmd == 'mul':
            arg2 = int(vars[1]) if is_digit(vars[1]) else registers[vars[1]]
            registers[vars[0]] *= arg2
        elif cmd == 'mod':
            arg2 = int(vars[1]) if is_digit(vars[1]) else registers[vars[1]]
            # print(registers[vars[0]])
            registers[vars[0]] %= arg2
        elif cmd == 'snd':
            sound = registers[vars[0]]
        elif cmd == 'set':
            arg2 = int(vars[1]) if is_digit(vars[1]) else registers[vars[1]]
            registers[vars[0]] = arg2
        elif cmd == 'rcv':
            if registers[vars[0]] > 0:
                return sound
        elif cmd == 'jgz':
            arg2 = int(vars[1]) if is_digit(vars[1]) else registers[vars[1]]
            if registers[vars[0]] > 0:
                current_instruction += arg2
                continue

        current_instruction += 1
    return sound


def do_instructions2(pid, p1, p0, input):
    count = 0
    registers = defaultdict(int)
    registers['p'] = pid
    current_instruction = 0
    for _ in itertools.count():
        cmd, *vars = input[current_instruction].split()
        print(cmd, vars)

        if len(vars) == 2:
            arg2 = int(vars[1]) if is_digit(vars[1]) else registers[vars[1]]

        if cmd == 'add':
            registers[vars[0]] += arg2

        elif cmd == 'mul':
            registers[vars[0]] *= arg2

        elif cmd == 'mod':
            registers[vars[0]] %= arg2

        elif cmd == 'set':
            registers[vars[0]] = arg2

        elif cmd == 'jgz':
            if registers[vars[0]] > 0:
                current_instruction += arg2
                # print("Current instruction: ", current_instruction)
                continue

        elif cmd == 'snd':
            print("[{}] Sending: {} (msg: {})".format(pid, registers[vars[0]], count))
            p0.append(registers[vars[0]])
            count += 1

        elif cmd == 'rcv':
            while len(p1) == 0 and p0 is not None:
                print("[{}] Waiting...".format(pid))
                yield
                time.sleep(0.1)

            if len(p1) == 0 and p0 is None:
                print("[{}] Deadlock".format(pid))
                1 / 0

            x = p1.pop(0)
            registers[vars[0]] = x
            print("[{}] Received: {}".format(pid, x), 'Count:', count)  # 256/257 is too low

            yield

        current_instruction += 1
    p1 = None
    print("Exiting:", pid, "after sending:", count, "items")

    return


def do_stuff(pid, p1, p0):
    print("Hello my name is", pid)
    stuff = """snd 1
    snd 2
    snd p
    rcv a
    rcv b
    rcv c
    rcv d""".split("\n")

    count = 0
    registers = defaultdict(int)
    for item in stuff:
        cmd, *vars = item.split()
        print(cmd, vars)
        if cmd == 'snd':
            p0.append(registers[vars[0]])
            count += 1
            print(pid, p0)
            yield
        elif cmd == 'rcv':
            while len(p1) == 0 and len(p0) > 0:
                time.sleep(1)
                print("1:", program1)
                print("0:", p0)

            if len(p1) == 0 and len(p0) == 0:
                print("Deadlock")
                print("Exiting: ", pid, 'after sending', count)
                print(registers['c'])
                1 / 0

            print("Received: ", pid, p1.pop(0))
            yield

    print("Exiting: ", pid, 'after sending', count)
    return


if __name__ == "__main__":
    input = get_input()
    instructions = [item for item in input]
    print("Part One: ", do_instructions(instructions))  # 7071

    # a = do_instructions2(0, program1, program0, instructions)
    # b = do_instructions2(1, program0, program1, instructions)
    # while True:
    #     next(a)
    #     next(b)

    a = do_stuff(0, program1, program0)
    b = do_stuff(1, program0, program1)

    for _ in range(10):
        next(a)
        next(b)
