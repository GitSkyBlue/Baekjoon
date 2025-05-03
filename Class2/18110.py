import sys, math
from collections import deque

ratings = deque(sorted(list(map(int, sys.stdin.read().splitlines()[1:]))))
if len(ratings) == 0:
    print(0)
else:
    for i in range(math.floor(len(ratings) * 0.15 + 0.5)):
        ratings.popleft()
        ratings.pop()
    
    print(math.floor(sum(ratings) / len(ratings) + 0.5))