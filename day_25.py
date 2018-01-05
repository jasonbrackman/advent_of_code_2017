"""

    A tape which contains 0 repeated infinitely to the left and right.
    A cursor, which can move left or right along the tape and read or write values at its current position.
    A set of states, each containing rules about what to do based on the current value under the cursor.

"""


class Tape:
    round = 0

    def __init__(self, stop):
        self.slots = [0]
        self.cursor = 0
        self.stop = stop

    def move_cursor_right(self):
        self.cursor += 1
        if len(self.slots)-1 < self.cursor:
            self.slots.append(0)

    def move_cursor_left(self):
        self.cursor -= 1
        if self.cursor == -1:
            self.cursor = 0
            self.slots.insert(0, 0)

    def state_a(self):

        self.should_continue()

        if self.slots[self.cursor] == 0:
            self.slots[self.cursor] = 1
            self.move_cursor_right()
            return self.state_b

        else:
            self.slots[self.cursor] = 0
            self.move_cursor_left()
            return self.state_c

    def state_b(self):
        self.should_continue()
        if self.slots[self.cursor] == 0:
            self.slots[self.cursor] = 1
            self.move_cursor_left()
            return self.state_a

        else:
            self.slots[self.cursor] = 1
            self.move_cursor_left()
            return self.state_d

    def state_c(self):
        self.should_continue()

        if self.slots[self.cursor] == 0:
            self.slots[self.cursor] = 1
            self.move_cursor_right()
            return self.state_d

        else:
            self.slots[self.cursor] = 0
            self.move_cursor_right()
            return self.state_c

    def state_d(self):
        self.should_continue()

        if self.slots[self.cursor] == 0:
            self.slots[self.cursor] = 0
            self.move_cursor_left()
            return self.state_b

        else:
            self.slots[self.cursor] = 0
            self.move_cursor_right()
            return self.state_e

    def state_e(self):
        self.should_continue()

        if self.slots[self.cursor] == 0:
            self.slots[self.cursor] = 1
            self.move_cursor_right()
            return self.state_c

        else:
            self.slots[self.cursor] = 1
            self.move_cursor_left()
            return self.state_f

    def state_f(self):
        self.should_continue()

        if self.slots[self.cursor] == 0:
            self.slots[self.cursor] = 1
            self.move_cursor_left()
            return self.state_e

        else:
            self.slots[self.cursor] = 1
            self.move_cursor_right()
            return self.state_a

    def should_continue(self):
        # print(self.slots)

        if self.round == self.stop:
            raise Exception(f"Stoppping at round {round}: DIAGNOSTIC CHECKSUM = {self.slots.count(1)}")
        else:
            self.round += 1

    def go(self, func):
        while True:
            func = func()


if __name__ == "__main__":
    tape = Tape(stop=12656374)

    tape.go(tape.state_a)  # 2526

