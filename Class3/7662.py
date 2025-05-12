import sys
from collections import deque

n = int(sys.stdin.readline())
for _ in range(n):
    dq = deque()
    k = int(sys.stdin.readline().strip())
    order_list = [sys.stdin.readline().strip() for _ in range(k)]

    for order in order_list:
        id, rank = order.split()
        if id == 'I':
            dq.append(int(rank))
        else:
            if len(dq) != 0:
                if rank == '-1':
                    dq.remove(min(dq))
                else:
                    dq.remove(max(dq))
    
    sys.stdout.write(f'{max(dq)} {min(dq)}\n' if len(dq) != 0 else 'EMPTY\n')