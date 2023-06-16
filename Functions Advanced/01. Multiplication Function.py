def multiply(*args):
    total = 1
    for num in args:
        total *= num
    return total


print(multiply(1, 4, 5))
