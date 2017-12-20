def get_col(lines, c):
    column = []
    for row in range(len(lines)):
        for col in range(len(lines[row])):
            if col == c:
                column.append(lines[row][col])
    return column


def get_input():
    with open(r'./input/day_19.txt', 'rt') as handle:
        test_input = handle.read().split('\n')
        test_input = [t.ljust(200) for t in test_input]
    return test_input


if __name__ == "__main__":
    test_input = """         |          
         |  +--+    
         A  |  C    
     F---|----E|--+ 
         |  |  |  D 
         +B-+  +--+ 
    """.split('\n')

    test_input = get_input()
    steps = 0
    row = 0
    col = test_input[0].find('|')
    letters = list()
    go = 'down'

    row_work = False
    col_work = True
    while True:
        if col_work:
            cols = get_col(test_input, col)
            # print('Col length: ', len(cols))

            char = cols[row]

            if go == 'undetermined':
                if row-1 >= 0 and cols[row-1] != ' ':

                    go = 'up'
                    row -= 1
                    steps += 1
                else:
                    go = 'down'
                    row += 1
                    steps += 1

                # print("Direction Change:", go)
            elif char != '+' or char.isalpha():
                if go == 'down':
                    row += 1
                    steps += 1
                if go == 'up':
                    row -= 1
                    steps += 1
                if char.isalpha():
                    letters.append(char)
                    print(go, row, col, letters, char)
                    if cols[row] == ' ':
                        print("Done!")
                        break

            elif char == '+':
                col_work = False
                row_work = True
                go = 'undetermined'

        elif row_work:
            rows = test_input[row]

            char = rows[col]

            if go == 'undetermined':
                if col-1 >= 0 and rows[col-1] != ' ':
                    go = 'left'
                    col -= 1
                    steps += 1
                else:
                    go = 'right'
                    col += 1
                    steps += 1
                # print("Direction Change:", go)

            elif rows[col] != '+' or rows[col].isalpha():
                if go == 'right':
                    col += 1
                    steps += 1
                else:
                    col -= 1
                    steps += 1
                if char.isalpha():
                    letters.append(char)
                    print(go, row, col, letters, char)
                    if rows[col] == ' ':
                        print("Done!")
                        break

            elif rows[col] == '+':
                col_work = True
                row_work = False
                go = 'undetermined'

    print('Part One: ', "".join(letters)) # EPYDUXANIT
    print('Part Two: ', steps)


