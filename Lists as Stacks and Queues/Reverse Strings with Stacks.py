text = input()

stack_text = list(text)

while stack_text:
    reversed_char = stack_text.pop()
    print(reversed_char, end="")

#for a simpler and stack-free solution, use [:-1]
