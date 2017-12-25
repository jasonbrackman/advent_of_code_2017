
import collections


class Particle:

    def __init__(self, px, py, pz,
                       vx, vy, vz,
                       ax, ay, az):
        self.posX = int(px)
        self.posY = int(py)
        self.posZ = int(pz)

        self.velX = int(vx)
        self.velY = int(vy)
        self.velZ = int(vz)

        self.accX = int(ax)
        self.accY = int(ay)
        self.accZ = int(az)

    def get_absolute_pos(self):
        return sum([abs(self.posX), abs(self.posY), abs(self.posZ)])

    def get_position(self):
        return self.posX, self.posY, self.posZ


def get_buffer():
    with open(r'./input/day_20.txt', 'rt') as handle:
        lines = handle.readlines()
        lines = [line.replace("'", '').split(' ') for line in lines]

    buffer = list()
    for line in lines:

        pva = {}
        for item in line:
            type_, xyz = item.split('=')
            x, y, z, *_ = (xyz.replace('<', '').replace('>', '').split(','))
            pva[type_] = [x, y, z]

        buffer.append(Particle(*pva['p'], *pva['v'], *pva['a']))

    return buffer


def update_particles(buffer):
    for particle in buffer:
        # increase the x velocity by the x acceleration
        particle.velX += particle.accX

        # increase the y velocity by teh y acceleration
        particle.velY += particle.accY

        # increase the z velocity by the z acceleration
        particle.velZ += particle.accZ

        # increase the x position by the x velocity
        particle.posX += particle.velX

        # increase the y position by the y velocity
        particle.posY += particle.velY

        # increase the z position by the z velocity
        particle.posZ += particle.velZ

    return buffer


def part_one():
    # for part one
    d = collections.defaultdict(int)
    buffer = get_buffer()
    for tick in range(len(buffer)):
        buffer = update_particles(buffer)
        positions = [particle.get_absolute_pos() for particle in buffer]
        d[positions.index(min(positions))] += 1
    key = None
    highest = 0
    for k, v in d.items():
        if v > highest:
            highest = v
            key = k
    print("Part One: ", key)  # 125


if __name__ == "__main__":
    part_one()

    buffer = get_buffer()

    for tick in range(len(buffer)):
        buffer = update_particles(buffer)

        positions = collections.Counter([particle.get_position() for particle in buffer])

        buffer = [b for b in buffer if positions[b.get_position()] == 1]

    print("Part Two: ", len(buffer))  # 461


