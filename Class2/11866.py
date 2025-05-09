import sys
from collections import deque

n, m = map(int, sys.stdin.readline().strip().split())
dq = deque([i + 1 for i in range(n)])
count = 0
print('<', end='')
answer = []
while sum(dq) != 0:
    num = dq.popleft()
    count += 1
    if count % m == 0:
        answer.append(str(num))
    else:
        dq.append(num)

print(', '.join(answer), end='')
print('>')