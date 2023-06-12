rows, cols = [int(x) for x in input().split(", ")]

matrix = []
max_sum = float('-inf')
sub_matrix = []

for _ in range(rows):
    inner_list = [int(el) for el in input().split(", ")]
    matrix.append(inner_list)

for row_idx in range(rows - 1):
    for col_idx in range(cols - 1):
        #We limit the rows and cols loops with 1 less than their values, so we don't get an idx out of range error
        current_el = matrix[row_idx][col_idx]
        bellow_el = matrix[row_idx + 1][col_idx]
        next_el = matrix[row_idx][col_idx + 1]
        diagonal_el = matrix[row_idx + 1][col_idx + 1]
        current_sum_elements = current_el + bellow_el + next_el + diagonal_el

        if max_sum < current_sum_elements:
            max_sum = current_sum_elements
            sub_matrix = [[current_el, next_el], [bellow_el, diagonal_el]]

print(*sub_matrix[0])
print(*sub_matrix[1])
print(max_sum)
