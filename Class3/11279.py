import sys
import heapq

n = int(sys.stdin.readline())

number_list = [int(sys.stdin.readline()) for _ in range(n)]
hq = []

for number in number_list:
    if number == 0:
        if hq:
            print(-heapq.heappop(hq))
        else:
            print(0)
    else:
        heapq.heappush(hq, -number)