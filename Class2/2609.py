import math

n, m = map(int, input().split())

max_num = max(n, m)
min_num = min(n, m)

print(math.gcd(n, m))

for i in range(1, min_num + 1):
    if max_num * i % min_num == 0:
        print(max_num * i)
        break
else:
    print(n * m)