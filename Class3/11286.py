import sys
import heapq

n = int(sys.stdin.readline())

order_list = [int(sys.stdin.readline()) for _ in range(n)]

hq = []
valid = {}
for order in order_list:
    if order != 0:
        heapq.heappush(hq, abs(order))
        if order in valid:
            valid[order] += 1
        else:
            valid[order] = 1
    else:
        if len(hq) == 0:
            print(0)
        else:
            num = heapq.heappop(hq)
            if -num in valid:
                print(-num)
                if valid[-num] > 1:
                    valid[-num] -= 1
                else:
                    del valid[-num]
            else:
                print(num)
                if valid[num] > 1:
                    valid[num] -= 1
                else:
                    del valid[num]
            