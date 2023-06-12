rows, cols = [int(x) for x in input().split()]

matrix = []

for _ in range(rows):
    inner_list = [int(el) for el in input().split()]
    matrix.append(inner_list)