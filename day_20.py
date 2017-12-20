def get_buffer():
    with open(r'./input/day_20.txt', 'rt') as handle:
        lines = handle.readlines()
        lines = [line.replace("'", '').split(' ') for line in lines]


    buffer = list()
    for line in lines:
        print(line)
        1/0
        for item in line:
            print(item)
            1/0
            parts = item.replace("<", "").replace("'", "").replace(">", "").strip()
            p = parts[0]
            print('parts:', parts)
            1/0

    # for particle in buffer:
    #     print(particle)
    return lines

def update_particles(buffer):
    # increase the x velocity by the x acceleration
    # increase the y velocity by teh y acceleration
    # increase the z velocity by the z acceleration
    # increase the x position by the x velocity
    # increase the y position by the y velocity
    # increase the z position by the z velocity
    return buffer



if __name__ == "__main__":
    # p = position(x, y, z)
    # v = velocity(x, y, z)
    # a = acceleration(x, y, z)
    # format: particle(p, v, a)
    buffer = get_buffer()
    pass

