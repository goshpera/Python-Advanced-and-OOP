rows = int(input())

matrix = []

for _ in range(rows):
    inner_list = list(input())  #'abc' turns into ['a', 'b', 'c'] this way
    matrix.append(inner_list)

searched_symbol = input()
position = None

for row_idx in range(rows):
    if position:
        break

    for col_idx in range(rows):
        if matrix[row_idx][col_idx] == searched_symbol:
            position = (row_idx, col_idx)
            break

if position:
    print(position)
else:
    print(f"{searched_symbol} does not occur in the matrix.")
