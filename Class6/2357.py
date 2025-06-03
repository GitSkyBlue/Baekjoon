import sys
import heapq

n, m = map(int, sys.stdin.readline().split())

max_number = []
min_number = []

for _ in range(n):
    num = int(sys.stdin.readline())
    max_number.append(-num)
    min_number.append(num)

for _ in range(m):
    start, end = map(int, sys.stdin.readline().split())
    ordered_min_number = min_number[start - 1:end]
    ordered_max_number = max_number[start - 1:end]
    heapq.heapify(ordered_min_number)
    heapq.heapify(ordered_max_number)
    sys.stdout.write(str(heapq.heappop(ordered_min_number)) + ' ' + str(-heapq.heappop(ordered_max_number)) + '\n')

