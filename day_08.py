from collections import defaultdict

registers = """b inc 5 if a > 1
a inc 1 if b < 5
c dec -10 if a >= 1
c inc -20 if c == 10"""

operators = {'>': "__gt__",
             '<': "__lt__",
             '>=': "__ge__",
             '<=': "__le__",
             '==': "__eq__",
             '!=': "__ne__"}

registers_ = defaultdict(int)
# for item in string.ascii_lowercase:
#     registers_[item] = 0

max_value = 0
def process_instruction(instruction):

    # parse data
    register_01, computation, value_01, _, register_02, operator, value_02 = instruction.split()
    computation = '__add__' if computation == 'inc' else '__sub__'
    value_01 = int(value_01)
    value_02 = int(value_02)

    # do some dynamic restructuring
    if getattr(registers_[register_02], operators[operator])(value_02):
        new_value = getattr(registers_[register_01], computation)(value_01)

        # quick and dirty collection of max value
        global max_value
        if new_value > max_value:
            max_value = new_value

        # update register`
        registers_[register_01] = new_value


if __name__ == "__main__":
    with open(r'./input/day_08.txt', 'rt') as handle:
        puzzle = handle.readlines()
        for register in puzzle:
            # print(register)
            process_instruction(register)
        all = [(v, k) for k, v in registers_.items()]

    print("Part 1: ", max(all))  # 5946 expected
    print("Part 2: ", max_value)  # 6026 expected
