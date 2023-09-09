rows = [295743861, 431865927, 876192543, 387459216, 612387495, 549216738, 763524189, 928671354, 154938672]

for i in range(9):
    rows[i] = str(rows[i])

if len(rows) != 9:
    print("Valid? No -", len(rows), "rows")
    exit()

for row in rows:
    if len(row) != 9:
        print(row)
        print("Valid? No -", "row", rows.index(row) + 1, len(row), "nums")
        exit()

print("+-------" * 3, "+", sep="")
row_count = 1
for row in rows:
    col_count = 1
    print("| ", end="")
    for num in row:
        print(num, end="")
        if col_count == 3:
            print(" | ", end="")
            col_count = 1
        else:
            print(" ", end="")
            col_count += 1
    print("")
    if row_count == 3:
        print("+-------" * 3, "+", sep="")
        row_count = 1
    else:
        row_count += 1

print("rows: ", rows)

checkList = [str(i) for i in range(1, 10)]

for row in rows:
    for num in checkList:
        if num not in row:
            print("Valid? No -", "row", rows.index(row) + 1, ", missing number", num)
            exit()

cols = ["" for i in range(9)]

for row in rows:
    for i in range(9):
        cols[i] += row[i]
print("cols: ", cols)

for col in cols:
    for num in checkList:
        if num not in col:
            print("Valid? No -", "col", cols.index(col) + 1, ", missing number", num)
            exit()

squares = []
for i in range(9):
    squares.append("")

for i in range(0, 3):
    squares[0] += rows[i][0:3]
    squares[1] += rows[i][3:6]
    squares[2] += rows[i][6:9]
for i in range(3, 6):
    squares[3] += rows[i][0:3]
    squares[4] += rows[i][3:6]
    squares[5] += rows[i][6:9]
for i in range(6, 9):
    squares[6] += rows[i][0:3]
    squares[7] += rows[i][3:6]
    squares[8] += rows[i][6:9]
print("sqrs: ", squares)

for square in squares:
    for num in checkList:
        if num not in square:
            print("Valid? No -", "square", squares.index(square) + 1, ", missing number", num)
            exit()

print("Valid? Yes")