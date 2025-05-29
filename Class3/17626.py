import sys
import math
n = int(sys.stdin.readline())

for i in range(4):
    print(math.sqrt(n))
    n -= int(math.sqrt(n)) ** 2
    if n == 0:
        break

print(i + 1)