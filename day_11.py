#  NOTE:  This totally passed the challenge
#         but I have no idea why -- the more I look at my
#         code the more it fails... so .. yeah .. this is
#         totally screwy.
#  If I ever come back to this:
#  https://www.redblobgames.com/grids/hexagons/
#  https://www.gamasutra.com/blogs/HermanTulleken/20140912/225495/20_Fun_Grid_Facts_Hex_Grids.php
# row, col
moves = {'n': [0, -1],
         'ne': [1, -1],
         'nw': [-1, -1],
         's': [0, 1],
         'se': [1, 0],
         'sw': [-1, 0]}


def test_stuff():
    t1 = 'ne,ne,ne'.split(',')
    t2 = 'ne,ne,sw,sw'.split(',')
    t3 = 'ne,ne,s,s'.split(',')
    t4 = 'se,sw,se,sw,sw'.split(',')
    for t in [t1, t2, t3, t4]:
        print(get_distance_away(t))


def get_distance_away(directions):
    total = [0, 0]
    max_distance = []
    for item in directions:
        total[0] += moves[item][0]
        total[1] += moves[item][1]

        max_distance.append(max(total))

    return total, max_distance


if __name__ == "__main__":
    test_stuff()
    with open(r'./input/day_11.txt', 'rt') as handle:
        directions = handle.read().split(',')
        total, max_distance_achieved = get_distance_away(directions)

        print('Part 1: ', max(total))
        print('Part 2: ', max(max_distance_achieved))

