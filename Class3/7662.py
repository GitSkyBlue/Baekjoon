import sys
import heapq
from collections import defaultdict

n = int(sys.stdin.readline())

for _ in range(n):
    m = int(sys.stdin.readline())
    order_list = [sys.stdin.readline().strip() for _ in range(m)]
    max_hq = []
    min_hq = []
    check = defaultdict(int)

    for order in order_list:
        o, v = order.split()
        v = int(v)
        if o == 'I':
            heapq.heappush(max_hq, -v)
            heapq.heappush(min_hq, v)
        elif o == 'D':
            if v == -1:
                c = heapq.heappop(min_hq)
                check[-c] += 1
            elif v == 1:
                c = heapq.heappop(max_hq)
                check[-c] += 1
            
                
        print(min_hq, max_hq)
# 7
# I 16
# I -5643
# D -1
# D 1
# D 1
# I 123
# D -1            
            
    # if len(result) == 0:
    #     sys.stdout.write('EMPTY\n')
    # else:
    #     sys.stdout.write(f'{str(result[-1])} {str(result[0])}\n')