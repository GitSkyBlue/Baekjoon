import sys
from collections import deque

n = int(input())

dq = deque()

order_list = sys.stdin.read().splitlines()

for order in order_list:
    if order[:2] == 'pu':
        dq.appendleft(order.split()[-1])
    elif order == 'front':
        print(-1 if len(dq) == 0 else dq[-1])
    elif order == 'back':
        print(-1 if len(dq) == 0 else dq[0])
    elif order == 'empty':
        print(1 if len(dq) == 0 else 0)
    elif order == 'size':
        print(len(dq))
    elif order == 'pop':
        print(-1 if len(dq) == 0 else dq.pop())
        
