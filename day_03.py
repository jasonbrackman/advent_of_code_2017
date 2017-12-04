"""
Example:
17  16  15  14  13
18   5   4   3  12
19   6   1   2  11
20   7   8   9  10
21  22  23---> ...
"""


RIGHT = 0
UP = 1
LEFT = 2
DOWN = 3
helpers = {RIGHT: "RIGHT",
           UP: "UP",
           LEFT: "LEFT",
           DOWN: "DOWN"}


def get_direction(rows):

    # Exit early
    if len(rows) == 0:
        return RIGHT

    # First row starts at one
    if len(rows) <= 1 and len(rows[0]) <= 1:
        return RIGHT

    if len(rows) == 1 and len(rows[0]) == 2:
        return UP

    if len(rows) > 1:
        min_ = min(len(x) for x in rows)
        results = list()
        for index, row in enumerate(rows):
            if len(row) == min_:
                results.append(index)

        min_row_length = len(rows[results[0]])
        top_row_length = len(rows[0])
        bot_row_length = len(rows[-1])
        # print("len(min_row): ", min_row_length)
        # print("len(top_row): ", top_row_length)
        # print("len(bot_row): ", bot_row_length)

        row_first = max(int(x) for x in rows[0])
        row_last = max(int(x) for x in rows[-1])

        # even rows?
        if len(results) == len(rows):
            if row_last > row_first:
                if str(row_last) in rows[-1][0]:
                    return DOWN
                return RIGHT

            if row_first > row_last:

                if str(row_first) == rows[0][-1]:
                    return UP
                if str(row_first) == rows[0][0]:
                    return LEFT

        # Uneven rows
        else:
            if min_row_length == top_row_length:
                if row_first > row_last:
                    if str(row_first) in rows[0][0]:
                        return LEFT
                    return UP
                if row_last > row_first:
                    if bot_row_length - min_row_length == 1:
                        return UP

                    return RIGHT

            # # Determine if we DOWN a level OR go RIGHT
            # if the min row length less than the top row
            if min_row_length < top_row_length:
                if results[0]+1 == len(rows):
                    # print("looking at row: ", results[0]+1, 'of ', len(rows))
                    if min_row_length < top_row_length and min_row_length == bot_row_length:
                        if top_row_length - bot_row_length == 1:

                            if row_first > row_last:
                                return DOWN
                            else:
                                return RIGHT

                    if min_row_length == bot_row_length:
                        return RIGHT

                    if top_row_length > bot_row_length:
                        return DOWN

                    return DOWN
                else:
                    return DOWN

            else:
                return UP

        if len(rows[0]) > min_row_length and len(results) + 1 == len(rows):
            return DOWN

    # print("DEFAULT LEFFT")

    return LEFT


def get_current_location(current_spiral, number):
    # get current location
    for index, row in enumerate(current_spiral):
        if str(number) in row:
            current_row = index
            current_col = row.index(str(number))
            return current_row, current_col


def get_sum_of_adjacent_squares(current_spiral, current_row, current_col):
    to_sum = list()

    # collect numbers from all adjacent squares.
    for row in range(current_row - 1, current_row + 2):
        for col in range(current_col - 1, current_col + 2):
            try:
                if row >= 0 and col >= 0:
                    # print('.', end='')
                    to_sum.append(int(current_spiral[row][col]))
            except:
                pass
    return sum(to_sum)


def build_spiral(number, special=False):
    numbers = [str(x + 1) for x in range(number)]
    level = 0
    results = []
    for n in numbers:

        directions = get_direction(results)
        # print(helpers[directions], ' = ', n)
        if len(results) == 0:
            results.append([])
            results[level].append(n)
            continue

        if directions == RIGHT:
            results[level].append(n)

        if directions == LEFT:
            results[level].insert(0, n)

        if directions == UP:
            if level == 0:
                results.insert(0, [n])
            else:
                level -= 1
                results[level].append(n)

        if directions == DOWN:
            # print("Current Level: ", level)
            # print("len(results):", len(results))

            if level < len(results)-1:
                # print("fill in existing row...")
                level += 1
                results[level].insert(0, n)
            else:
                # print("Create a new row")
                results.append([n])
                level += 1

    return results


def count_steps(number, plus=0):
    rows = build_spiral(number+plus)
    max_length = max([len(row) for row in rows])
    same_length = all(len(row) == max_length for row in rows)
    min_length = min([len(row) for row in rows])

    if same_length:
        center_col = 0
        center_row = 0
        for index, row in enumerate(rows):
            if str(1) in row:
                center_row = index
                center_col = row.index(str(1))

        print("CENTER INFO: {} - {}".format(center_row, center_col))

        for index, row in enumerate(rows):
            if str(number) in row:
                print("Looking for ", number)

                return abs(index - center_row) + abs((row.index(str(number))) - center_col)
    print("try again by adding: ", max_length - min_length)
    return False


def count_steps_with_padding(number):
    for index in range(100):
        test = count_steps(number, plus=index)
        if test is not False:
            return test


def not_sure(number):
    old_rows = build_spiral(number)
    new_rows = [['0' for _ in row] for row in old_rows]

    for index in range(1, number+1):
        current_row, current_col = get_current_location(old_rows, index)

        if index == 1:
            new_rows[current_row][current_col] = index

        else:
            new_number = get_sum_of_adjacent_squares(new_rows, current_row, current_col)
            new_rows[current_row][current_col] = new_number

    for index, row in enumerate(new_rows):
        # looking for a number > 265149
        for item in row:
            if int(item) > 265149:
                return item


print("Part 1: ", count_steps(265149, plus=76))
print("Part 2: ", not_sure(64))



# print(count_steps_with_padding(265149))
# for row in build_spiral(23):
#     for x in row:
#         print('{:03} '.format(int(x)), end='')
#     print("\n")
#     #print(row)