import sys
from collections import deque

n = int(sys.stdin.readline())

class_list = deque(map(int, sys.stdin.readline().strip().split()))
now = class_list.popleft()
count = 1
answer = deque()
while class_list: 
    next = class_list.popleft()
    if now == next:
        count += 1
    else:
        answer.append([now, count])
        count = 1
        now = next
else:
    answer.append([now, count])

a, b = answer.popleft()
while answer:
    answer.popleft()
print(answer)