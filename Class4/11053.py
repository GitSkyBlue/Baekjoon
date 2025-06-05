import sys

n = int(sys.stdin.readline())
number_list = list(map(int, sys.stdin.readline().split()))
dp = [1 for _ in range(1, len(number_list) + 1)]

for i in range(n):
    for j in range(i):
        if number_list[i] > number_list[j]:
            dp[i] = max(dp[i], dp[j] + 1)
print(max(dp))
