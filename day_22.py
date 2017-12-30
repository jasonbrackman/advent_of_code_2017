# Infinite 2d grid
# each node on the grid is 'clean' or 'infected'
# one node is a 'virus carrier' - it is always in the 'current node' and knows its 'direction'


class Node:
    # Directions (local to Node)
    UP = (-1, 0)
    RIGHT = (0, 1)
    DOWN = (1, 0)
    LEFT = (0, -1)
    DIRECTIONS = [UP, RIGHT, DOWN, LEFT]
    facing = 0

    def __init__(self):
        self.location = (0, 0)
        self.direction = self.DIRECTIONS[0]  # default is UP

    def change_direction(self, direction):
        self.facing += 1 if direction == self.RIGHT else -1

        a, b = self.direction
        c, d = direction
        self.direction = ((a+c), (b+d))

    def move(self):
        a, b = self.location
        c, d = self.DIRECTIONS[self.facing % len(self.DIRECTIONS)]
        self.location = ((a + c), (b + d))
        # print('loc:', self.location)


class Grid:
    CLEAN = '.'
    WEAKENED = 'W'
    INFECTED = '#'
    FLAGGED = 'F'
    STATES = [CLEAN, WEAKENED, INFECTED, FLAGGED]

    grid = dict()
    grid_size = 0

    infection_counter = 0

    def __init__(self):
        self.init_grid()
        self.carrier = Node()

    def init_grid(self):
        with open('./input/day_22.txt', 'rt') as handle:
            lines = handle.read().split('\n')
        self.grid_size = len(lines)
        center = self.grid_size // 2
        for row, line in enumerate(lines):
            for col, character in enumerate(line):
                self.grid[(row-center, col-center)] = character

    def pprint(self):
        # print("GRID SIZE:", self.grid_size)
        # print(self.carrier.location)
        original = self.grid[self.carrier.location]
        temp = f'[{original}]'
        self.grid[self.carrier.location] = temp
        center = self.grid_size // 2
        container = []

        for x in range(0, self.grid_size):
            container.append([])
            for y in range(0, self.grid_size):
                container[x].append(self.grid.get((x-center, y-center), self.CLEAN))

        for line in container:
            print("".join(x.center(3) for x in line))

        self.grid[self.carrier.location] = original

    def burst(self):

        position = self.carrier.location
        self.update_carrier_direction(position)
        self.update_position_state(position)

        # finally move the carrier forward in its current direction
        self.carrier.move()
        a, b = self.carrier.location
        if abs(a) >= self.grid_size-1 or abs(b) >= self.grid_size-1:
            self.grid_size += 1
        if self.carrier.location not in self.grid:
            self.grid[self.carrier.location] = self.CLEAN

    def update_carrier_direction(self, position):
        grid_state = self.grid[position]

        if grid_state == self.INFECTED:
            self.carrier.change_direction(self.carrier.RIGHT)

        elif grid_state == self.CLEAN:
            self.carrier.change_direction(self.carrier.LEFT)

        elif grid_state == self.FLAGGED:
            self.carrier.change_direction(self.carrier.RIGHT)
            self.carrier.change_direction(self.carrier.RIGHT)

    def update_position_state(self, position):
        current_state = self.grid[position]
        index = self.STATES.index(current_state)
        new_state = self.STATES[(index+1) % len(self.STATES)]
        if new_state == self.INFECTED:
            self.infection_counter += 1

        # print(current_state, '->', new_state)
        self.grid[position] = new_state


if __name__ == "__main__":
    grid = Grid()

    for _ in range(10000000):
        grid.burst()
    grid.pprint()
    print(grid.infection_counter)

