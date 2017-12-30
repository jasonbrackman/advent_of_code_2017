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



class Grid:
    INFECTED = '#'
    CLEAN = '.'

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

        original = self.grid[self.carrier.location]
        temp = f'[{original}]'
        self.grid[self.carrier.location] = temp
        center = self.grid_size // 2
        container = []

        for x in range(0, self.grid_size):
            container.append([])
            for y in range(0, self.grid_size):
                container[x].append(self.grid.get((x-center, y-center), '.'))

        for line in container:
            print("".join(x.center(3) for x in line))
            print()

        self.grid[self.carrier.location] = original

    def burst(self):

        position = self.carrier.location

        # In place direction turn
        if self.grid[position] == self.INFECTED:
            self.carrier.change_direction(self.carrier.RIGHT)
        else:
            self.carrier.change_direction(self.carrier.LEFT)

        # Clean or infect grid position
        if self.grid[position] != self.INFECTED:
            self.infection_counter += 1
        self.grid[position] = '.' if self.grid[position] == self.INFECTED else '#'

        # finally move the carrier forward in its current direction
        self.carrier.move()
        if self.carrier.location not in self.grid:
            self.grid_size += 1
            self.grid[self.carrier.location] = self.CLEAN


if __name__ == "__main__":
    grid = Grid()
    # grid.pprint()
    # print("--")
    for _ in range(10000):
        grid.burst()
    grid.pprint()
    print(grid.infection_counter)

