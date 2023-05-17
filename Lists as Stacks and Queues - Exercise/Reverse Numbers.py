from collections import deque

#solution 1

numbers = deque(input().split())

for _ in range(len(numbers)):
    print(numbers.pop(), end=" ")


'''
#solution 2
nums = deque(input().split())
nums.reverse()
print(' '.join(nums))
'''
