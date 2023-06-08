row = int(input())

matrix_flat = []

for _ in range(row):
    inner_list = [int(el) for el in input().split()]
    matrix_flat.extend(inner_list)

print(matrix_flat)
