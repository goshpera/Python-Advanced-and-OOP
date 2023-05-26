numbers_dict = {}

while True:
    line = input()
    if line == "Search":
        break

    num_as_str = line
    try:
        num_as_int = int(input())
        numbers_dict[num_as_str] = num_as_int
    except ValueError:
        print("The variable must be an integer")


while True:
    line = input()
    if line == "Remove":
        break

    try:
        print(numbers_dict[line])
    except KeyError:
        print("Number does not exist in dictionary")

while True:
    line = input()
    if line == "End":
        break

    try:
        numbers_dict.pop(line)
    except KeyError:
        print("Number does not exist in dictionary")


print(numbers_dict)
