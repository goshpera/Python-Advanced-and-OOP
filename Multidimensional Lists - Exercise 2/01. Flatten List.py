line = input().split("|")

sub_lists = []

for sub_str in line[::-1]:
    sub_lists.extend(sub_str.split())

print(*sub_lists)

'''
comprehension:
numbers = [string.split() for string in input().split("|")]
print(*[' '.join(sub_list) for sub_list in numbers[::-1]])
'''