import sys
import math

n = int(sys.stdin.readline())
result = 0
for i in range(n // 2, -1, -1):
    l = []
    l.append([2] * i)
    l.append([1] * (n - i * 2))
    result += math.factorial(len(l[0] + l[1])) // (math.factorial(len(l[0])) * math.factorial(len(l[1])))

sys.stdout.write(str(result % 10007))
