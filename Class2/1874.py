import sys
from collections import deque

number_list = list(map(int, sys.stdin.read().splitlines()))[1:]

dq = deque()

print(number_list)
current = number_list[0]
for i in range(current):
    dq.append(i + 1)
print(dq, current)
for i in number_list:  
    pass

