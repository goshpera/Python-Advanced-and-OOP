rows, cols = [int(x) for x in input().split(", ")]

matrix = []
sum_nums = 0

for _ in range(rows):
    inner_list = [int(el) for el in input().split(", ")]
    sum_nums += sum(inner_list)
    matrix.append(inner_list)

'''
!!!that's a nested loop variation to sum all the numbers in the matrix!!!
sum_nums = 0
for row_idx in range(rows):
    for col_idx in range(cols):
        sum_nums += matrix[row_idx][col_idx]
'''


print(sum_nums)
print(matrix)
