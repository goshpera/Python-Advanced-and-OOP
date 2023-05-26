numbers_dict = {}

while True:
    line = input()
    if line == "Search":
        break

    num_as_str = line
    num_as_int = int(input())
    numbers_dict[num_as_str] = num_as_int

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

    if line in numbers_dict:
        numbers_dict.pop(line)

print(numbers_dict)
