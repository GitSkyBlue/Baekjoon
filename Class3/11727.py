import sys
import math

n = int(sys.stdin.readline())
result = 0
for i in range(n // 2, -1, -1):
    l = [[2] * i, [1] * (n - i * 2)]
    plus = 0
    for j in range(i, -1, -1):
        plus += math.factorial(i) // (math.factorial(i - j) * math.factorial(j))
    result += math.factorial(len(l[0] + l[1])) // (math.factorial(len(l[0])) * math.factorial(len(l[1]))) * plus

sys.stdout.write(str(result % 10007))
