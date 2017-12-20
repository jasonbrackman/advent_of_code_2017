def get_col(lines, c):
    column = []
    for row in range(len(lines)):
        for col in range(len(lines[row])):
            if col == c:
                column.append(lines[row][col])
    return column


if __name__ == "__main__":
    test_input = """         |          
         |  +--+    
         A  |  C    
     F---|----E|--+ 
         |  |  |  D 
         +B-+  +--+ 
    """.split('\n')

    row = 0
    col = test_input[0].find('|')
    letters = list()
    go = 'down'
    print(row, col)

    row_work = False
    col_work = True
    while True:
        if col_work:
            cols = get_col(test_input, col)
            char = cols[row]
            if go == 'undetermined':
                if row-1 >= 0 and cols[row-1] == '|':
                    go = 'up'
                    row -= 1
                else:
                    go = 'down'
                    row += 1

            elif char != '+' or char.isalpha():
                if go == 'down':
                    row += 1
                if go == 'up':
                    row -= 1
                if char.isalpha():
                    letters.append(char)
                    print(row, col, char)

            elif char == '+':
                col_work = False
                row_work = True
                go = 'undetermined'

            print(go, row, col, letters)

        elif row_work:
            rows = test_input[row]
            char = rows[col]
            if go == 'undetermined':
                if col-1 >= 0 and rows[col-1] == '-':
                    go = 'left'
                    col -= 1
                else:
                    go = 'right'
                    col += 1

            elif rows[col] != '+' or rows[col].isalpha():
                if go == 'right':
                    col += 1
                if go == 'left':
                    col -= 1
                if char.isalpha():
                    letters.append(char)

            elif rows[col] == '+':
                col_work = True
                row_work = False
                go = 'undetermined'

            print(go, row, col, letters)







