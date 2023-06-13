rows, cols = [int(x) for x in input().split()]

start = ord('a')

for row in range(start, start + rows):
    for col in range(row, row + cols):
        print(f"{chr(row)}{chr(row + col - start)}{chr(row)}", end=" ")

    print()
