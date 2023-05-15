stack_parent = []
text = input()

for index in range(len(text)):
    if text[index] == "(":
        stack_parent.append(index)
    elif text[index] == ")":
        start_pos = stack_parent.pop()
        end_pos = index
        print(text[start_pos:end_pos + 1])
