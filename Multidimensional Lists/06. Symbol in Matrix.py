rows = int(input())

matrix = []

for _ in range(rows):
    inner_list = [el for el in input().split()]
    matrix.append(inner_list)
